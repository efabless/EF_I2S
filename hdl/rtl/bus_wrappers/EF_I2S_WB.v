/*
	Copyright 2023 Efabless Corp.

	Author: Mohamed Shalan (mshalan@efabless.com)

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	    http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

*/

/* THIS FILE IS GENERATED, DO NOT EDIT */

`timescale			1ns/1ps
`default_nettype	none

`define				WB_AW		16

`include			"wb_wrapper.vh"

module EF_I2S_WB (
	`WB_SLAVE_PORTS,
	output	[0:0]	ws,
	output	[0:0]	sck,
	input	[0:0]	sdi
);

	localparam	RXDATA_REG_OFFSET = `WB_AW'd0;
	localparam	PR_REG_OFFSET = `WB_AW'd4;
	localparam	FIFOLEVEL_REG_OFFSET = `WB_AW'd8;
	localparam	RXFIFOT_REG_OFFSET = `WB_AW'd12;
	localparam	AVGT_REG_OFFSET = `WB_AW'd16;
	localparam	CTRL_REG_OFFSET = `WB_AW'd20;
	localparam	CFG_REG_OFFSET = `WB_AW'd24;
	localparam	IM_REG_OFFSET = `WB_AW'd3840;
	localparam	MIS_REG_OFFSET = `WB_AW'd3844;
	localparam	RIS_REG_OFFSET = `WB_AW'd3848;
	localparam	IC_REG_OFFSET = `WB_AW'd3852;

	wire		clk = clk_i;
	wire		rst_n = (~rst_i);


	`WB_CTRL_SIGNALS

	wire [1-1:0]	fifo_rd;
	wire [5-1:0]	fifo_level_threshold;
	wire [1-1:0]	fifo_full;
	wire [1-1:0]	fifo_empty;
	wire [5-1:0]	fifo_level;
	wire [1-1:0]	fifo_level_above;
	wire [32-1:0]	fifo_rdata;
	wire [1-1:0]	sign_extend;
	wire [1-1:0]	left_justified;
	wire [5-1:0]	sample_size;
	wire [8-1:0]	sck_prescaler;
	wire [1-1:0]	avg_flag;
	wire [2-1:0]	channels;
	wire [1-1:0]	en;

	wire	[32-1:0]	RXDATA_WIRE;

	reg [8-1:0]	PR_REG;
	assign	sck_prescaler = PR_REG;
	`WB_REG(PR_REG, 0, 8)

	wire [5-1:0]	FIFOLEVEL_WIRE;
	assign	FIFOLEVEL_WIRE = fifo_level;

	reg [5-1:0]	RXFIFOT_REG;
	assign	fifo_level_threshold = RXFIFOT_REG;
	`WB_REG(RXFIFOT_REG, 0, 5)

	reg [32-1:0]	AVGT_REG;
	assign	avg_threshold = AVGT_REG;
	`WB_REG(AVGT_REG, 0, 32)

	reg [2-1:0]	CTRL_REG;
	assign	en	=	CTRL_REG[0 : 0];
	assign	fifo_en	=	CTRL_REG[1 : 1];
	`WB_REG(CTRL_REG, 'h0, 2)

	reg [9-1:0]	CFG_REG;
	assign	channels	=	CFG_REG[1 : 0];
	assign	sign_extend	=	CFG_REG[2 : 2];
	assign	left_justified	=	CFG_REG[3 : 3];
	assign	sample_size	=	CFG_REG[9 : 4];
	`WB_REG(CFG_REG, 'h3F08, 9)

	reg [3:0] IM_REG;
	reg [3:0] IC_REG;
	reg [3:0] RIS_REG;

	`WB_MIS_REG(4)
	`WB_REG(IM_REG, 0, 4)
	`WB_IC_REG(4)

	wire [0:0] FIFOE = fifo_empty;
	wire [0:0] FIFOA = fifo_level_above;
	wire [0:0] FIFOF = fifo_full;
	wire [0:0] AVGF = avg_flag;


	integer _i_;
	`WB_BLOCK(RIS_REG, 0) else begin
		for(_i_ = 0; _i_ < 1; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(FIFOE[_i_ - 0] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 1; _i_ < 2; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(FIFOA[_i_ - 1] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 2; _i_ < 3; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(FIFOF[_i_ - 2] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 3; _i_ < 4; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(AVGF[_i_ - 3] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
	end

	assign IRQ = |MIS_REG;

	EF_I2S instance_to_wrap (
		.clk(clk),
		.rst_n(rst_n),
		.fifo_rd(fifo_rd),
		.fifo_level_threshold(fifo_level_threshold),
		.fifo_full(fifo_full),
		.fifo_empty(fifo_empty),
		.fifo_level(fifo_level),
		.fifo_level_above(fifo_level_above),
		.fifo_rdata(fifo_rdata),
		.sign_extend(sign_extend),
		.left_justified(left_justified),
		.sample_size(sample_size),
		.sck_prescaler(sck_prescaler),
		.avg_flag(avg_flag),
		.channels(channels),
		.en(en),
		.ws(ws),
		.sck(sck),
		.sdi(sdi)
	);

	assign	dat_o = 
			(adr_i[`WB_AW-1:0] == RXDATA_REG_OFFSET)	? RXDATA_WIRE :
			(adr_i[`WB_AW-1:0] == PR_REG_OFFSET)	? PR_REG :
			(adr_i[`WB_AW-1:0] == FIFOLEVEL_REG_OFFSET)	? FIFOLEVEL_WIRE :
			(adr_i[`WB_AW-1:0] == RXFIFOT_REG_OFFSET)	? RXFIFOT_REG :
			(adr_i[`WB_AW-1:0] == AVGT_REG_OFFSET)	? AVGT_REG :
			(adr_i[`WB_AW-1:0] == CTRL_REG_OFFSET)	? CTRL_REG :
			(adr_i[`WB_AW-1:0] == CFG_REG_OFFSET)	? CFG_REG :
			(adr_i[`WB_AW-1:0] == IM_REG_OFFSET)	? IM_REG :
			(adr_i[`WB_AW-1:0] == MIS_REG_OFFSET)	? MIS_REG :
			(adr_i[`WB_AW-1:0] == RIS_REG_OFFSET)	? RIS_REG :
			(adr_i[`WB_AW-1:0] == IC_REG_OFFSET)	? IC_REG :
			32'hDEADBEEF;

	always @ (posedge clk_i or posedge rst_i)
		if(rst_i)
			ack_o <= 1'b0;
		else if(wb_valid & ~ack_o)
			ack_o <= 1'b1;
		else
			ack_o <= 1'b0;
	assign	RXDATA_WIRE = fifo_rdata;
	assign	fifo_rd =  ack_o & (wb_re & (adr_i[`WB_AW-1:0] == RXDATA_REG_OFFSET));
endmodule
