import cocotb
from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info
from uvm.base.uvm_config_db import UVMConfigDb
from uvm.base.uvm_object_globals import UVM_LOW
from uvm.base.uvm_globals import run_test
from i2s_interface.i2s_if import i2s_if
from EF_UVM.bus_env.bus_interface.bus_if import bus_apb_if, bus_irq_if, bus_ahb_if, bus_wb_if
from cocotb_coverage.coverage import coverage_db
from cocotb.triggers import Event, First, Timer
from EF_UVM.bus_env.bus_regs import bus_regs
from uvm.base import UVMRoot
from EF_UVM.base_test import base_test
import random

# seqences import
from i2s_seq_lib.i2s_config_seq import i2s_config_seq
from i2s_seq_lib.i2s_send_sample_seq import i2s_send_sample_seq
from i2s_seq_lib.i2s_send_right_sample_seq import i2s_send_right_sample_seq
from i2s_seq_lib.i2s_send_left_sample_seq import i2s_send_left_sample_seq
from i2s_seq_lib.i2s_read_rxdata_seq import i2s_read_rxdata_seq
from i2s_seq_lib.i2s_read_ris_seq import i2s_read_ris_seq


# override classes
from EF_UVM.ip_env.ip_agent.ip_driver import ip_driver
from i2s_agent.i2s_driver import i2s_driver
from EF_UVM.ip_env.ip_agent.ip_monitor import ip_monitor
from i2s_agent.i2s_monitor import i2s_monitor
from EF_UVM.ref_model.ref_model import ref_model
from i2s_ref_model.i2s_ref_model import i2s_ref_model
from EF_UVM.ip_env.ip_coverage.ip_coverage import ip_coverage
from i2s_coverage.i2s_coverage import i2s_coverage
from EF_UVM.ip_env.ip_logger.ip_logger import ip_logger
from i2s_logger.i2s_logger import i2s_logger


@cocotb.test()
async def module_top(dut):
    # profiler = cProfile.Profile()
    # profiler.enable()
    BUS_TYPE = cocotb.plusargs['BUS_TYPE']
    pif = i2s_if(dut)
    if BUS_TYPE == "APB":
        w_if = bus_apb_if(dut)
    elif BUS_TYPE == "AHB":
        w_if = bus_ahb_if(dut)
    elif BUS_TYPE == "WISHBONE":
        w_if = bus_wb_if(dut)
    else:
        uvm_fatal("module_top", f"unknown bus type {BUS_TYPE}")
    w_irq_if = bus_irq_if(dut)
    UVMConfigDb.set(None, "*", "ip_if", pif)
    UVMConfigDb.set(None, "*", "bus_if", w_if)
    UVMConfigDb.set(None, "*", "bus_irq_if", w_irq_if)
    yaml_file = []
    UVMRoot().clp.get_arg_values("+YAML_FILE=", yaml_file)
    yaml_file = yaml_file[0]
    regs = bus_regs(yaml_file)
    UVMConfigDb.set(None, "*", "bus_regs", regs)
    UVMConfigDb.set(None, "*", "irq_exist", regs.get_irq_exist())
    UVMConfigDb.set(None, "*", "collect_coverage", True)
    UVMConfigDb.set(None, "*", "disable_logger", False)
    test_path = []
    UVMRoot().clp.get_arg_values("+TEST_PATH=", test_path)
    test_path = test_path[0]
    await run_test()
    coverage_db.export_to_yaml(filename=f"{test_path}/coverage.yalm")
    # profiler.disable()
    # profiler.dump_stats("profile_result.prof")


class i2s_base_test(base_test):
    def __init__(self, name="i2s_first_test", parent=None):
        BUS_TYPE = cocotb.plusargs['BUS_TYPE']
        super().__init__(name, bus_type=BUS_TYPE, parent=parent)
        self.tag = name
        self.config_reg = 0

    def build_phase(self, phase):
        super().build_phase(phase)
        # override
        self.set_type_override_by_type(ip_driver.get_type(), i2s_driver.get_type())
        self.set_type_override_by_type(ip_monitor.get_type(), i2s_monitor.get_type())
        self.set_type_override_by_type(ref_model.get_type(), i2s_ref_model.get_type())
        self.set_type_override_by_type(ip_coverage.get_type(), i2s_coverage.get_type())
        self.set_type_override_by_type(ip_logger.get_type(), i2s_logger.get_type())
        # self.config_reg = self.get_config_reg_val()

    # async def pre_configure_phase(self, phase):
    #     # add background sequences
    #     await super().pre_configure_phase(phase)
    #     phase.raise_objection(self, f"{self.__class__.__name__} pre_configure_phase phase OBJECTED ")
    #     bus_i2s_config_seq = i2s_config_seq("i2s_config_seq")
    #     bus_i2s_config_seq.set_config_reg(self.config_reg)
    #     await bus_i2s_config_seq.start(self.bus_sqr)
    #     phase.drop_objection(
    #         self, f"{self.__class__.__name__} pre_configure_phase phase drop objection"
    #     )

    def get_config_reg_val(self, channel=None, sign_extend= None, left_justify=None, sample_size=None ):
        if channel is None:
            channel_bits = random.choice([0b01, 0b10, 0b11])
        elif channel == "right":
            channel_bits = 0b01
        elif channel == "left":
            channel_bits = 0b10
        elif channel == "stereo":
            channel_bits = 0b11
        else:
            uvm_fatal(self.tag, "Please enter a valid channel config ('left', 'right' or 'stereo')")

        sign_extend_bit = random.choice([0,1]) if sign_extend is None else 0b1 if sign_extend else 0b0
        left_justify_bit = random.choice([0,1]) if left_justify is None else 0b1 if left_justify else 0b0
        if sample_size is None:
            sample_size = random.randint(1,33)
        config_reg =  (sample_size & 0b11111) << 4 | (left_justify_bit & 0b1) << 3 | (sign_extend_bit & 0b1) << 2 | (channel_bits & 0b11)
        return  config_reg

