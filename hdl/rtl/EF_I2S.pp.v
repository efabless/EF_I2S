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

    reg last_ws; wire ws_npulse, ws_ppulse; always @(posedge clk) last_ws <= ws; assign ws_npulse = ~ws & last_ws; assign ws_ppulse = ws & ~last_ws;
    reg last_sck; wire sck_pulse; always @(posedge clk) last_sck <= sck; assign sck_pulse = sck & ~last_sck;

    reg last_nsck; wire sck_npulse; always @(posedge clk) last_nsck <= sck; assign sck_npulse = ~sck & last_nsck;
    reg last_ws_dly; wire ws_dly_npulse, ws_dly_ppulse; always @(posedge clk) last_ws_dly <= ws_dly; assign ws_dly_npulse = ~ws_dly & last_ws_dly; assign ws_dly_ppulse = ws_dly & ~last_ws_dly;
    
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
    reg  [4:0]  sum_ctr;
    wire [31:0] sample_value = (fifo_wdata[31]) ? ~fifo_wdata : fifo_wdata;
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            sum_ctr <= 'b0;
        else
            if(sample_rdy & |(current_channel & channels))
                sum_ctr <= sum_ctr + 1'b1;
    
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            sum <= 'b0;
        else if(sample_rdy & |(current_channel & channels))
            if(sum_ctr == 5'b0)
                sum <= sample_value;
            else
               if(avg_en) sum <= sum + sample_value;

    assign avg_flag = avg_en & (sum[31:5] > avg_threshold);

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
