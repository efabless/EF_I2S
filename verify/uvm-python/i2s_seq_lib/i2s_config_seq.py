from uvm.seq import UVMSequence
from uvm.macros.uvm_object_defines import uvm_object_utils
from uvm.macros.uvm_message_defines import uvm_fatal
from uvm.base.uvm_config_db import UVMConfigDb
from EF_UVM.bus_env.bus_seq_lib.bus_seq_base import bus_seq_base
from cocotb.triggers import Timer
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do
import random
from EF_UVM.bus_env.bus_item import bus_item

class i2s_config_seq(bus_seq_base):
    # use this sequence write or read from register by the bus interface
    # this sequence should be connected to the bus sequencer in the testbench
    # you should create as many sequences as you need not only this one
    def __init__(self, name="i2s_config_seq", config_reg=0, ctrl_reg=0):
        super().__init__(name)
        self.config_reg = config_reg
        self.ctrl_reg = ctrl_reg
        self.req = bus_item()

    async def body(self):
        await super().body()
        # await self.send_req(is_write=True, reg="control", data_condition=lambda data: data > 5)
        # example for writing register by value == 5
        await self.send_reset()
        # enable gated clock
        await self.send_req(is_write=True, reg="CLKGATE", data_condition=lambda data: data == 1)
        await self.send_req(is_write=True, reg="PR", data_condition=lambda data: 2 <= data <= 50)
        await self.send_req(is_write=False, reg="PR")
        # config_reg = self.get_config_reg_val(channel="left", sign_extend=False, left_justify=True, sample_size=24)
        await self.send_req(is_write=True, reg="CFG", data_value=self.config_reg)
        await self.send_req(is_write=False, reg="CFG")
        await self.send_req(is_write=True, reg="CTRL", data_value=self.ctrl_reg) 
        await self.send_req(is_write=False, reg="CTRL")

    def set_config_reg(self, config_reg):
        self.config_reg = config_reg
    
    def set_ctrl_reg(self, ctrl_reg):
        self.ctrl_reg = ctrl_reg


uvm_object_utils(i2s_config_seq)
