PLUSARGS += "+UVM_VERBOSITY=UVM_MEDUIM"
TOPLEVEL := top
MODULE   ?= top_module
PDK_FILES ?= /home/nouran/PDK_cheetah_v3/sky130A/libs.ref/sky130_fd_sc_hd/verilog/primitives.v /home/nouran/PDK_cheetah_v3/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v
AHB_FILES ?=$(PWD)/../../hdl/rtl/bus_wrappers/EF_I2S_AHBL.pp.v
APB_FILES ?=$(PWD)/../../hdl/rtl/bus_wrappers/EF_I2S_APB.pp.v
WB_FILES ?=$(PWD)/../../hdl/rtl/bus_wrappers/EF_I2S_WB.pp.v 
HDL_FILES ?= $(PWD)/IP_Utilities/rtl/aucohl_lib.v $(PWD)/../../hdl/rtl/EF_I2S.v
VERILOG_SOURCES ?=  $(PWD)/top.v $(AHB_FILES) $(APB_FILES) $(WB_FILES) $(HDL_FILES) $(PDK_FILES)
RTL_MACROS += -DUSE_POWER_PINS -DFUNCTIONAL -DUNIT_DELAY=\#1  # Add macros needed
BUS_TYPE ?= APB
ifeq ($(BUS_TYPE),APB)
    RTL_MACROS += -DBUS_TYPE_APB
	DESIGN_NAME = EF_I2S_APB
    export CLK_MAKEFILE = PCLK
    export RST_MAKEFILE = PRESETn
else ifeq ($(BUS_TYPE),AHB)
    RTL_MACROS += -DBUS_TYPE_AHB
	DESIGN_NAME = EF_I2S_AHBL
    export CLK_MAKEFILE = HCLK
    export RST_MAKEFILE = HRESETn
else ifeq ($(BUS_TYPE),WISHBONE)
    RTL_MACROS += -DBUS_TYPE_WISHBONE
	DESIGN_NAME = EF_I2S_WB
    export CLK_MAKEFILE = clk_i
    export RST_MAKEFILE = rst_i
endif
# RTL_MACROS ?= "-DSKIP_WAVE_DUMP"
## netlist Gen 
GL_MACROS += -DFUNCTIONAL  $(RTL_MACROS) -DUNIT_DELAY=\#1
PRE_SYS_FILES = $(AHB_FILES) $(APB_FILES) $(WB_FILES) $(HDL_FILES)
PDK_DIR = $(HOME)/.volare/volare/sky130/versions/bdc9412b3e468c102d01b7cf6337be06ec6e9c9a/sky130A/
PDK_FILES = $(PDK_DIR)/libs.ref/sky130_fd_sc_hd/verilog/primitives.v $(PDK_DIR)/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v # get this from openlane logs in the future 
POST_SYS_FILES = $(PWD)/top.v $(VIP_FILES) $(PWD)/../../hdl/gl/synthesis/nl/$(DESIGN_NAME).nl.v

YAML_FILE = $(PWD)/../../EF_I2S.yaml
MAKEFLAGS += --no-print-directory

# List of tests
TESTS := i2s_left_channel_test  i2s_right_channel_test  i2s_stereo_test i2s_fifo_interrupts_test i2s_averaging_test WriteReadRegsTest

# Variable for tag - set this as required
SIM_TAG ?= default_tag

# Define SIM_PATH variable
SIM_PATH := $(PWD)/sim/$(SIM_TAG)

# Check and clone EF_UVM repository at the beginning of the Makefile execution
clone_ip_util := $(shell if [ ! -d "IP_Utilities" ]; then \
	echo "Cloning the IP_Utilities repository..."; \
	git clone https://github.com/shalan/IP_Utilities.git; \
fi;)

clone_ef_uvm := $(shell if [ ! -d "EF_UVM" ]; then \
	echo "Cloning the EF_UVM repository..."; \
	git clone https://github.com/efabless/EF_UVM.git; \
fi;)


include EF_UVM/Makefile.test
