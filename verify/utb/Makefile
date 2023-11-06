SIM-I2S:
	iverilog  -g2012 -s EF_I2S_tb i2s_mic.v ../../hdl/rtl/EF_I2S.v EF_I2S_tb.v
	./a.out

SIM-RTL:
	iverilog  -g2012 -s EF_I2S_apb_tb ../../hdl/rtl/EF_I2S.v ../../hdl/rtl/bus_wrappers/EF_I2S_apb.v EF_I2S_apb_tb.v
	./a.out

SIM-GL:
	iverilog  -g2012 -s EF_I2S_apb_tb ../../hdl/rtl/EF_I2S.v ../../hdl/gl/sky130/EF_I2S_apb.v EF_I2S_apb_tb.v ../../util/tech/sky130/sky130_hd.v
	./a.out
