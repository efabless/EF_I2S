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
from EF_UVM.bus_env.bus_seq_lib.write_read_regs import write_read_regs
from i2s_seq_lib.i2s_config_seq import i2s_config_seq
from i2s_seq_lib.i2s_send_right_sample_seq import i2s_send_right_sample_seq
from i2s_seq_lib.i2s_send_left_sample_seq import i2s_send_left_sample_seq
from i2s_seq_lib.i2s_read_rxdata_seq import i2s_read_rxdata_seq
from i2s_seq_lib.i2s_write_fifoth_seq import i2s_write_fifoth_seq
from i2s_seq_lib.i2s_write_avgth_seq import i2s_write_avgth_seq
from i2s_seq_lib.i2s_read_ris_seq import i2s_read_ris_seq
from i2s_seq_lib.i2s_write_im_seq import i2s_write_im_seq
from i2s_seq_lib.i2s_write_ic_seq import i2s_write_ic_seq
from i2s_seq_lib.i2s_read_mis_seq import i2s_read_mis_seq
from i2s_seq_lib.i2s_send_nop_seq import i2s_send_nop_seq
from i2s_seq_lib.i2s_read_fifo_level_seq import i2s_read_fifo_level_seq
from i2s_seq_lib.i2s_fifo_flush_seq import i2s_fifo_flush_seq

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
            sample_size = random.randint(1,32)
        config_reg =  (sample_size & 0b111111) << 4 | (left_justify_bit & 0b1) << 3 | (sign_extend_bit & 0b1) << 2 | (channel_bits & 0b11)
        return  config_reg

    async def delay(self, cycles=None):
        bus_i2s_send_nop_seq = i2s_send_nop_seq("i2s_send_nop_seq")
        if cycles is None:
            cycles = 1
        for _ in range(cycles):
            await bus_i2s_send_nop_seq.start(self.bus_sqr)

uvm_component_utils(i2s_base_test)


class i2s_left_channel_test(i2s_base_test):
    def __init__(self, name="i2s_left_channel_test", parent=None):
        super().__init__(name, parent=parent)
        self.tag = name

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")

        bus_i2s_config_seq = i2s_config_seq("i2s_config_seq")
        bus_i2s_config_seq.set_ctrl_reg(0b011)          # enable i2s and enable fifo 
        ip_i2s_send_left_sample_seq = i2s_send_left_sample_seq("i2s_send_left_sample_seq")
        bus_i2s_read_rxdata_seq = i2s_read_rxdata_seq("i2s_read_rxdata_seq")
        bus_i2s_read_fifo_level_seq = i2s_read_fifo_level_seq("i2s_read_fifo_level_seq")
        # bus_i2s_read_rxdata_seq.set_check_on_threshold(True)

        for _ in range (20):
            self.config_reg = self.get_config_reg_val(channel="left")   # left channel mode and random configuration for sign extension, left justified, and sign extension  
            bus_i2s_config_seq.set_config_reg(self.config_reg)
            await bus_i2s_config_seq.start(self.bus_sqr)

            for i in range (16):                                        # send samples until fifo is full 
                await ip_i2s_send_left_sample_seq.start(self.ip_sqr)


            for i in range (random.randint(1, 16)):                     # read a random number of samples 
                await bus_i2s_read_rxdata_seq.start(self.bus_sqr)
                # await bus_i2s_read_fifo_level_seq.start(self.bus_sqr)

            
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
        bus_i2s_config_seq.set_ctrl_reg(0b011)          # enable i2s and enable fifo 
        ip_i2s_send_right_sample_seq = i2s_send_right_sample_seq("i2s_send_right_sample_seq")
        bus_i2s_read_rxdata_seq = i2s_read_rxdata_seq("i2s_read_rxdata_seq")
        # bus_i2s_read_rxdata_seq.set_check_on_threshold(True)


        for _ in range (20):
            self.config_reg = self.get_config_reg_val(channel="right")      # right channel mode and random configuration for sign extension, left justified, and sign extension  
            bus_i2s_config_seq.set_config_reg(self.config_reg)
            await bus_i2s_config_seq.start(self.bus_sqr)

            for i in range (16):                                            # send samples until fifo is full 
                await ip_i2s_send_right_sample_seq.start(self.ip_sqr)
                
            for i in range (random.randint(1, 16)):                         # read a random number of samples 
                await bus_i2s_read_rxdata_seq.start(self.bus_sqr)

            await Timer(10000 , "ns")

        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


