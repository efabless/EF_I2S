from uvm.seq import UVMSequence
from uvm.macros.uvm_object_defines import uvm_object_utils
from uvm.macros.uvm_message_defines import uvm_fatal
from uvm.base.uvm_config_db import UVMConfigDb
from EF_UVM.bus_env.bus_seq_lib.bus_seq_base import bus_seq_base
from cocotb.triggers import Timer
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do
import random


class i2s_read_ris_seq(bus_seq_base):
    # use this sequence write or read from register by the bus interface
    # this sequence should be connected to the bus sequencer in the testbench
    # you should create as many sequences as you need not only this one
    def __init__(self, name="i2s_read_ris_seq"):
        super().__init__(name)

    async def body(self):
        await super().body()
        # await Timer(1, "ns")
        # for _ in range(5):
        #     await self.send_nop()
        await self.send_req(is_write=False, reg="ris")

uvm_object_utils(i2s_read_ris_seq)