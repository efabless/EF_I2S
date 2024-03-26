from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info, uvm_error, uvm_warning
from uvm.comps.uvm_monitor import UVMMonitor
from uvm.tlm1.uvm_analysis_port import UVMAnalysisPort
from uvm.base.uvm_config_db import UVMConfigDb
from cocotb.triggers import Timer, ClockCycles, FallingEdge, Event, RisingEdge, Combine, First
from uvm.base.uvm_object_globals import UVM_HIGH, UVM_LOW, UVM_MEDIUM
import cocotb
import math
from EF_UVM.ip_env.ip_agent.ip_monitor import ip_monitor
from i2s_item.i2s_item import i2s_item

class i2s_monitor(ip_monitor):
    def __init__(self, name="i2s_monitor", parent=None):
        super().__init__(name, parent)
        self.clk_freq = 0.0
        self.sck_freq = 0.0
        self.ws_freq = 0.0
        self.done_calculating_freq = Event()
        

    async def run_phase(self, phase):
        uvm_info(self.tag, "run_phase started", UVM_LOW)
        # await self.get_i2s_sample()
        await cocotb.start(self.get_i2s_sample())
        await cocotb.start(self.get_clk_freq())
        await cocotb.start(self.get_sck_freq())
        await cocotb.start(self.get_ws_freq())
        await cocotb.start(self.check_sample_rate())
        

    async def get_i2s_sample(self):
        await RisingEdge (self.vif.RESETn)
        while(True):
            left_sample = 0
            right_sample = 0
            tr = i2s_item.type_id.create("tr", self)
            await FallingEdge(self.vif.ws)    # At word select falling edge, left channel 
            # sample_size = self.get_sample_size()
            sample_size = 32
            for i in range (sample_size-1, -1, -1):
                await RisingEdge(self.vif.sck)
                await Timer(1 , "ns")           # small delay to capture changes made by driver 
                left_sample |= (self.vif.sdi.value << i )
                # uvm_info(self.tag, f"left channel i = {i} , sdi = {self.vif.sdi.value}", UVM_LOW)
            tr.left_sample = left_sample
            # tr.sample = left_sample
            # tr.channel = "left"

            # uvm_info(self.tag, "Sampled transaction " + tr.convert2string(), UVM_LOW)
            # # await FallingEdge(self.vif.ws) # just to sync the refrence model with the monitor
            # self.monitor_port.write(tr)

            await RisingEdge(self.vif.ws)    # At word select rising edge, right channel 
            for i in range (sample_size-1, -1, -1):
                await RisingEdge(self.vif.sck)
                await Timer(1 , "ns")           # small delay to capture changes made by driver 
                right_sample |= (self.vif.sdi.value << i )
            tr.right_sample = right_sample
            # tr.sample = right_sample
            # tr.channel = "right"

            uvm_info(self.tag, "Sampled transaction " + tr.convert2string(), UVM_LOW)
            # await FallingEdge(self.vif.ws) # just to sync the refrence model with the monitor
            self.monitor_port.write(tr)

    async def get_clk_freq(self):
        await RisingEdge(self.vif.CLK)
        time0 = cocotb.utils.get_sim_time(units="ns")
        await RisingEdge(self.vif.CLK)
        time1 = cocotb.utils.get_sim_time(units="ns")
        clk_period = time1 - time0
        self.clk_freq = 1/(clk_period/1000_000_000)
        uvm_info(self.tag, f"clk frequency = {self.clk_freq/1000_000} MHz", UVM_LOW)

    async def get_sck_freq(self):
        await RisingEdge(self.vif.sck)
        time0 = cocotb.utils.get_sim_time(units="ns")
        await RisingEdge(self.vif.sck)
        time1 = cocotb.utils.get_sim_time(units="ns")
        sck_period = time1 - time0
        self.sck_freq = 1/(sck_period/1000_000_000)
        uvm_info(self.tag, f"sck frequency = {self.sck_freq/1000_000} MHz", UVM_LOW)

    async def get_ws_freq(self):
        await FallingEdge(self.vif.ws)
        time0 = cocotb.utils.get_sim_time(units="ns")
        await FallingEdge(self.vif.ws)
        time1 = cocotb.utils.get_sim_time(units="ns")
        ws_period = time1 - time0
        self.ws_freq = 1/(ws_period/1000_000_000)
        uvm_info(self.tag, f"ws frequency = {self.ws_freq/1000_000} MHz", UVM_LOW)
        self.done_calculating_freq.set()
    
    async def check_sample_rate(self):
        await self.done_calculating_freq.wait()
        prescaler = self.get_prescaler()
        expected_sck_freq = round ((self.clk_freq / (prescaler+1))/2, 5)

        if round (self.sck_freq , 5) != expected_sck_freq:
            uvm_fatal(self.tag, f"sck frequency = {self.sck_freq/1000_000} MHz, expected sck frequency = {expected_sck_freq/1000_000} MHz")

        expected_ws_freq = round (expected_sck_freq / 64 , 5)
        if round (self.ws_freq, 5) != expected_ws_freq:
            uvm_fatal(self.tag, f"ws frequency = {self.ws_freq/1000_000} MHz, expected ws frequency = {expected_ws_freq/1000_000} MHz")

        self.done_calculating_freq.clear()
    
    # def get_sample_size(self):
    #     cfg_reg = self.regs.read_reg_value("CFG")
    #     uvm_info(self.tag, "Config Reg = " + str(cfg_reg), UVM_LOW)
    #     sample_size = (cfg_reg >> 4) & 0b11111            # get sample size field
    #     uvm_info(self.tag, "Sample Size = " + str(sample_size), UVM_LOW)
    #     return sample_size

    def get_prescaler(self):
        prescaler = self.regs.read_reg_value("PR")
        uvm_info(self.tag, "Prescaler = " + str(prescaler), UVM_LOW)
        return prescaler

uvm_component_utils(i2s_monitor)
