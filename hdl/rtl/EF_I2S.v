/*
	Copyright 2023 Efabless Corp.

	Author: Mohamed Shalan (mshalan@efabless.com)
	
	Licensed under the Apache License, Version 2.0 (the "License"); 
	you may not use this file except in compliance with the License. 
	You may obtain a copy of the License at:
	http://www.apache.org/licenses/LICENSE-2.0
	Unless required by applicable law or agreed to in writing, software 
	distributed under the License is distributed on an "AS IS" BASIS, 
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
	See the License for the specific language governing permissions and 
	limitations under the License.
*/

`default_nettype        none

`define     PED(clk, sig, pulse)    reg last_``sig``; wire pulse; always @(posedge clk, negedge rst_n) if(!rst_n) last_``sig`` <= 1'b0; else last_``sig`` <= sig; assign pulse = sig & ~last_``sig``;
`define     NED(clk, sig, pulse)    reg last_n``sig``; wire pulse; always @(posedge clk, negedge rst_n) if(!rst_n) last_n``sig`` <= 1'b0; else last_n``sig`` <= sig; assign pulse = ~sig & last_n``sig``;
`define     PNED(clk, sig, ppulse, npulse, rst_val)    reg last_``sig``, npulse, ppulse; always @(posedge clk, negedge rst_n)  if(!rst_n)begin last_``sig`` <= rst_val; npulse <= 1'b0; ppulse <= 1'b0; end else begin last_``sig`` <= sig; npulse <= ~sig & last_``sig``; ppulse <= sig & ~last_``sig``; end


