from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info, uvm_warning
from uvm.base.uvm_config_db import UVMConfigDb
from uvm.base.uvm_object_globals import UVM_HIGH, UVM_LOW, UVM_MEDIUM
from cocotb.triggers import Timer, ClockCycles, FallingEdge, Event, RisingEdge, First
import cocotb
import random
from EF_UVM.ip_env.ip_agent.ip_driver import ip_driver
from i2s_item.i2s_item import i2s_item


class i2s_driver(ip_driver):
    def __init__(self, name="i2s_driver", parent=None):
        super().__init__(name, parent)
        self.tag = name

    async def run_phase(self, phase):
        uvm_info(self.tag, "run_phase started", UVM_LOW)
        self.vif.sdi.value = 0
        while True:
            tr = []
            await self.seq_item_port.get_next_item(tr)
            tr = tr[0]
            uvm_info(self.tag, f"Received transaction {tr.convert2string()}" , UVM_LOW)
            sample_size = 32
            left_justified = self.is_left_justified() 
            if left_justified:
                if (tr.channel == "right"):
                    right_sample = tr.sample 
                    await FallingEdge(self.vif.ws)    
                    await Timer(1 , "ns") # delay to avoid shifting of bits after reset 
                    for i in range (sample_size-1, -1, -1):             # get MSB first 
                        self.vif.sdi.value = (right_sample >> i ) & 0b1
                        await FallingEdge(self.vif.sck)
                        uvm_info(self.tag, f" right: falling edge sck {i}= {(right_sample >> i ) & 0b1}", UVM_LOW)
                
                if (tr.channel == "left"): 
                    left_sample = tr.sample
                    await RisingEdge(self.vif.ws)   
                    await Timer(1 , "ns") # delay to avoid shifting of bits after reset 
                    for i in range (sample_size-1, -1, -1):             # get MSB first 
                        self.vif.sdi.value = (left_sample >> i ) & 0b1
                        await FallingEdge(self.vif.sck)
                        uvm_info(self.tag, f" left: falling edge sck {i} = {(left_sample >> i ) & 0b1}", UVM_LOW)
                        

            else: # i2s mode 
                if (tr.channel == "left"):
                    left_sample = tr.sample
                    await FallingEdge(self.vif.ws)                     # left sample driven in ws falling edge in i2s mode
                    await Timer(1 , "ns") # delay to avoid capturing sck with ws 
                    for i in range (sample_size-1, -1, -1):             # get MSB first 
                        await FallingEdge(self.vif.sck)
                        self.vif.sdi.value = (left_sample >> i ) & 0b1
                        uvm_info(self.tag, f"left channel i = {i} , sdi = {self.vif.sdi.value}", UVM_LOW)
                    
                elif (tr.channel == "right"):
                    right_sample = tr.sample
                    await RisingEdge(self.vif.ws)                     # right sample driven in ws rising edge in i2s mode 
                    await Timer(1 , "ns") # delay to avoid capturing sck with ws  
                    for i in range (sample_size-1, -1, -1):             # get MSB first 
                        await FallingEdge(self.vif.sck)
                        self.vif.sdi.value = (right_sample >> i ) & 0b1
                        uvm_info(self.tag, f"right channel i = {i} , sdi = {self.vif.sdi.value}", UVM_LOW)
                    
            self.seq_item_port.item_done()
    
    def get_sample_size(self):
        cfg_reg = self.regs.read_reg_value("CFG")
        uvm_info(self.tag, "Config Reg = " + str(cfg_reg), UVM_HIGH)
        sample_size = cfg_reg >> 4            # get sample size field
        uvm_info(self.tag, "Sample Size = " + str(sample_size), UVM_HIGH)
        return sample_size
    
    def is_left_justified(self):
        cfg_reg = self.regs.read_reg_value("CFG")
        uvm_info(self.tag, "Config Reg = " + str(cfg_reg), UVM_HIGH)
        left_justify = True if (cfg_reg >> 3) &0b1 else False            # get left justify bit
        uvm_info(self.tag, "Left justify = " + str(left_justify), UVM_HIGH)
        return left_justify

uvm_component_utils(i2s_driver)