uvm_component_utils(i2s_right_channel_test)


class i2s_stereo_test(i2s_base_test):
    def __init__(self, name="i2s_stereo_test", parent=None):
        super().__init__(name, parent=parent)
        self.tag = name

    def build_phase(self, phase):
        super().build_phase(phase)
        
        

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")

        bus_i2s_config_seq = i2s_config_seq("i2s_config_seq")
        bus_i2s_config_seq.set_ctrl_reg(0b011)          # enable i2s and enable fifo 
        ip_i2s_send_left_sample_seq = i2s_send_left_sample_seq("i2s_send_left_sample_seq")
        ip_i2s_send_right_sample_seq = i2s_send_right_sample_seq("i2s_send_right_sample_seq")
        bus_i2s_read_rxdata_seq = i2s_read_rxdata_seq("i2s_read_rxdata_seq")
        # bus_i2s_read_rxdata_seq.set_check_on_threshold(True)
        

        for _ in range(20):
            self.config_reg = self.get_config_reg_val(channel="stereo")     # stereo  mode and random configuration for sign extension, left justified, and sign extension  
            bus_i2s_config_seq.set_config_reg(self.config_reg)
            await bus_i2s_config_seq.start(self.bus_sqr)

            for i in range (16):                                            # send samples until fifo is full 
                await ip_i2s_send_left_sample_seq.start(self.ip_sqr)
                await ip_i2s_send_right_sample_seq.start(self.ip_sqr)


            for i in range (random.randint(1, 16)):                         # read a random number of samples 
                await bus_i2s_read_rxdata_seq.start(self.bus_sqr)

            await Timer(10000 , "ns")

        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


uvm_component_utils(i2s_stereo_test)


