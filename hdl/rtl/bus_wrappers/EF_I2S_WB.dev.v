/*
	Copyright 2024 Efabless Corp.

	Author: Efabless Corp. (ip_admin@efabless.com)

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

module EF_I2S_WB #( 
	parameter	
		DW = 32,
		AW = 4
) (
`ifdef USE_POWER_PINS
	inout VPWR,
	inout VGND,
`endif
	`WB_SLAVE_PORTS,
	output	wire	[1-1:0]	ws,
	output	wire	[1-1:0]	sck,
	input	wire	[1-1:0]	sdi
);

	localparam	RXDATA_REG_OFFSET = `WB_AW'h0000;
	localparam	PR_REG_OFFSET = `WB_AW'h0004;
	localparam	AVGT_REG_OFFSET = `WB_AW'h0008;
	localparam	ZCRT_REG_OFFSET = `WB_AW'h000C;
	localparam	CTRL_REG_OFFSET = `WB_AW'h0010;
	localparam	CFG_REG_OFFSET = `WB_AW'h0014;
	localparam	RX_FIFO_LEVEL_REG_OFFSET = `WB_AW'hFE00;
	localparam	RX_FIFO_THRESHOLD_REG_OFFSET = `WB_AW'hFE04;
	localparam	RX_FIFO_FLUSH_REG_OFFSET = `WB_AW'hFE08;
	localparam	IM_REG_OFFSET = `WB_AW'hFF00;
	localparam	MIS_REG_OFFSET = `WB_AW'hFF04;
	localparam	RIS_REG_OFFSET = `WB_AW'hFF08;
	localparam	IC_REG_OFFSET = `WB_AW'hFF0C;

    reg [0:0] GCLK_REG;
    wire clk_g;

    wire clk_gated_en = GCLK_REG[0];
    ef_util_gating_cell clk_gate_cell(
        `ifdef USE_POWER_PINS 
        .vpwr(VPWR),
        .vgnd(VGND),
        `endif // USE_POWER_PINS
        .clk(clk_i),
        .clk_en(clk_gated_en),
        .clk_o(clk_g)
    );
    
	wire		clk = clk_g;
	wire		rst_n = (~rst_i);


	`WB_CTRL_SIGNALS

	wire [1-1:0]	fifo_en;
	wire [1-1:0]	fifo_rd;
	wire [AW-1:0]	fifo_level_threshold;
	wire [1-1:0]	fifo_flush;
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
	wire [1-1:0]	avg_en;
	wire [1-1:0]	avg_sel;
	wire [32-1:0]	zcr_threshold;
	wire [1-1:0]	zcr_flag;
	wire [1-1:0]	zcr_en;
	wire [1-1:0]	zcr_sel;
	wire [1-1:0]	vad_flag;
	wire [2-1:0]	channels;
	wire [1-1:0]	en;

	// Register Definitions
	wire	[32-1:0]	RXDATA_WIRE;

	reg [7:0]	PR_REG;
	assign	sck_prescaler = PR_REG;
	`WB_REG(PR_REG, 0, 8)

	reg [31:0]	AVGT_REG;
	assign	avg_threshold = AVGT_REG;
	`WB_REG(AVGT_REG, 0, 32)

	reg [31:0]	ZCRT_REG;
	assign	zcr_threshold = ZCRT_REG;
	`WB_REG(ZCRT_REG, 0, 32)

	reg [3:0]	CTRL_REG;
	assign	en	=	CTRL_REG[0 : 0];
	assign	fifo_en	=	CTRL_REG[1 : 1];
	assign	avg_en	=	CTRL_REG[2 : 2];
	assign	zcr_en	=	CTRL_REG[3 : 3];
	`WB_REG(CTRL_REG, 'h0, 4)

	reg [11:0]	CFG_REG;
	assign	channels	=	CFG_REG[1 : 0];
	assign	sign_extend	=	CFG_REG[2 : 2];
	assign	left_justified	=	CFG_REG[3 : 3];
	assign	sample_size	=	CFG_REG[9 : 4];
	assign	avg_sel	=	CFG_REG[10 : 10];
	assign	zcr_sel	=	CFG_REG[11 : 11];
	`WB_REG(CFG_REG, 'h201, 12)

	wire [AW-1:0]	RX_FIFO_LEVEL_WIRE;
	assign	RX_FIFO_LEVEL_WIRE[(AW - 1) : 0] = fifo_level;

	reg [AW-1:0]	RX_FIFO_THRESHOLD_REG;
	assign	fifo_level_threshold	=	RX_FIFO_THRESHOLD_REG[(AW - 1) : 0];
	`WB_REG(RX_FIFO_THRESHOLD_REG, 0, AW)

	reg [0:0]	RX_FIFO_FLUSH_REG;
	assign	fifo_flush	=	RX_FIFO_FLUSH_REG[0 : 0];
	`WB_REG_AC(RX_FIFO_FLUSH_REG, 0, 1, 1'h0)

	localparam	GCLK_REG_OFFSET = `WB_AW'hFF10;
	`WB_REG(GCLK_REG, 0, 1)

	reg [5:0] IM_REG;
	reg [5:0] IC_REG;
	reg [5:0] RIS_REG;

	`WB_MIS_REG(6)
	`WB_REG(IM_REG, 0, 6)
	`WB_IC_REG(6)

	wire [0:0] FIFOE = fifo_empty;
	wire [0:0] FIFOA = fifo_level_above;
	wire [0:0] FIFOF = fifo_full;
	wire [0:0] AVGF = avg_flag;
	wire [0:0] ZCRF = zcr_flag;
	wire [0:0] VADF = vad_flag;


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
		for(_i_ = 4; _i_ < 5; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(ZCRF[_i_ - 4] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
		for(_i_ = 5; _i_ < 6; _i_ = _i_ + 1) begin
			if(IC_REG[_i_]) RIS_REG[_i_] <= 1'b0; else if(VADF[_i_ - 5] == 1'b1) RIS_REG[_i_] <= 1'b1;
		end
	end

	assign IRQ = |MIS_REG;

	reg [0:0]	_sdi_reg_[1:0];
	wire		_sdi_w_ = _sdi_reg_[1];
	always@(posedge clk_i or posedge rst_i)
		if(rst_i == 1) begin
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
		.fifo_flush(fifo_flush),
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
		.avg_en(avg_en),
		.avg_sel(avg_sel),
		.zcr_threshold(zcr_threshold),
		.zcr_flag(zcr_flag),
		.zcr_en(zcr_en),
		.zcr_sel(zcr_sel),
		.vad_flag(vad_flag),
		.channels(channels),
		.en(en),
		.ws(ws),
		.sck(sck),
		.sdi(_sdi_w_)
	);

	assign	dat_o = 
			(adr_i[`WB_AW-1:0] == RXDATA_REG_OFFSET)	? RXDATA_WIRE :
			(adr_i[`WB_AW-1:0] == PR_REG_OFFSET)	? PR_REG :
			(adr_i[`WB_AW-1:0] == AVGT_REG_OFFSET)	? AVGT_REG :
			(adr_i[`WB_AW-1:0] == ZCRT_REG_OFFSET)	? ZCRT_REG :
			(adr_i[`WB_AW-1:0] == CTRL_REG_OFFSET)	? CTRL_REG :
			(adr_i[`WB_AW-1:0] == CFG_REG_OFFSET)	? CFG_REG :
			(adr_i[`WB_AW-1:0] == RX_FIFO_LEVEL_REG_OFFSET)	? RX_FIFO_LEVEL_WIRE :
			(adr_i[`WB_AW-1:0] == RX_FIFO_THRESHOLD_REG_OFFSET)	? RX_FIFO_THRESHOLD_REG :
			(adr_i[`WB_AW-1:0] == RX_FIFO_FLUSH_REG_OFFSET)	? RX_FIFO_FLUSH_REG :
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
