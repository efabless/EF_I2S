from uvm.seq import UVMSequence
from uvm.macros.uvm_object_defines import uvm_object_utils
from uvm.macros.uvm_message_defines import uvm_fatal, uvm_info
from uvm.base.uvm_config_db import UVMConfigDb
from EF_UVM.bus_env.bus_seq_lib.bus_seq_base import bus_seq_base
from cocotb.triggers import Timer
from uvm.macros.uvm_sequence_defines import uvm_do_with, uvm_do
import random
from uvm.base.uvm_object_globals import UVM_LOW


class i2s_read_rxdata_seq(bus_seq_base):
    # use this sequence write or read from register by the bus interface
    # this sequence should be connected to the bus sequencer in the testbench
    # you should create as many sequences as you need not only this one
    def __init__(self, name="i2s_read_rxdata_seq"):
        super().__init__(name)
        self.check_on_threshold = False
        regs_arr = []
        if not UVMConfigDb.get(self, "", "bus_regs", regs_arr):
            uvm_fatal(self.tag, "No json file wrapper regs")
        else:
            self.regs = regs_arr[0]

    async def body(self):
        await super().body()
        if self.check_on_threshold:
            while True:
                rsp = []
                await self.send_req(is_write=False, reg="ris")
                await self.get_response(rsp)
                ris_reg = rsp[0]
                uvm_info(self.tag, f"RIS value = {ris_reg}", UVM_LOW)
                if (
                    ris_reg.data & 0b010 == 0b010
                    and ris_reg.addr == self.regs.reg_name_to_address["ris"]
                ):
                    break
        # uvm_info(self.tag, f"RSP value = {self.rsp.convert2string()}", UVM_LOW)
        uvm_info(self.tag, "before sending read rxdata sequence", UVM_LOW)
        await self.send_req(is_write=False, reg="RXDATA")

    def set_check_on_threshold(self, flag):
        self.check_on_threshold = flag


uvm_object_utils(i2s_read_rxdata_seq)
