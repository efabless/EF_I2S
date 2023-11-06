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
    input   wire [4:0]  sample_size,
    output  reg  [31:0] lsample,
    output  reg  [31:0] rsample
    
);

    reg last_ws; wire lw_pulse, rw_pulse; always @(posedge clk) last_ws <= ws; assign lw_pulse = ~ws & last_ws; assign rw_pulse = ws & ~last_ws;
    reg last_sck; wire sck_pulse; always @(posedge clk) last_sck <= sck; assign sck_pulse = sck & ~last_sck;
    
    reg [1:0]   lw_state;
    reg [1:0]   lw_state_next;

    reg [4:0]   bit_cnt;

    localparam [1:0] LEFT = 2'b00, RIGHT = 2'b10, LEFT_LSB = 2'b01, RIGHT_LSB = 2'b11; 

    always @(posedge clk or negedge rst_n)
        if(!rst_n)
            lw_state <= RIGHT;
        else
            lw_state <= lw_state_next;

    always @* 
        if(left_justified)
            case (lw_state)
                RIGHT       :   if(lw_pulse)    lw_state_next = LEFT; else lw_state_next = RIGHT;
                LEFT        :   if(rw_pulse)    lw_state_next = RIGHT; else lw_state_next = LEFT;
                default     :   lw_state_next = RIGHT;
            endcase
        else
            case (lw_state)
                RIGHT       :   if(lw_pulse)    lw_state_next = RIGHT_LSB; else lw_state_next = RIGHT;
                RIGHT_LSB   :   if(sck_pulse)   lw_state_next = LEFT; else lw_state_next = RIGHT_LSB;
                LEFT        :   if(rw_pulse)    lw_state_next = LEFT_LSB; else lw_state_next = LEFT;
                LEFT_LSB    :   if(sck_pulse)   lw_state_next = RIGHT; else lw_state_next = LEFT_LSB;
                default     :   lw_state_next = RIGHT;
            endcase

/*
    always @(posedge clk or negedge rst_n)
        if(!rst_n)
            bit_cnt <= 5'b0;
        else
            if(sck_pulse)
                if(lw_state == RIGHT_LSB || lw_state == LEFT_LSB)
                    bit_cnt <= sample_size;
                else
                    bit_cnt <= bit_cnt - 1;
*/
    always @(posedge clk or negedge rst_n)
        if(!rst_n)
            lsample <= 32'b0;
        else
            if(sck_pulse)
                if(lw_state == RIGHT_LSB)
                    lsample <= 32'b0;
                else if((lw_state == LEFT) || (lw_state == LEFT_LSB))
                    lsample <= {lsample[30:0], sd};

    always @(posedge clk or negedge rst_n)
        if(!rst_n)
            rsample <= 32'b0;
        else
            if(sck_pulse)
                if(lw_state == LEFT_LSB)
                    rsample <= 32'b0;
                else if((lw_state == RIGHT) || (lw_state == RIGHT_LSB))
                    rsample <= {rsample[30:0], sd};

endmodule

module I2SFIFO #(parameter DW=8, AW=4)(
    input     wire            clk,
    input     wire            rst_n,
    input     wire            rd,
    input     wire            wr,
    input     wire [DW-1:0]   w_data,
    output    wire            empty,
    output    wire            full,
    output    wire [DW-1:0]   r_data,
    output    wire [AW-1:0]   level    
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
    if(!rst_n)
      begin
        w_ptr_reg <= 0;
        r_ptr_reg <= 0;
        full_reg <= 1'b0;
        empty_reg <= 1'b1;
        level_reg <= 4'd0;
      end
    else
      begin
        w_ptr_reg <= w_ptr_next;
        r_ptr_reg <= r_ptr_next;
        full_reg <= full_next;
        empty_reg <= empty_next;
        level_reg <= level_next;
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

module EF_I2S (
    input   wire        clk,
    input   wire        rst_n,
    
    output   wire        ws,
    output   wire        sck,
    input   wire        sdi,
    output  wire        sdo,

    input   wire        fifo_rd,
    input   wire [4:0]  fifo_level_threshold,
    output  wire        fifo_full,
    output  wire        fifo_empty,
    output  wire [4:0]  fifo_level,
    output  wire        fifo_level_above,
    output  wire [31:0] fifo_rdata,

    input   wire        sign_extend,
    input   wire        left_justified,
    input   wire [4:0]  sample_size,
    input   wire [7:0]  sck_prescaler,
    input   wire [1:0]  channels,
    input   wire        en         // 10: left, 01: right, 11: both (stereo)
); 

    reg         sck_reg;
    reg         ws_reg;
    reg [7:0]   prescaler;
    reg [4:0]   bit_ctr;

    assign      sck = sck_reg;
    assign      ws = ws_reg;

    wire [31:0] rsample, lsample;

    reg [31:0]  sample;

    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            prescaler <= sck_prescaler;
        else if(en)
            if(prescaler == 8'b0)
                prescaler <= sck_prescaler;
            else 
                prescaler <= prescaler - 1'b1;

    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            sck_reg <= 1'b0;
        else if(en==1'b1 && prescaler == 8'b0)
            sck_reg <= !sck_reg;
    
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            bit_ctr <= 5'b0;
        else if(en == 1'b1 && prescaler == 8'b0 && sck_reg == 1'b1)
            bit_ctr <= bit_ctr + 1'b1;
    
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            ws_reg <= 1'b1;
        else
            if(en == 1'b1 && bit_ctr == 5'b0 && prescaler == 8'b0 && sck_reg == 1'b1)
                ws_reg <= !ws_reg;
/*
    always @ (posedge clk, negedge rst_n)
        if(!rst_n)
            sample <= 32'b0;
        else
            if(en == 1'b1 && bit_ctr == 5'b0 && prescaler == 8'b0 && sck_reg == 1'b1)
                if(ws_reg & channels[0]) sample <= (rsample >> (32-sample_size));
                else if(~ws_reg & channels[1]) sample <= (lsample >> (32-sample_size));
*/
    wire        fifo_wr = (en == 1'b1 && bit_ctr == 5'b0 && prescaler == 8'b0 && sck_reg == 1'b1) && ((ws_reg & channels[0]) || (~ws_reg & channels[1]));

    wire [31:0] rsample_sign = sign_extend ? {32{rsample[31]}} << sample_size : 32'b0;
    wire [31:0] lsample_sign = sign_extend ? {32{lsample[31]}} << sample_size : 32'b0;

    wire [31:0] fifo_wdata = ws_reg ?  (rsample >> (32-sample_size)) | rsample_sign : (lsample >> (32-sample_size)) | lsample_sign;

    assign      fifo_level_above = fifo_level > fifo_level_threshold;

    i2s_rx RX (
        .clk(clk),
        .rst_n(rst_n),
        .sd(sdi),
        .ws(ws),
        .sck(sck),
        .left_justified(left_justified),
        .sample_size(sample_size),
        .lsample(lsample),
        .rsample(rsample)
    );

    I2SFIFO #(.DW(32), .AW(5)) I2SFIFO (
        .clk(clk),
        .rst_n(rst_n),
        .rd(fifo_rd),
        .wr(fifo_wr),
        .w_data(fifo_wdata),
        .empty(fifo_empty),
        .full(fifo_full),
        .r_data(fifo_rdata),
        .level(fifo_level)    
    );

endmodule