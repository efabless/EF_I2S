from uvm.macros.uvm_object_defines import uvm_object_utils	
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do	
from uvm.base import sv, UVM_HIGH, UVM_LOW	
from uvm.macros.uvm_message_defines import uvm_info, uvm_fatal	
from i2s_item.i2s_item import i2s_item	
from uvm.seq import UVMSequence	
import random


class i2s_send_left_sample_seq(UVMSequence):	

    def __init__(self, name="i2s_send_left_sample_seq"):	
        UVMSequence.__init__(self, name)	
        self.set_automatic_phase_objection(1)	
        self.req = i2s_item()	
        self.rsp = i2s_item()	
        self.tag = name	
        self.sample = None


    async def body(self):	
        self.req.channel = "left"	
        # self.req.sample = 0x80808080	
        # self.req.sample = self.get_random_sample()
        if self.sample is None:
            self.req.sample = random.randint(0x0, 0xFFFFFFFF)
            if (random.choice([0,1])):
                self.req.sample = 0xFFFFFFFF
        else:
             self.req.sample = self.sample
        await uvm_do(self, self.req)

    def set_sample(self, sample):
        self.sample = sample	
    
    # def get_random_sample(self):
    #     sample = 0
    #     for i in range(32):
    #         bit = random.choice([0,1])
    #         sample |= bit << i
    #     return(sample)


uvm_object_utils(i2s_send_left_sample_seq)	