uvm_component_utils(i2s_base_test)


class i2s_left_channel_test(i2s_base_test):
    def __init__(self, name="i2s_left_channel_test", parent=None):
        super().__init__(name, parent=parent)
        self.tag = name

    # def build_phase(self, phase):
    #     super().build_phase(phase)
    #     self.config_reg = self.get_config_reg_val(channel="left", sign_extend= False, left_justify=True, sample_size=24)

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")

        bus_i2s_config_seq = i2s_config_seq("i2s_config_seq")
        ip_i2s_send_left_sample_seq = i2s_send_left_sample_seq("i2s_send_left_sample_seq")
        bus_i2s_read_rxdata_seq = i2s_read_rxdata_seq("i2s_read_rxdata_seq")
        bus_i2s_read_ris_seq = i2s_read_ris_seq("i2s_read_ris_seq")

        for _ in range (2):

            self.config_reg = self.get_config_reg_val(channel="left", sign_extend= False, left_justify=False, sample_size=24)
            bus_i2s_config_seq.set_config_reg(self.config_reg)
            await bus_i2s_config_seq.start(self.bus_sqr)

            for i in range (16):
                await ip_i2s_send_left_sample_seq.start(self.ip_sqr)


            for i in range (random.randint(1, 16)):
                await bus_i2s_read_rxdata_seq.start(self.bus_sqr)

            
            await Timer(10000 , "ns")
            
            

        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


uvm_component_utils(i2s_left_channel_test)



class i2s_right_channel_test(i2s_base_test):
    def __init__(self, name="i2s_right_channel_test", parent=None):
        super().__init__(name, parent=parent)
        self.tag = name

    # def build_phase(self, phase):
    #     super().build_phase(phase)
    #     self.config_reg = self.get_config_reg_val(channel="right", sign_extend= False, left_justify=True, sample_size=24)

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")

        bus_i2s_config_seq = i2s_config_seq("i2s_config_seq")
        ip_i2s_send_right_sample_seq = i2s_send_right_sample_seq("i2s_send_right_sample_seq")
        bus_i2s_read_rxdata_seq = i2s_read_rxdata_seq("i2s_read_rxdata_seq")
        bus_i2s_read_ris_seq = i2s_read_ris_seq("i2s_read_ris_seq")

        for _ in range (2):
            self.config_reg = self.get_config_reg_val(channel="left", sign_extend= True, left_justify=True, sample_size=24)
            bus_i2s_config_seq.set_config_reg(self.config_reg)
            await bus_i2s_config_seq.start(self.bus_sqr)

            for i in range (16):
                await ip_i2s_send_right_sample_seq.start(self.ip_sqr)
                
            for i in range (random.randint(1, 16)):
                await bus_i2s_read_rxdata_seq.start(self.bus_sqr)

            await Timer(10000 , "ns")

        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


uvm_component_utils(i2s_right_channel_test)


class i2s_stereo_test(i2s_base_test):
    def __init__(self, name="i2s__first_test", parent=None):
        super().__init__(name, parent=parent)
        self.tag = name

    def build_phase(self, phase):
        super().build_phase(phase)
        self.config_reg = self.get_config_reg_val(channel="stereo", sign_extend= False, left_justify=False, sample_size=24)
        

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")

        ip_i2s_send_left_sample_seq = i2s_send_left_sample_seq("i2s_send_left_sample_seq")
        ip_i2s_send_right_sample_seq = i2s_send_right_sample_seq("i2s_send_right_sample_seq")
        bus_i2s_read_rxdata_seq = i2s_read_rxdata_seq("i2s_read_rxdata_seq")
        bus_i2s_read_ris_seq = i2s_read_ris_seq("i2s_read_ris_seq")


        for i in range (8):
            await ip_i2s_send_left_sample_seq.start(self.ip_sqr)
            await ip_i2s_send_right_sample_seq.start(self.ip_sqr)


        for i in range (random.randint(1, 16)):
            await bus_i2s_read_rxdata_seq.start(self.bus_sqr)

        await Timer(10000 , "ns")

        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


uvm_component_utils(i2s_stereo_test)
