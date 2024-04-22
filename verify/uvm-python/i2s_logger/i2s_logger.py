from EF_UVM.ip_env.ip_logger.ip_logger import ip_logger
import cocotb 
from uvm.macros import uvm_component_utils, uvm_fatal


class i2s_logger(ip_logger):
    def __init__(self, name="i2s_logger", parent=None):
        super().__init__(name, parent)
        self.header = ['Time (ns)', "Channel", "Sample"]
        self.col_widths = [10]* len(self.header)

    def logger_formatter(self, transaction):
        sim_time = f"{cocotb.utils.get_sim_time(units='ns')} ns"
        sample = f"{transaction.sample} ({hex(transaction.sample)})"
        channel = f"{transaction.channel}"
        return [sim_time, channel, sample]


uvm_component_utils(i2s_logger)