class i2s_fifo_interrupts_test(i2s_base_test):
    def __init__(self, name="i2s_fifo_interrupts_test", parent=None):
        super().__init__(name, parent=parent)
        self.tag = name

    def build_phase(self, phase):
        super().build_phase(phase)
        

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")

        bus_i2s_config_seq = i2s_config_seq("i2s_config_seq")
        bus_i2s_config_seq.set_ctrl_reg(0b011)          # enable i2s and enable fifo 
        ip_i2s_send_left_sample_seq = i2s_send_left_sample_seq("i2s_send_left_sample_seq")
        bus_i2s_read_rxdata_seq = i2s_read_rxdata_seq("i2s_read_rxdata_seq")
        bus_i2s_write_im_seq = i2s_write_im_seq("i2s_write_im_seq")
        bus_i2s_write_ic_seq = i2s_write_ic_seq("i2s_write_ic_seq")
        bus_i2s_read_ris_seq = i2s_read_ris_seq("i2s_read_ris_seq")
        bus_i2s_read_mis_seq = i2s_read_mis_seq("i2s_read_mis_seq")
        bus_i2s_write_fifoth_seq = i2s_write_fifoth_seq("i2s_write_fifoth_seq")
        bus_i2s_send_nop_seq = i2s_send_nop_seq("i2s_send_nop_seq")

        
        for _ in range (10):
            self.config_reg = self.get_config_reg_val(channel="left") # random configuration 
            bus_i2s_config_seq.set_config_reg(self.config_reg)
            await bus_i2s_config_seq.start(self.bus_sqr)
            threshold = random.randint(1, 14)                       # set a random value for the fifo threshold (fifo level can not be greater than 15)
            bus_i2s_write_fifoth_seq.set_fifo_threshold(threshold)
            await bus_i2s_write_fifoth_seq.start(self.bus_sqr)      # write the fifo threshold register 

            #### FIFO empty irq 
            await bus_i2s_read_ris_seq.start(self.bus_sqr)  # fifo should be empty at first so irq 1 should be fired
            bus_i2s_write_im_seq.set_im(0b1)                # read ris to check that it has the correct value  
            await bus_i2s_write_im_seq.start(self.bus_sqr)  # mask the interrupt
            await bus_i2s_read_mis_seq.start(self.bus_sqr)  # read mis to check that it has the correct value

            for _ in range(2):
                await ip_i2s_send_left_sample_seq.start(self.ip_sqr)  # write something to fifo to make it non-empty

            self.delay(10)

            bus_i2s_write_ic_seq.set_ic(0b1)
            await bus_i2s_write_ic_seq.start(self.bus_sqr)  # clear the interrupt
            await bus_i2s_read_mis_seq.start(self.bus_sqr)  # reread mis to check that it was cleared 

            await Timer(1000 , "ns") # wait some time before reset

            #### FIFO level above threshold
            await bus_i2s_config_seq.start(self.bus_sqr)
            threshold = random.randint(1, 14)                       # set a random value for the fifo threshold (fifo level can not be greater than 15)
            bus_i2s_write_fifoth_seq.set_fifo_threshold(threshold)
            await bus_i2s_write_fifoth_seq.start(self.bus_sqr)      # write the fifo threshold register 
            
            for _ in range (threshold+1):
                await ip_i2s_send_left_sample_seq.start(self.ip_sqr)

            self.delay(10)
            await bus_i2s_read_ris_seq.start(self.bus_sqr) 
            self.delay(10)
            bus_i2s_write_im_seq.set_im(0b10)                # read ris to check that it has the correct value  
            await bus_i2s_write_im_seq.start(self.bus_sqr)  # mask the interrupt
            self.delay(20)
            await bus_i2s_read_mis_seq.start(self.bus_sqr)  # read mis to check that it has the correct value

            for _ in range(2):
                await bus_i2s_read_rxdata_seq.start(self.bus_sqr) # read from fifo for the level to be below threshold 

            self.delay(10)
            bus_i2s_write_ic_seq.set_ic(0b10)
            await bus_i2s_write_ic_seq.start(self.bus_sqr)  # clear the interrupt
            await bus_i2s_read_mis_seq.start(self.bus_sqr)  # reread mis to check that it was cleared 

            await Timer(1000 , "ns") # wait some time before reset

            ##### FIFO is full
            await bus_i2s_config_seq.start(self.bus_sqr)
            for _ in range (18):                                
                await ip_i2s_send_left_sample_seq.start(self.ip_sqr)

            self.delay(10)
            await bus_i2s_read_ris_seq.start(self.bus_sqr)  # fifo should be empty at first so irq 1 should be fired
            self.delay(10)
            bus_i2s_write_im_seq.set_im(0b100)               # read ris to check that it has the correct value  
            await bus_i2s_write_im_seq.start(self.bus_sqr)  # mask the interrupt
            self.delay(10)
            await bus_i2s_read_mis_seq.start(self.bus_sqr)  # read mis to check that it has the correct value

            for _ in range(2):
                await bus_i2s_read_rxdata_seq.start(self.bus_sqr) # read from fifo for the level to be below threshold 

            self.delay(10)

            bus_i2s_write_ic_seq.set_ic(0b100)
            await bus_i2s_write_ic_seq.start(self.bus_sqr)  # clear the interrupt
            await bus_i2s_read_mis_seq.start(self.bus_sqr)  # reread mis to check that it was cleared 
            
            await Timer(1000 , "ns") # wait some time before reset


        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


uvm_component_utils(i2s_fifo_interrupts_test)


