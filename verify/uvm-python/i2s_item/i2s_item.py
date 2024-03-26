from uvm.seq.uvm_sequence_item import UVMSequenceItem
from uvm.macros import uvm_object_utils_begin, uvm_object_utils_end, uvm_field_int, uvm_object_utils, uvm_error, uvm_info
from uvm.base.uvm_object_globals import UVM_ALL_ON, UVM_NOPACK, UVM_HIGH, UVM_MEDIUM
from uvm.base.sv import sv
from EF_UVM.ip_env.ip_item import ip_item

class i2s_item(ip_item):
    def __init__(self, name="i2s_item"):
        super().__init__(name)
        self.left_sample = 0
        self.right_sample = 0

    def convert2string(self):
        return sv.sformatf(f" I2S Left Sample = 0x{self.left_sample:X} , I2S Right Sample = 0x{self.right_sample:X} ")

    def do_compare(self, tr):
        uvm_info(self.tag, "Comparing " + self.convert2string() + " with " + tr.convert2string(), UVM_MEDIUM)
        return self.left_sample == tr.left_sample and self.right_sample == tr.right_sample 


uvm_object_utils(i2s_item)
