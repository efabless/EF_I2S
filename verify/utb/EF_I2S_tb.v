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

`define     CLK(clk, period)        initial clk = 0; always #(period/2) clk = !clk;
`define     RSTn(rst, clk, duration)     initial rst = 1'bx; initial #5 rst = 1'b0; initial begin #duration; @(posedge clk) rst = 1'b1; end

`timescale  1ns/1ps

module EF_I2S_tb;
    reg             clk = 0;
    reg             rst_n;
    wire            sd, sdo;
    wire            ws;
    wire            sck;

    reg             fifo_rd = 1'b0;
    reg [4:0]       fifo_level_threshold = 5;

    wire            fifo_full;
    wire [4:0]      fifo_level;
    wire            fifo_level_above;
    wire [31:0]     fifo_rdata;

    reg  [4:0]      sample_size = 18;    
    reg [7:0]       sck_prescaler = (10/2)-1;


    reg [7:0]       clkdiv;

    localparam      FREQDIV = 10;

    i2s MUV (
        .clk(clk),
        .rst_n(rst_n),
        .sdi(sd),
        .sdo(sdo),
        .ws(ws),
        .sck(sck),

        .fifo_rd(fifo_rd),
        .fifo_level_threshold(fifo_level_threshold),
        .fifo_full(fifo_full),
        .fifo_level(fifo_level),
        .fifo_level_above(fifo_level_above),
        .fifo_rdata(fifo_rdata),

        .sample_size(sample_size),
        .sck_prescaler(sck_prescaler),
        .channels(2'b01),
        .en(1'b1)
    );

    i2s_mic vip (
        .sck(sck),
        .sdo(sd),
        .ws(ws)
    );

    `CLK(clk, 100)
    `RSTn(rst_n, clk, 1000)

    initial begin
        $dumpfile("EF_I2S_tb.vcd");
        $dumpvars;
        #1_000_000 $finish;
    end

    initial begin
        @(posedge fifo_level_above);
        repeat(5) begin
            @(posedge clk);
            fifo_rd <= 1'b1;
            @(posedge clk);
            fifo_rd <= 1'b0;
        end        
    end


endmodule


