
/*
	Copyright 2023 Efabless Corp.

	Author: Mohamed Shalan (mshalan@efabless.com)

	This file is auto-generated by wrapper_gen.py on 2023-11-06

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


`timescale			1ns/1ns
`default_nettype	none

`define		APB_BLOCK(name, init)		always @(posedge PCLK or negedge PRESETn) if(~PRESETn) name <= init;
`define		APB_REG(name, init, size)	`APB_BLOCK(name, init) else if(apb_we & (PADDR[15:0]==``name``_ADDR)) name <= PWDATA[``size``-1:0];
`define		APB_ICR(size)				`APB_BLOCK(ICR_REG, ``size``'b0) else if(apb_we & (PADDR[15:0]==ICR_REG_ADDR)) ICR_REG <= PWDATA[``size``-1:0]; else ICR_REG <= ``size``'d0;

module EF_I2S_apb (
	output	wire 		ws,
	output	wire 		sck,
	input	wire 		sdi,
	output	wire 		sdo,
	input	wire 		PCLK,
	input	wire 		PRESETn,
	input	wire [31:0]	PADDR,
	input	wire 		PWRITE,
	input	wire 		PSEL,
	input	wire 		PENABLE,
	input	wire [31:0]	PWDATA,
	output	wire [31:0]	PRDATA,
	output	wire 		PREADY,
	output	wire 		irq
);
	localparam[15:0] RXDATA_REG_ADDR = 16'h0000;
	localparam[15:0] PRESCALE_REG_ADDR = 16'h0004;
	localparam[15:0] FIFOLEVEL_REG_ADDR = 16'h0008;
	localparam[15:0] RXFIFOT_REG_ADDR = 16'h000c;
	localparam[15:0] CONTROL_REG_ADDR = 16'h0010;
	localparam[15:0] CONFIG_REG_ADDR = 16'h0014;
	localparam[15:0] ICR_REG_ADDR = 16'h0f00;
	localparam[15:0] RIS_REG_ADDR = 16'h0f04;
	localparam[15:0] IM_REG_ADDR = 16'h0f08;
	localparam[15:0] MIS_REG_ADDR = 16'h0f0c;

	reg	[7:0]	PRESCALE_REG;
	reg	[4:0]	RXFIFOT_REG;
	reg	[0:0]	CONTROL_REG;
	reg	[4:0]	CONFIG_REG;
	reg	[2:0]	RIS_REG;
	reg	[2:0]	ICR_REG;
	reg	[2:0]	IM_REG;

	wire[31:0]	fifo_rdata;
	wire[31:0]	RXDATA_REG	= fifo_rdata;
	wire[7:0]	sck_prescaler	= PRESCALE_REG[7:0];
	wire[4:0]	fifo_level;
	wire[4:0]	FIFOLEVEL_REG	= fifo_level;
	wire[4:0]	fifo_level_threshold	= RXFIFOT_REG[4:0];
	wire		en	= CONTROL_REG[0:0];
	wire[1:0]	channels	= CONFIG_REG[1:0];
	wire		sign_extend	= CONFIG_REG[2:2];
	wire		left_justified	= CONFIG_REG[3:3];
	wire[4:0]	sample_size	= CONFIG_REG[8:4];
	wire		fifo_empty;
	wire		_EMPTY_FLAG_FLAG_	= fifo_empty;
	wire		fifo_level_above;
	wire		_ABOVE_FLAG_FLAG_	= fifo_level_above;
	wire		fifo_full;
	wire		_FULL_FLAG_FLAG_	= fifo_full;
	wire[2:0]	MIS_REG	= RIS_REG & IM_REG;
	wire		apb_valid	= PSEL & PENABLE;
	wire		apb_we	= PWRITE & apb_valid;
	wire		apb_re	= ~PWRITE & apb_valid;
	wire		_clk_	= PCLK;
	wire		_rst_	= ~PRESETn;
	wire		fifo_rd	= (apb_re & (PADDR[15:0]==RXDATA_REG_ADDR));

	EF_I2S inst_to_wrap (
		.clk(_clk_),
		.rst_n(~_rst_),
		.ws(ws),
		.sck(sck),
		.sdi(sdi),
		.sdo(sdo),
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
		.channels(channels),
		.en(en)
	);

	`APB_REG(PRESCALE_REG, 0, 8)
	`APB_REG(RXFIFOT_REG, 0, 5)
	`APB_REG(CONTROL_REG, 0, 1)
	`APB_REG(CONFIG_REG, 0, 5)
	`APB_REG(IM_REG, 0, 3)

	`APB_ICR(3)

	always @(posedge PCLK or negedge PRESETn)
		if(~PRESETn) RIS_REG <= 3'd0;
		else begin
			if(_EMPTY_FLAG_FLAG_) RIS_REG[0] <= 1'b1; else if(ICR_REG[0]) RIS_REG[0] <= 1'b0;
			if(_ABOVE_FLAG_FLAG_) RIS_REG[1] <= 1'b1; else if(ICR_REG[1]) RIS_REG[1] <= 1'b0;
			if(_FULL_FLAG_FLAG_) RIS_REG[2] <= 1'b1; else if(ICR_REG[2]) RIS_REG[2] <= 1'b0;

		end

	assign irq = |MIS_REG;

	assign	PRDATA = 
			(PADDR[15:0] == PRESCALE_REG_ADDR) ? PRESCALE_REG :
			(PADDR[15:0] == RXFIFOT_REG_ADDR) ? RXFIFOT_REG :
			(PADDR[15:0] == CONTROL_REG_ADDR) ? CONTROL_REG :
			(PADDR[15:0] == CONFIG_REG_ADDR) ? CONFIG_REG :
			(PADDR[15:0] == RIS_REG_ADDR) ? RIS_REG :
			(PADDR[15:0] == ICR_REG_ADDR) ? ICR_REG :
			(PADDR[15:0] == IM_REG_ADDR) ? IM_REG :
			(PADDR[15:0] == RXDATA_REG_ADDR) ? RXDATA_REG :
			(PADDR[15:0] == FIFOLEVEL_REG_ADDR) ? FIFOLEVEL_REG :
			(PADDR[15:0] == MIS_REG_ADDR) ? MIS_REG :
			32'hDEADBEEF;


	assign PREADY = 1'b1;

endmodule
