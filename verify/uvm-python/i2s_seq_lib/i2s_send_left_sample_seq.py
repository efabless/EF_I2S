from uvm.macros.uvm_object_defines import uvm_object_utils	
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do	
from uvm.base import sv, UVM_HIGH, UVM_LOW	
from uvm.macros.uvm_message_defines import uvm_info, uvm_fatal	
from i2s_item.i2s_item import i2s_item	
from uvm.seq import UVMSequence	


class i2s_send_left_sample_seq(UVMSequence):	

    def __init__(self, name="i2s_send_left_sample_seq"):	
        UVMSequence.__init__(self, name)	
        self.set_automatic_phase_objection(1)	
        self.req = i2s_item()	
        self.rsp = i2s_item()	
        self.tag = name	

    async def body(self):	
        self.req.channel = "left"	
        self.req.sample = 0x80808080	
        await uvm_do(self, self.req)	


uvm_object_utils(i2s_send_left_sample_seq)	