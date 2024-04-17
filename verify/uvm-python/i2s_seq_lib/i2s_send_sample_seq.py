from uvm.macros.uvm_object_defines import uvm_object_utils
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do
from uvm.base import sv, UVM_HIGH, UVM_LOW
from uvm.macros.uvm_message_defines import uvm_info, uvm_fatal
from i2s_item.i2s_item import i2s_item
from uvm.seq import UVMSequence
import random

class i2s_send_sample_seq(UVMSequence):
    # use this sequence write or read from register by the ip interface
    # this sequence should be connected to the ip sequencer in the testbench
    # you should add as many sequences as you need not only this one
    def __init__(self, name="i2s_send_sample_seq"):
        UVMSequence.__init__(self, name)
        self.set_automatic_phase_objection(1)
        self.req = i2s_item()
        self.rsp = i2s_item()
        self.tag = name

    async def body(self):
        # send item with conditions 
        # await uvm_do_with(self, self.req, lambda i2s_var1: i2s_var1 == 10, lambda i2s_var2: i2s_var2 > 7, ......)
        # send item without conditions
        self.req.left_sample = 0x80808080
        self.req.right_sample = 0x90909090
        # self.req.left_sample = random.randint(0x0, 0xFFFFFFFF)
        # self.req.right_sample = random.randint(0x0, 0xFFFFFFFF)
        await uvm_do(self, self.req)

uvm_object_utils(i2s_send_sample_seq)
