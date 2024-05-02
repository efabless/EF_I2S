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


class i2s_read_fifo_level_seq(bus_seq_base):

    def __init__(self , name="i2s_read_fifo_level_seq"):
        super().__init__(name)


    async def body(self):
        await super().body()
        await self.send_req(is_write=False, reg="RX_FIFO_LEVEL") # set interrupt mask


uvm_object_utils(i2s_read_fifo_level_seq)