from uvm.seq import UVMSequence
from uvm.macros.uvm_object_defines import uvm_object_utils
from uvm.macros.uvm_message_defines import uvm_fatal
from EF_UVM.bus_env.bus_item import bus_item
from uvm.base.uvm_config_db import UVMConfigDb
from cocotb.triggers import Timer
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do
from EF_UVM.bus_env.bus_seq_lib.bus_seq_base import bus_seq_base
from i2s_item.i2s_item import i2s_item
import random


class i2s_write_avgth_seq(bus_seq_base):

    def __init__(self , name="i2s_write_avgth_seq"):
        super().__init__(name)
        self.threshold = 0

    async def body(self):
        # get register names/address conversion dict
        await super().body()
        # await self.send_req(is_write=True, reg="icr", data_condition=lambda data: data == self.ic ) # set interrupt mask
        await self.send_req(is_write=True, reg="AVGT"  ,data_value = self.threshold ) # set interrupt mask


    def set_average_threshold (self, threshold):
        self.threshold = threshold

uvm_object_utils(i2s_write_avgth_seq)