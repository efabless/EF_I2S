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

`define     PED(clk, sig, pulse)    reg last_``sig``; wire pulse; always @(posedge clk) last_``sig`` <= sig; assign pulse = sig & ~last_``sig``;
`define     NED(clk, sig, pulse)    reg last_n``sig``; wire pulse; always @(posedge clk) last_n``sig`` <= sig; assign pulse = ~sig & last_n``sig``;
`define     PNED(clk, sig, ppulse, npulse)    reg last_``sig``; wire npulse, ppulse; always @(posedge clk) last_``sig`` <= sig; assign npulse = ~sig & last_``sig``; assign ppulse = sig & ~last_``sig``;


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

    `PNED(clk, ws,  ws_ppulse, ws_npulse)
    `PED(clk, sck, sck_pulse)

    `NED(clk, sck, sck_npulse)
    `PNED(clk, ws_dly,  ws_dly_ppulse, ws_dly_npulse)
    
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
    
    always @(posedge clk or negedge rst_n)
        if(!rst_n)
            rdy <= 1'b0;
        else if(left_justified)
            rdy <= ws_pulse;
        else
            rdy <= ws_dly_pulse;

endmodule

module I2SFIFO #(parameter DW=8, AW=4)(
    input       wire            clk,
    input       wire            rst_n,
    input       wire            rd,
    input       wire            wr,
    input       wire            clr,
    input       wire [DW-1:0]   w_data,
    output      wire            empty,
    output      wire            full,
    output      wire [DW-1:0]   r_data,
    output      wire [AW-1:0]   level    
);

    localparam  DEPTH = 2**AW;

    //Internal Signal declarations
    reg [DW-1:0]  array_reg [DEPTH-1:0];
    reg [AW-1:0]  w_ptr_reg;
    reg [AW-1:0]  w_ptr_next;
    reg [AW-1:0]  w_ptr_succ;
    reg [AW-1:0]  r_ptr_reg;
    reg [AW-1:0]  r_ptr_next;
    reg [AW-1:0]  r_ptr_succ;

  // Level
    reg [AW-1:0] level_reg;
    reg [AW-1:0] level_next;      
    reg full_reg;
    reg empty_reg;
    reg full_next;
    reg empty_next;
  
  wire w_en;
  

  always @ (posedge clk)
    if(w_en)
    begin
      array_reg[w_ptr_reg] <= w_data;
    end

  assign r_data = array_reg[r_ptr_reg];   

  assign w_en = wr & ~full_reg;           

//State Machine
  always @ (posedge clk, negedge rst_n)
  begin
    if(!rst_n) begin
        w_ptr_reg   <= 0;
        r_ptr_reg   <= 0;
        full_reg    <= 1'b0;
        empty_reg   <= 1'b1;
        level_reg   <= 4'd0;
    end
    else if(clr) begin
        w_ptr_reg   <= 0;
        r_ptr_reg   <= 0;
        full_reg    <= 1'b0;
        empty_reg   <= 1'b1;
        level_reg   <= 4'd0;
    end
    else begin
        w_ptr_reg   <= w_ptr_next;
        r_ptr_reg   <= r_ptr_next;
        full_reg    <= full_next;
        empty_reg   <= empty_next;
        level_reg   <= level_next;
      end
  end


//Next State Logic
  always @*
  begin
    w_ptr_succ = w_ptr_reg + 1;
    r_ptr_succ = r_ptr_reg + 1;
    
    w_ptr_next = w_ptr_reg;
    r_ptr_next = r_ptr_reg;
    full_next = full_reg;
    empty_next = empty_reg;
    level_next = level_reg;
    
    case({w_en,rd})
      //2'b00: nop
      2'b01:
        if(~empty_reg)
          begin
            r_ptr_next = r_ptr_succ;
            full_next = 1'b0;
            level_next = level_reg - 1;
            if (r_ptr_succ == w_ptr_reg)
              empty_next = 1'b1;
          end
      2'b10:
        if(~full_reg)
          begin
            w_ptr_next = w_ptr_succ;
            empty_next = 1'b0;
            level_next = level_reg + 1;
            if (w_ptr_succ == r_ptr_reg)
              full_next = 1'b1;
          end
      2'b11:
        begin
          w_ptr_next = w_ptr_succ;
          r_ptr_next = r_ptr_succ;
        end
    endcase
  end

    //Set Full and Empty

  assign full = full_reg;
  assign empty = empty_reg;

  assign level = level_reg;
  
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
    
    assign      fifo_level_above = fifo_level > fifo_level_threshold;

    // Averaging Logic
    reg  [31:0] sum;
    reg  [4:0]  sum_ctr;
    wire [31:0] sample_value = (fifo_wdata[31]) ? ~fifo_wdata : fifo_wdata;
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            sum_ctr <= 'b0;
        else
            if(sample_rdy)
                sum_ctr <= sum_ctr + 1'b1;
    
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            sum <= 'b0;
        else if(sample_rdy & |(current_channel & channels))
            if(sum_ctr == 5'b0)
                sum = sample_value;
            else
               if(avg_en) sum = sum + sample_value;

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

    I2SFIFO #(.DW(DW), .AW(AW)) I2SFIFO (
        .clk(clk),
        .rst_n(rst_n),
        .clr(fifo_clr),
        .rd(fifo_rd),
        .wr(fifo_wr),
        .w_data(fifo_wdata),
        .empty(fifo_empty),
        .full(fifo_full),
        .r_data(fifo_rdata),
        .level(fifo_level)    
    );

endmodule