module i2s_rx (
    input   wire        clk,
    input   wire        rst_n,
    input   wire        sd,
    input   wire        ws,
    input   wire        sck,

    input   wire        left_justified,
    output  reg         rdy,
    output  reg  [31:0] sample
);

    reg [31:0] sr;

    reg ws_dly0, ws_dly;

    `PNED(clk, ws,  ws_ppulse, ws_npulse, 1'b1)
    `PED(clk, sck, sck_pulse)

    `NED(clk, sck, sck_npulse)
    `PNED(clk, ws_dly,  ws_dly_ppulse, ws_dly_npulse, 1'b0)
    
    always @(posedge clk or negedge rst_n)
        if(!rst_n) begin
            ws_dly <= 0;
            ws_dly0 <= 0;
        end
        else if(sck_npulse) begin
            ws_dly0 <= ws;
            ws_dly <= ws_dly0;
        end

    wire ws_pulse = ws_ppulse | ws_npulse;
    wire ws_dly_pulse = ws_dly_ppulse | ws_dly_npulse;
    
    always @(posedge clk or negedge rst_n)
        if(!rst_n)
            sr <= 32'b0;
        else
            if(sck_pulse) 
                sr <= {sr[30:0], sd};

    always @(posedge clk or negedge rst_n)
        if(!rst_n)
            sample <= 32'b0;
        else
            if(left_justified & ws_pulse)
                sample <= sr;
            else if(~left_justified & ws_dly_pulse)
                sample <= sr;
    
    // adding a flag to prevent the initial ready assertion 
    reg first; 
    always @(posedge clk or negedge rst_n)
        if(!rst_n)
          first <= 1'b0;
        else if (ws_pulse | ws_dly_pulse)
          first <= 1'b1;

    always @(posedge clk or negedge rst_n)
        if(!rst_n)
            rdy <= 1'b0;
        else if(left_justified)
            rdy <= ws_pulse & first;
        else
            rdy <= ws_dly_pulse & first;

endmodule


module EF_I2S #(parameter DW=32, AW=4) (
    input   wire            clk,
    input   wire            rst_n,

    output  wire            ws,
    output  wire            sck,
    input   wire            sdi,
    //output  wire        sdo,

    input   wire            fifo_en,
    input   wire            fifo_rd,
    input   wire            fifo_clr,
    input   wire [AW-1:0]   fifo_level_threshold,
    input   wire            fifo_flush,
    output  wire            fifo_full,
    output  wire            fifo_empty,
    output  wire [AW-1:0]   fifo_level,
    output  wire            fifo_level_above,
    output  wire [31:0]     fifo_rdata,

    input   wire            sign_extend,
    input   wire            left_justified,
    input   wire [5:0]      sample_size,
    input   wire [7:0]      sck_prescaler,
    input   wire [31:0]     avg_threshold,
    output  wire            avg_flag,
    input   wire            avg_en,
    input   wire            avg_sel,        // 0: 256 samples, 1: 512 samples
    input   wire [31:0]     zcr_threshold,
    output  wire            zcr_flag,
    input   wire            zcr_en,
    input   wire            zcr_sel,        // 0: 256 samples, 1: 512 samples
    
    output  wire            vad_flag,
    
    input   wire [1:0]      channels,       // 10: left, 01: right, 11: both (stereo)
    input   wire            en         
); 

    reg         sck_reg;
    reg         ws_reg;
    reg [7:0]   prescaler;
    reg [4:0]   bit_ctr;

    wire        sample_rdy;

    assign      sck = sck_reg;
    assign      ws = ws_reg;

    //wire [31:0] rsample, lsample;

    wire [31:0]  sample;

    // The prescaler
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            prescaler <= 8'b0;
        else if(en)
            if(prescaler == 8'b0)
                prescaler <= sck_prescaler;
            else 
                prescaler <= prescaler - 1'b1;

    // The Serial Clock (SCK)
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            sck_reg <= 1'b0;
        else if(en==1'b1 && prescaler == 8'b0)
            sck_reg <= !sck_reg;
    
    // The Bit Counter
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            bit_ctr <= 5'b0;
        else if(en == 1'b1 && prescaler == 8'b0 && sck_reg == 1'b1)
            bit_ctr <= bit_ctr + 1'b1;
    
    // Word Select Line Register
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            ws_reg <= 1'b1;
        else
            if(en==1'b1 && bit_ctr==5'b0 && prescaler==8'b0 && sck_reg==1'b1)
                ws_reg <= !ws_reg;

    wire [1:0]  current_channel = 1 << (left_justified == ~ws);
    wire        fifo_wr = fifo_en & sample_rdy & |(current_channel & channels);
    wire [31:0] sample_sign = sign_extend ? {32{sample[31]}} << sample_size : 32'b0;
    wire [31:0] fifo_wdata = (sample >> (32-sample_size)) | sample_sign;
    
    assign      fifo_level_above = (fifo_level > fifo_level_threshold) | fifo_full;

    // Averaging Logic
    reg  [31:0] sum;
    reg  [8:0]  sum_ctr;
    wire [31:0] abs_sample_value = (fifo_wdata[31]) ? ~fifo_wdata : fifo_wdata;
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            sum_ctr <= 'b0;
        else
            if(sample_rdy & |(current_channel & channels))
                sum_ctr <= sum_ctr + 1'b1;
    
    wire sum_ctr_zero = avg_sel ? (sum_ctr == 9'b0) : (sum_ctr[7:0] == 8'b0);

    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            sum <= 'b0;
        else if(sample_rdy & |(current_channel & channels))
            if(sum_ctr_zero)
                sum <= abs_sample_value;
            else
               if(avg_en) sum <= sum + abs_sample_value;

    wire avg_gt_threshold = avg_sel ? (sum[31:9] > avg_threshold) : (sum[31:8] > avg_threshold);
    assign avg_flag = avg_en & (avg_gt_threshold);

    // ZCR Logic
    reg prev_sign;
    reg  [31:0] zcr;
    reg  [8:0]  zc_ctr;
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            zc_ctr <= 'b0;
        else
            if(sample_rdy & |(current_channel & channels))
                zc_ctr <= zc_ctr + 1'b1;
    
    always @(posedge clk, negedge rst_n)
        if(!rst_n)
            prev_sign <= 1'b0;
        else if(sample_rdy & |(current_channel & channels))
            prev_sign <= fifo_wdata[31];

    wire zc_ctr_zero = zcr_sel ? (zc_ctr == 9'b0) : (zc_ctr[7:0] == 8'b0);

    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            zcr <= 'b0;
        else if(sample_rdy & |(current_channel & channels))
            if(zc_ctr_zero)
                zcr <= 0;
            else
                if(zcr_en) zcr <= zcr + (prev_sign ^ fifo_wdata[31]);
    
    wire zcr_gt_threshold = zcr > zcr_threshold;
    assign zcr_flag = zcr_en & (zcr_gt_threshold);

    assign vad_flag = avg_flag & zcr_flag;

    i2s_rx RX (
        .clk(clk),
        .rst_n(rst_n),
        .sd(sdi),
        .ws(ws),
        .sck(sck),
        .left_justified(left_justified),
        .sample(sample),
        .rdy(sample_rdy)
    );

    aucohl_fifo #(.DW(DW), .AW(AW)) I2SFIFO (
        .clk(clk),
        .rst_n(rst_n),
        // .clr(fifo_clr),
        .flush(fifo_flush),
        .rd(fifo_rd),
        .wr(fifo_wr),
        .wdata(fifo_wdata),
        .empty(fifo_empty),
        .full(fifo_full),
        .rdata(fifo_rdata),
        .level(fifo_level)    
    );

endmodule
