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

module EF_I2S_APB #( 
	parameter	
		DW = 32,
		AW = 4
) (
	input wire          PCLK,
                                        input wire          PRESETn,
                                        input wire          PWRITE,
                                        input wire [31:0]   PWDATA,
                                        input wire [31:0]   PADDR,
                                        input wire          PENABLE,
                                        input wire          PSEL,
                                        output wire         PREADY,
                                        output wire [31:0]  PRDATA,
                                        output wire         IRQ
,
	output	[0:0]	ws,
	output	[0:0]	sck,
	input	[0:0]	sdi
);

	localparam	RXDATA_REG_OFFSET = 16'd0;
	localparam	PR_REG_OFFSET = 16'd4;
	localparam	FIFOLEVEL_REG_OFFSET = 16'd8;
	localparam	RXFIFOT_REG_OFFSET = 16'd12;
	localparam	AVGT_REG_OFFSET = 16'd16;
	localparam	CTRL_REG_OFFSET = 16'd20;
	localparam	CFG_REG_OFFSET = 16'd24;
	localparam	IM_REG_OFFSET = 16'd3840;
	localparam	MIS_REG_OFFSET = 16'd3844;
	localparam	RIS_REG_OFFSET = 16'd3848;
	localparam	IC_REG_OFFSET = 16'd3852;

	wire		clk = PCLK;
	wire		rst_n = PRESETn;


	wire		apb_valid   = PSEL & PENABLE;
                                        wire		apb_we	    = PWRITE & apb_valid;
                                        wire		apb_re	    = ~PWRITE & apb_valid;

	wire [1-1:0]	fifo_en;
	wire [1-1:0]	fifo_rd;
	wire [AW-1:0]	fifo_level_threshold;
	wire [1-1:0]	fifo_full;
	wire [1-1:0]	fifo_empty;
	wire [AW-1:0]	fifo_level;
	wire [1-1:0]	fifo_level_above;
	wire [32-1:0]	fifo_rdata;
	wire [1-1:0]	sign_extend;
	wire [1-1:0]	left_justified;
	wire [6-1:0]	sample_size;
	wire [8-1:0]	sck_prescaler;
	wire [32-1:0]	avg_threshold;
	wire [1-1:0]	avg_flag;
	wire [2-1:0]	channels;
	wire [1-1:0]	en;

	wire	[32-1:0]	RXDATA_WIRE;

	reg [8-1:0]	PR_REG;
	assign	sck_prescaler = PR_REG;
	always @(posedge PCLK or negedge PRESETn) if(~PRESETn) PR_REG <= 0;
                                        else if(apb_we & (PADDR[16-1:0]==PR_REG_OFFSET))
                                            PR_REG <= PWDATA[8-1:0];

	wire [AW-1:0]	FIFOLEVEL_WIRE;
	assign	FIFOLEVEL_WIRE = fifo_level;

	reg [AW-1:0]	RXFIFOT_REG;
	assign	fifo_level_threshold = RXFIFOT_REG;
	always @(posedge PCLK or negedge PRESETn) if(~PRESETn) RXFIFOT_REG <= 0;
                                        else if(apb_we & (PADDR[16-1:0]==RXFIFOT_REG_OFFSET))
                                            RXFIFOT_REG <= PWDATA[AW-1:0];

	reg [32-1:0]	AVGT_REG;
	assign	avg_threshold = AVGT_REG;
	always @(posedge PCLK or negedge PRESETn) if(~PRESETn) AVGT_REG <= 0;
                                        else if(apb_we & (PADDR[16-1:0]==AVGT_REG_OFFSET))
                                            AVGT_REG <= PWDATA[32-1:0];

	reg [2-1:0]	CTRL_REG;
	assign	en	=	CTRL_REG[0 : 0];
	assign	fifo_en	=	CTRL_REG[1 : 1];
	always @(posedge PCLK or negedge PRESETn) if(~PRESETn) CTRL_REG <= 'h0;
                                        else if(apb_we & (PADDR[16-1:0]==CTRL_REG_OFFSET))
                                            CTRL_REG <= PWDATA[2-1:0];

	reg [10-1:0]	CFG_REG;
	assign	channels	=	CFG_REG[1 : 0];
	assign	sign_extend	=	CFG_REG[2 : 2];
	assign	left_justified	=	CFG_REG[3 : 3];
	assign	sample_size	=	CFG_REG[9 : 4];
	always @(posedge PCLK or negedge PRESETn) if(~PRESETn) CFG_REG <= 'h3F08;
                                        else if(apb_we & (PADDR[16-1:0]==CFG_REG_OFFSET))
                                            CFG_REG <= PWDATA[10-1:0];

	reg [3:0] IM_REG;
	reg [3:0] IC_REG;
	reg [3:0] RIS_REG;

	wire[4-1:0]      MIS_REG	= RIS_REG & IM_REG;
	always @(posedge PCLK or negedge PRESETn) if(~PRESETn) IM_REG <= 0;
                                        else if(apb_we & (PADDR[16-1:0]==IM_REG_OFFSET))
                                            IM_REG <= PWDATA[4-1:0];
	always @(posedge PCLK or negedge PRESETn) if(~PRESETn) IC_REG <= 4'b0;
                                        else if(apb_we & (PADDR[16-1:0]==IC_REG_OFFSET))
                                            IC_REG <= PWDATA[4-1:0];
                                        else
                                            IC_REG <= 4'd0;

	wire [0:0] FIFOE = fifo_empty;
	wire [0:0] FIFOA = fifo_level_above;
	wire [0:0] FIFOF = fifo_full;
	wire [0:0] AVGF = avg_flag;


	integer _i_;
	always @(posedge PCLK or negedge PRESETn) if(~PRESETn) RIS_REG <= 0; else begin
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

	reg [0:0]	_sdi_reg_[1:0];
	wire		_sdi_w_ = _sdi_reg_[1];
	always@(posedge PCLK or negedge PRESETn)
		if(PRESETn == 0) begin
			_sdi_reg_[0] <= 'b0;
			_sdi_reg_[1] <= 'b0;
		end
		else begin
			_sdi_reg_[0] <= sdi;
			_sdi_reg_[1] <= _sdi_reg_[0];
		end
	EF_I2S #(
		.DW(DW),
		.AW(AW)
	) instance_to_wrap (
		.clk(clk),
		.rst_n(rst_n),
		.fifo_en(fifo_en),
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
		.avg_threshold(avg_threshold),
		.avg_flag(avg_flag),
		.channels(channels),
		.en(en),
		.ws(ws),
		.sck(sck),
		.sdi(_sdi_w_)
	);

	assign	PRDATA = 
			(PADDR[16-1:0] == RXDATA_REG_OFFSET)	? RXDATA_WIRE :
			(PADDR[16-1:0] == PR_REG_OFFSET)	? PR_REG :
			(PADDR[16-1:0] == FIFOLEVEL_REG_OFFSET)	? FIFOLEVEL_WIRE :
			(PADDR[16-1:0] == RXFIFOT_REG_OFFSET)	? RXFIFOT_REG :
			(PADDR[16-1:0] == AVGT_REG_OFFSET)	? AVGT_REG :
			(PADDR[16-1:0] == CTRL_REG_OFFSET)	? CTRL_REG :
			(PADDR[16-1:0] == CFG_REG_OFFSET)	? CFG_REG :
			(PADDR[16-1:0] == IM_REG_OFFSET)	? IM_REG :
			(PADDR[16-1:0] == MIS_REG_OFFSET)	? MIS_REG :
			(PADDR[16-1:0] == RIS_REG_OFFSET)	? RIS_REG :
			(PADDR[16-1:0] == IC_REG_OFFSET)	? IC_REG :
			32'hDEADBEEF;

	assign	PREADY = 1'b1;

	assign	RXDATA_WIRE = fifo_rdata;
	assign	fifo_rd = (apb_re & (PADDR[16-1:0] == RXDATA_REG_OFFSET));
endmodule
