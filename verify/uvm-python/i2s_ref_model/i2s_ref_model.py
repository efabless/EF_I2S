from uvm.base.uvm_component import UVMComponent
from uvm.macros import uvm_component_utils
from uvm.tlm1.uvm_analysis_port import UVMAnalysisImp
from uvm.base.uvm_object_globals import UVM_HIGH, UVM_LOW, UVM_MEDIUM 
from uvm.macros import uvm_component_utils, uvm_fatal, uvm_info, uvm_warning
from uvm.base.uvm_config_db import UVMConfigDb
from uvm.tlm1.uvm_analysis_port import UVMAnalysisExport
import cocotb
from cocotb.triggers import Event
from cocotb.queue import Queue
import asyncio
from EF_UVM.ref_model.ref_model import ref_model
from EF_UVM.bus_env.bus_item import bus_item
from i2s_item.i2s_item import i2s_item
from EF_UVM.bus_env.bus_item import bus_item, bus_irq_item


class i2s_ref_model(ref_model):
    """
    The reference model is a crucial element within the top-level verification environment, designed to validate the functionality and performance of both the IP (Intellectual Property) and the bus system. Its primary role is to act as a representative or mimic of the actual hardware components, including the IP and the bus. Key features and functions of the reference model include:
    1) Input Simulation: The reference model is capable of receiving the same inputs that would be provided to the actual IP and bus via connection with the monitors of the bus and IP.
    2) Functional Emulation: It emulates the behavior and responses of the IP and bus under test. By replicating the operational characteristics of these components, the reference model serves as a benchmark for expected performance and behavior.
    3) Output Generation: Upon receiving inputs, the reference model processes them in a manner akin to the real hardware, subsequently generating expected outputs. These outputs are essential for comparison in the verification process.
    4) Interface with Scoreboard: The outputs from the reference model, representing the expected results, are forwarded to the scoreboard. The scoreboard then compares these expected results with the actual outputs from the IP and bus for verification.
    5)Register Abstraction Layer (RAL) Integration: The reference model includes a RAL model that mirrors the register values of the RTL, ensuring synchronization between expected and actual register states. This model facilitates register-level tests and error detection, offering accessible and up-to-date register values for other verification components. It enhances the automation and coverage of register testing, playing a vital role in ensuring the accuracy and comprehensiveness of the verification process.
    """
    def __init__(self, name="i2s_ref_model", parent=None):
        super().__init__(name, parent)
        self.tag = name
        self.stereo_channel=""
        self.first = True
        self.fifo_rx = Queue(maxsize=16)
        self.channels = 0b00
        self.left_justified = True
        self.samples_count = 0
        self.samples_sum = 0
        self.ris_reg = 0b0001            # FIFO is always empty at first so set ris flag 0 = 1
        self.mis_reg = 0
        self.irq = 0
        self.mis_changed = Event()
        self.icr_changed = Event()
        

    def build_phase(self, phase):
        super().build_phase(phase)
        # Here adding any initialize for user classes for the model

    
    async def run_phase(self, phase):
        await super().run_phase(phase)
        uvm_info(self.tag, "run phase started", UVM_HIGH)
        await cocotb.start (self.send_irq_tr())
        await cocotb.start (self.clear_ris_reg())

    def write_bus(self, tr):
        self.update_interrupt_regs()
        # Called when new transaction is received from the bus monitor
        uvm_info(self.tag, " Ref model received from bus monitor: " + tr.convert2string(), UVM_LOW)
        if tr.kind == bus_item.RESET:
            self.bus_bus_export.write(tr)
            uvm_info("Ref model", "reset from ref model", UVM_HIGH)
            self.reset_ref_model()
            return
        if tr.kind == bus_item.WRITE:
            self.regs.write_reg_value(tr.addr, tr.data, force_write=True)
            uvm_info(self.tag, f"Writing to register 0x{tr.addr:x} {tr.data}", UVM_LOW)
            if tr.addr == self.regs.reg_name_to_address["CFG"]:
                self.channels = self.regs.read_reg_value("CFG") & 0b11
                self.left_justified = True if (self.regs.read_reg_value("CFG") >> 3) & 0b1 else False
                self.avg_samples_size = 512 if self.regs.read_reg_value("CFG") & 0b1000000000 else 256
                self.zcr_samples_size = 512 if self.regs.read_reg_value("CFG") & 0b10000000000 else 256
            if tr.addr == self.regs.reg_name_to_address["icr"] and tr.data != 0:
                self.icr_changed.set()
            if tr.addr == self.regs.reg_name_to_address["RX_FIFO_FLUSH"] and tr.data != 0:
                while not self.fifo_rx.empty():    # flush the fifo 
                    _ = self.fifo_rx.get_nowait()  
                # self.regs.write_reg_value("RX_FIFO_FLUSH", 0 ,force_write=True)
            self.bus_bus_export.write(tr)
        elif tr.kind == bus_item.READ:
            data = self.read_register(tr.addr)
            td = tr.do_clone()
            td.data = data
            self.bus_bus_export.write(td)

    def write_ip(self, tr):
        # Called when new transaction is received from the ip monitor
        uvm_info(self.tag, "Ref model received from ip monitor: " + tr.convert2string(), UVM_HIGH)  
        self.update_registers(tr)
        self.set_ris_reg()
        self.update_interrupt_regs()
        self.ip_export.write(tr)  # Write the same ip transaction just for scoreboard purpose (verification is done through reading registers)

    def reset_ref_model(self):
        uvm_info(self.tag, "ref model is resetting", UVM_LOW)
        self.first = True
        self.channels = 0b00
        self.left_justified = True
        self.samples_count = 0
        self.samples_sum = 0
        self.avg_samples_size = 256
        self.zcr_samples_size = 256
        self.ris_reg = 0b0001            # FIFO is always empty at first so set ris flag 0 = 1
        self.mis_reg = 0
        self.irq = 0
        while not self.fifo_rx.empty():
            _ = self.fifo_rx.get_nowait()  # Discard the retrieved value
        
        self.regs.write_reg_value("RXDATA", 0, force_write=True)  # clear icr register
        self.regs.write_reg_value("PR", 0, force_write=True)  # clear icr register
        self.regs.write_reg_value("RX_FIFO_LEVEL", 0, force_write=True)  # clear icr register
        self.regs.write_reg_value("AVGT", 0, force_write=True)  # clear icr register
        self.regs.write_reg_value("CTRL", 0, force_write=True)  # clear icr register
        self.regs.write_reg_value("CFG", 0x308, force_write=True)  # clear icr register
        self.regs.write_reg_value("ris", 0, force_write=True)  # clear icr register
        self.regs.write_reg_value("mis", 0, force_write=True)  # clear icr register
        self.regs.write_reg_value("icr", 0, force_write=True)  # clear icr register
        self.regs.write_reg_value("im", 0, force_write=True)  # clear icr register


    def update_registers(self, tr):
        td = i2s_item.type_id.create("td", self)
        enable =  True if self.regs.read_reg_value("CTRL") & 0b1 else False
        fifo_enable =  True if (self.regs.read_reg_value("CTRL") >> 1)&0b1 else False
        averaging_enable =  True if (self.regs.read_reg_value("CTRL") >> 2)&0b1 else False
        prescaler = self.regs.read_reg_value("PR")
        self.channels = self.regs.read_reg_value("CFG") & 0b11
        sign_extend = True if (self.regs.read_reg_value("CFG") >> 2) & 0b1 else False
        self.left_justified = True if (self.regs.read_reg_value("CFG") >> 3) & 0b1 else False
        sample_size = (self.regs.read_reg_value("CFG") >> 4) & 0b111111

        sample = tr.sample

        # if not self.left_justified:
        #     left_sample = left_sample << 1
        #     right_sample = right_sample << 1
        if sample_size <= 32:
            sample = sample >> (32 - sample_size)

        uvm_info(self.tag, f"sample after adjusting size = 0x{sample:X}", UVM_LOW)
        
        if sample_size >= 1:
            sign_bit = (sample >> (sample_size-1)) & 0b1
        else:
            sign_bit = 0
        if sign_extend:
            if (sign_bit):
                # sign_extension = (((1 << sample_size) - 1) << sample_size) & 0xFFFFFFFF
                # sign_extension = (1 << (32 - sample_size)) - 1
                sign_extension = (0xFFFFFFFF << sample_size) & 0xFFFFFFFF
                uvm_info(self.tag, f"sign extension = 0x{sign_extension:X}", UVM_LOW)  
                sample = sample | sign_extension
        uvm_info(self.tag, f"sample after sign extension = 0x{sample:X}", UVM_LOW)
        sample_absolute = sample if not sign_bit else (~sample  & 0xFFFFFFFF)  #one's complement to get the absolute value of the samples
        uvm_info (self.tag, f"sample after absolute value = 0x{sample_absolute:X}", UVM_MEDIUM)

        if self.samples_count == self.avg_samples_size:   # reset counter and samples sum when 512 or 256 samples are read 
            self.samples_count = 0
            self.samples_sum = sample_absolute 
        else:
            if (self.channels == 0b01 and tr.channel == "right") or (self.channels == 0b10 and tr.channel == "left") or (self.channels == 0b11):
                self.samples_sum += sample_absolute # otherwise, calculate sum and increment counter 
                self.samples_sum &= 0xFFFFFFFF # make sure it's 32 bits
                uvm_info(self.tag, f"sample number {self.samples_count} samples sum = 0x{self.samples_sum:X}", UVM_LOW)
                self.samples_count += 1

        if self.first:
            if self.left_justified:
                self.stereo_channel = "right"
            else:
                self.stereo_channel= "left"
            self.first = False
        if enable and fifo_enable:
            if self.channels == 0b01 and tr.channel == "right":         # right
                self.write_to_FIFO(sample)
            elif self.channels == 0b10 and tr.channel == "left":      # left 
                self.write_to_FIFO(sample)
            elif self.channels == 0b11:      # stereo
                if self.left_justified:
                    if self.stereo_channel == "right":
                        self.write_to_FIFO(sample)
                        self.stereo_channel = "left"
                    else:
                        self.write_to_FIFO(sample)
                        self.stereo_channel = "right"
                else:
                    if self.stereo_channel == "left":
                        self.write_to_FIFO(sample)
                        self.stereo_channel = "right"
                    else:
                        self.write_to_FIFO(sample)
                        self.stereo_channel = "left"
        elif not enable:
            uvm_warning(self.tag, "received transaction while i2s is disabled")


    

    def read_register(self, addr):
        uvm_info(self.tag, f"Reading register  {hex(addr)} = {hex(self.regs.read_reg_value(addr))}" , UVM_MEDIUM)
        if addr == self.regs.reg_name_to_address["RXDATA"]:  # reading from rx data
            try:
                uvm_info(self.tag, f"Reading from rx fifo size = {self.fifo_rx.qsize()} {self.fifo_rx._queue}", UVM_LOW)
                data = self.fifo_rx.get_nowait()
                fifo_level = 0 if self.fifo_rx.qsize() == 16 else self.fifo_rx.qsize()
                self.regs.write_reg_value("RX_FIFO_LEVEL", fifo_level, force_write=True)
                if self.fifo_rx.empty():               # set empty flag if fifo is empty
                    self.ris_reg |= 0x1
                return data
            except asyncio.QueueEmpty:
                return "X" # x means the data is trash so the scoreboard should not check it
        return self.regs.read_reg_value(addr)


    def write_to_FIFO(self, data):
        try:
            self.fifo_rx.put_nowait(data)
            uvm_info(self.tag, f"Writing to fifo 0x{data:X} , fifo size = {self.fifo_rx.qsize()}", UVM_MEDIUM)
            fifo_level = 0 if self.fifo_rx.qsize() == 16 else self.fifo_rx.qsize()
            self.regs.write_reg_value("RX_FIFO_LEVEL", fifo_level, force_write=True)
        except asyncio.QueueFull:
            uvm_warning(self.tag, "writing to rx while fifo is full so ignore the value")


    def set_ris_reg(self):                  
        rx_fifo_threshold = self.regs.read_reg_value("RX_FIFO_THRESHOLD")
        avg_enable = (self.regs.read_reg_value("CTRL") & 0b100) >> 2
        avg_threshold = self.regs.read_reg_value("AVGT")

        if self.fifo_rx.empty():
            self.ris_reg |= 0x1

        if self.fifo_rx.qsize() > rx_fifo_threshold:
            self.ris_reg |= 0x2
            uvm_info (self.tag, f"RX FIFO level is above threshold", UVM_MEDIUM)

        if self.fifo_rx.qsize() >= 16: 
            self.ris_reg |= 0x4
            uvm_info (self.tag, f"RX FIFO is full", UVM_MEDIUM)

        if avg_enable:
            samples_average = int (self.samples_sum / self.avg_samples_size)
            uvm_info(self.tag, f"samples average = 0x{samples_average:X}", UVM_LOW)

            if samples_average > avg_threshold:
                self.ris_reg |= 0x9
    
    async def clear_ris_reg (self):
        while (True):
            await self.icr_changed.wait()
            icr_reg = self.regs.read_reg_value("icr")
            mask = ~icr_reg
            self.ris_reg = self.ris_reg & mask
            self.update_interrupt_regs()
            self.regs.write_reg_value("icr", 0, force_write=True)  # clear icr register
            self.icr_changed.clear()
    
    def update_interrupt_regs(self):
        self.regs.write_reg_value_after("ris", self.ris_reg, force_write=True, cycles=2)
        im_reg = self.regs.read_reg_value("im")
        mis_reg_new = self.ris_reg & im_reg
        uvm_info(self.tag, f" Update interrupts :  im =  {im_reg:X}, ris =  {self.ris_reg:X}, mis = {mis_reg_new:X}", UVM_LOW)
        if mis_reg_new != self.mis_reg:
            self.mis_changed.set()
        self.mis_reg = mis_reg_new
        self.regs.write_reg_value("mis", self.mis_reg, force_write=True)

    async def send_irq_tr(self):
        while (True):
            await self.mis_changed.wait()
            uvm_info (self.tag, "mis changed event", UVM_LOW)
            irq_new = 1 if self.mis_reg else 0                                        
            if irq_new and not self.irq: # irq changed from low to high 
                self.irq = 1 
                tr = bus_irq_item.type_id.create("tr", self)
                tr.trg_irq = 1     
                uvm_info (self.tag, f"sending irq tr {tr}", UVM_LOW)   
                self.bus_irq_export.write(tr)
            elif not irq_new and self.irq: # irq changed from high to low 
                self.irq = 0
                tr = bus_irq_item.type_id.create("tr", self)
                tr.trg_irq = 0
                uvm_info (self.tag, f"sending irq tr {tr}", UVM_LOW)   
                self.bus_irq_export.write(tr)
            
            self.mis_changed.clear()


uvm_component_utils(i2s_ref_model)
