from uvm.seq.uvm_sequence_item import UVMSequenceItem
from uvm.macros import uvm_object_utils_begin, uvm_object_utils_end, uvm_field_int, uvm_object_utils, uvm_error, uvm_info
from uvm.base.uvm_object_globals import UVM_ALL_ON, UVM_NOPACK, UVM_HIGH, UVM_MEDIUM
from uvm.base.sv import sv
from EF_UVM.ip_env.ip_item import ip_item

class i2s_item(ip_item):
    def __init__(self, name="i2s_item"):
        super().__init__(name)
        self.sample = 0
        self.channel = "left"

    def convert2string(self):
        return sv.sformatf(f"I2S {self.channel} channel sample = 0x{self.sample:X} ")

    def do_compare(self, tr):
        uvm_info(self.tag, "Comparing " + self.convert2string() + " with " + tr.convert2string(), UVM_MEDIUM)
        return self.sample == tr.sample and self.channel == tr.channel 


uvm_object_utils(i2s_item)