class i2s_averaging_test(i2s_base_test):
    def __init__(self, name="i2s_averaging_test", parent=None):
        super().__init__(name, parent=parent)
        self.tag = name

    def build_phase(self, phase):
        super().build_phase(phase)
        

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")

        bus_i2s_config_seq = i2s_config_seq("i2s_config_seq")
        bus_i2s_config_seq.set_ctrl_reg(0b101)          # enable i2s and enable averaging  
        ip_i2s_send_right_sample_seq = i2s_send_right_sample_seq("i2s_send_right_sample_seq")
        ip_i2s_send_left_sample_seq = i2s_send_left_sample_seq("i2s_send_left_sample_seq")
        bus_i2s_read_rxdata_seq = i2s_read_rxdata_seq("i2s_read_rxdata_seq")
        bus_i2s_write_im_seq = i2s_write_im_seq("i2s_write_im_seq")
        bus_i2s_write_ic_seq = i2s_write_ic_seq("i2s_write_ic_seq")
        bus_i2s_read_ris_seq = i2s_read_ris_seq("i2s_read_ris_seq")
        bus_i2s_read_mis_seq = i2s_read_mis_seq("i2s_read_mis_seq")
        bus_i2s_write_avgth_seq = i2s_write_avgth_seq("i2s_write_avgth_seq")
        bus_i2s_send_nop_seq = i2s_send_nop_seq("i2s_send_nop_seq")

        
        self.config_reg = self.get_config_reg_val(channel="right", sample_size=24, sign_extend=True) # put sample size to predict average 
        bus_i2s_config_seq.set_config_reg(self.config_reg)
        await bus_i2s_config_seq.start(self.bus_sqr)

        samples_list = []
        samples_sum = 0
        for i in range (32):
            sample = random.randint(0x0, 0xFFFFFFFF)
            samples_list.append(sample)

        samples_expected_average = self.get_expected_avg_threshold(samples_list, 24)
        
        bus_i2s_write_avgth_seq.set_average_threshold(samples_expected_average-1)
        await bus_i2s_write_avgth_seq.start(self.bus_sqr)      # write the fifo threshold register 

        
        for i in range (32):
            ip_i2s_send_right_sample_seq.set_sample(samples_list[i])
            await ip_i2s_send_right_sample_seq.start(self.ip_sqr)
        
        for _ in range(10):
            await bus_i2s_send_nop_seq.start(self.bus_sqr)

        await bus_i2s_read_ris_seq.start(self.bus_sqr)  # fifo should be empty at first so irq 1 should be fired
        bus_i2s_write_im_seq.set_im(0b1000)                # read ris to check that it has the correct value  
        await bus_i2s_write_im_seq.start(self.bus_sqr)  # mask the interrupt
        await bus_i2s_read_mis_seq.start(self.bus_sqr)  # read mis to check that it has the correct value

        for _ in range (2):
            await ip_i2s_send_right_sample_seq.start(self.ip_sqr)
        
        bus_i2s_write_ic_seq.set_ic(0b1000)
        await bus_i2s_write_ic_seq.start(self.bus_sqr)  # clear the interrupt
        await bus_i2s_read_mis_seq.start(self.bus_sqr)  # reread mis to check that it was cleared 

        await Timer(10000 , "ns")

        # ##################################################################################################################

        self.config_reg = self.get_config_reg_val(channel="left", sample_size=16, sign_extend=True) # put sample size to predict average 
        bus_i2s_config_seq.set_config_reg(self.config_reg)
        await bus_i2s_config_seq.start(self.bus_sqr)

        samples_list = []
        samples_sum = 0
        for i in range (32):
            sample = random.randint(0x0, 0xFFFFFFFF)
            samples_list.append(sample)

        samples_expected_average = self.get_expected_avg_threshold(samples_list, 16)
        

        bus_i2s_write_avgth_seq.set_average_threshold(samples_expected_average-1)
        await bus_i2s_write_avgth_seq.start(self.bus_sqr)      # write the fifo threshold register 

        
        for i in range (32):
            ip_i2s_send_left_sample_seq.set_sample(samples_list[i])
            await ip_i2s_send_left_sample_seq.start(self.ip_sqr)
        
        for _ in range(10):
            await bus_i2s_send_nop_seq.start(self.bus_sqr)

        await bus_i2s_read_ris_seq.start(self.bus_sqr)  # fifo should be empty at first so irq 1 should be fired
        bus_i2s_write_im_seq.set_im(0b1000)                # read ris to check that it has the correct value  
        await bus_i2s_write_im_seq.start(self.bus_sqr)  # mask the interrupt
        await bus_i2s_read_mis_seq.start(self.bus_sqr)  # read mis to check that it has the correct value

        for _ in range (2):
            await ip_i2s_send_right_sample_seq.start(self.ip_sqr)
        
        bus_i2s_write_ic_seq.set_ic(0b1000)
        await bus_i2s_write_ic_seq.start(self.bus_sqr)  # clear the interrupt
        await bus_i2s_read_mis_seq.start(self.bus_sqr)  # reread mis to check that it was cleared 

        await Timer(10000 , "ns")

        ######################################################################################################################

        self.config_reg = self.get_config_reg_val(channel="stereo", sample_size=8, sign_extend=True) # put sample size to predict average 
        bus_i2s_config_seq.set_config_reg(self.config_reg)
        await bus_i2s_config_seq.start(self.bus_sqr)

        samples_list = []
        samples_sum = 0
        for i in range (32):
            sample = random.randint(0x0, 0xFFFFFFFF)
            samples_list.append(sample)

        samples_expected_average = self.get_expected_avg_threshold(samples_list, 8)
        
        bus_i2s_write_avgth_seq.set_average_threshold(samples_expected_average-1)
        await bus_i2s_write_avgth_seq.start(self.bus_sqr)      # write the fifo threshold register 
        
        for i in range (0,32,2):
            ip_i2s_send_left_sample_seq.set_sample(samples_list[i])
            await ip_i2s_send_left_sample_seq.start(self.ip_sqr)
            ip_i2s_send_right_sample_seq.set_sample(samples_list[i+1])
            await ip_i2s_send_right_sample_seq.start(self.ip_sqr)
        
        for _ in range(10):
            await bus_i2s_send_nop_seq.start(self.bus_sqr)

        await bus_i2s_read_ris_seq.start(self.bus_sqr)  # fifo should be empty at first so irq 1 should be fired
        bus_i2s_write_im_seq.set_im(0b1000)                # read ris to check that it has the correct value  
        await bus_i2s_write_im_seq.start(self.bus_sqr)  # mask the interrupt
        await bus_i2s_read_mis_seq.start(self.bus_sqr)  # read mis to check that it has the correct value

        # for _ in range (2):
        await ip_i2s_send_left_sample_seq.start(self.ip_sqr)
        await ip_i2s_send_right_sample_seq.start(self.ip_sqr)
        
        bus_i2s_write_ic_seq.set_ic(0b1000)
        await bus_i2s_write_ic_seq.start(self.bus_sqr)  # clear the interrupt
        await bus_i2s_read_mis_seq.start(self.bus_sqr)  # reread mis to check that it was cleared 

        await Timer(10000 , "ns")



        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


    def get_expected_avg_threshold(self, samples_list, sample_size):
        samples_sum = 0 
        for sample in samples_list:
            sample = sample >> (32 - sample_size)
            sign_bit = (sample >> (sample_size-1)) & 0b1
            if (sign_bit):
                sign_extension = (0xFFFFFFFF << sample_size) & 0xFFFFFFFF
                sample = sample | sign_extension
            sample_absolute = sample if not sign_bit else (~sample  & 0xFFFFFFFF)  #one's complement to get the absolute value of the sample
            samples_sum += sample_absolute
        
        samples_sum &= 0xFFFFFFFF
        samples_average = int (samples_sum/32)
        uvm_info(self.tag, f"In tests samples sum  = 0x{samples_sum:X} and samples average = 0x{samples_average:X}", UVM_LOW)
        return(samples_average)


uvm_component_utils(i2s_averaging_test)


class WriteReadRegsTest(i2s_base_test):
    def __init__(self, name="WriteReadRegsTest", parent=None):
        super().__init__(name, parent)
        self.tag = name

    async def main_phase(self, phase):
        uvm_info(self.tag, f"Starting test {self.__class__.__name__}", UVM_LOW)
        phase.raise_objection(self, f"{self.__class__.__name__} OBJECTED")
        bus_seq = write_read_regs()
        await bus_seq.start(self.bus_sqr)
        phase.drop_objection(self, f"{self.__class__.__name__} drop objection")


uvm_component_utils(WriteReadRegsTest)