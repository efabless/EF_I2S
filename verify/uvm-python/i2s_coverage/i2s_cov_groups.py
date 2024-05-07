from uvm.macros.uvm_message_defines import uvm_info
from uvm.base.uvm_object_globals import UVM_HIGH, UVM_LOW
from cocotb_coverage.coverage import CoverPoint, CoverCross
from uvm.macros import uvm_component_utils
from i2s_item.i2s_item import i2s_item


class i2s_cov_groups():
    def __init__(self, hierarchy, regs) -> None:
        self.hierarchy = hierarchy
        self.regs = regs
        self.samples_coverage = self.samples_cov()
        self.ip_cov(None, do_sampling=False)


    def ip_cov(self, tr, do_sampling=True):
        @self.apply_decorators(decorators=self.samples_coverage)
        @CoverPoint(
            f"{self.hierarchy}.Left Channel.Prescaler",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b10, self.regs.read_reg_value("PR")),
            bins=[( True, i*10 , ((i+1)*10)-1 ) for i in range(5)],
            bins_labels=[(i*10 , ((i+1)*10)-1) for i in range(5)],
            rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        @CoverPoint(
            f"{self.hierarchy}.Left Channel.Sample Size",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b10, (self.regs.read_reg_value("CFG")>>4)&0b111111),
            bins=[( True, (i*8)+1 , ((i+1)*8) ) for i in range(4)],
            bins_labels=[((i*8)+1 , ((i+1)*8)) for i in range(4)],
            rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        @CoverPoint(
            f"{self.hierarchy}.Left Channel.Sign extended",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b10, (self.regs.read_reg_value("CFG")>>2)&0b1),
            bins=[( True, True ), (True, False) ],
            bins_labels=["sign extended", "not sign extended"],
            # rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        @CoverPoint(
            f"{self.hierarchy}.Left Channel.Left Justified",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b10, (self.regs.read_reg_value("CFG")>>3)&0b1),
            bins=[( True, True ), (True, False) ],
            bins_labels=["left justified", "not left justified"],
            # rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        # @CoverPoint(
        #     f"{self.hierarchy}.Left Channel.Received Data",
        #     xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b10 , tr.sample),
        #     bins=[(True, 1 << i, (1 << i + 1) - 1) if i != 0 else (True, 0, 1) for i in range(32)],
        #     bins_labels=[f"from {hex(1 << i)} to {hex((1 << i + 1) - 1)}" if i != 0 else f"from {hex(0)} to {hex(1)}" for i in range(32)],
        #     rel=lambda val, b:  (val[0] == b[0]) and  (b[1] <= val[1] <= b[2])
        # )
        # @CoverPoint(
        #     f"{self.hierarchy}.Left Channel.Received Data",
        #     xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b10 , tr.sample),
        #     bins=[(True, i)  for i in range(32)],
        #     bins_labels=[f"bit {i} = 1" for i in range(32)],
        #     rel=lambda val, b:  (val[0] == b[0]) and  ((val[1]>>b[1])&0b1) == 1  
        # )

        @CoverPoint(
            f"{self.hierarchy}.Right Channel.Prescaler",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b01, self.regs.read_reg_value("PR")),
            bins=[( True, i*10 , ((i+1)*10)-1 ) for i in range(5)],
            bins_labels=[(i*10 , ((i+1)*10)-1) for i in range(5)],
            rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        @CoverPoint(
            f"{self.hierarchy}.Right Channel.Sample Size",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b01, (self.regs.read_reg_value("CFG")>>4)&0b11111),
            bins=[( True, (i*8)+1 , ((i+1)*8) ) for i in range(4)],
            bins_labels=[((i*8)+1 , ((i+1)*8)) for i in range(4)],
            rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        @CoverPoint(
            f"{self.hierarchy}.Right Channel.Sign extended",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b01, (self.regs.read_reg_value("CFG")>>2)&0b1),
            bins=[( True, True ), (True, False) ],
            bins_labels=["sign extended", "not sign extended"],
            # rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        @CoverPoint(
            f"{self.hierarchy}.Right Channel.Left Justified",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b01, (self.regs.read_reg_value("CFG")>>3)&0b1),
            bins=[( True, True ), (True, False) ],
            bins_labels=["left justified", "not left justified"],
            # rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        # @CoverPoint(
        #     f"{self.hierarchy}.Right Channel.Received Data",
        #     xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b01 , tr.sample),
        #     bins=[(True, 1 << i, (1 << i + 1) - 1) if i != 0 else (True, 0, 1) for i in range(32)],
        #     bins_labels=[f"from {hex(1 << i)} to {hex((1 << i + 1) - 1)}" if i != 0 else f"from {hex(0)} to {hex(1)}" for i in range(32)],
        #     rel=lambda val, b:  (val[0] == b[0]) and  (b[1] == val[1] <= b[2])
        # )
        # @CoverPoint(
        #     f"{self.hierarchy}.Right Channel.Received Data",
        #     xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b01 , tr.sample),
        #     bins=[(True, i)  for i in range(32)],
        #     bins_labels=[f"bit {i} = 1" for i in range(32)],
        #     rel=lambda val, b:  (val[0] == b[0]) and  ((val[1]>>b[1])&0b1) == 1  
        # )
        @CoverPoint(
            f"{self.hierarchy}.Stereo.Prescaler",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b11, self.regs.read_reg_value("PR")),
            bins=[( True, i*10 , ((i+1)*10)-1 ) for i in range(5)],
            bins_labels=[(i*10 , ((i+1)*10)-1) for i in range(5)],
            rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        @CoverPoint(
            f"{self.hierarchy}.Stereo.Sample Size",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b11, (self.regs.read_reg_value("CFG")>>4)&0b11111),
            bins=[( True, (i*8)+1 , ((i+1)*8) ) for i in range(4)],
            bins_labels=[((i*8)+1 , ((i+1)*8)) for i in range(4)],
            rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        @CoverPoint(
            f"{self.hierarchy}.Stereo.Sign extended",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b11, (self.regs.read_reg_value("CFG")>>2)&0b1),
            bins=[( True, True ), (True, False) ],
            bins_labels=["sign extended", "not sign extended"],
            # rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        @CoverPoint(
            f"{self.hierarchy}.Stereo.Left Justified",
            xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b11, (self.regs.read_reg_value("CFG")>>3)&0b1),
            bins=[( True, True ), (True, False) ],
            bins_labels=["left justified", "not left justified"],
            # rel=lambda val, b:  (val[0] == b[0]) and (b[1] <= val[1] <= b[2])
        )
        # @CoverPoint(
        #     f"{self.hierarchy}.Stereo.Received Data (left)",
        #     xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b11 , tr.sample),
        #     bins=[(True, 1 << i, (1 << i + 1) - 1) if i != 0 else (True, 0, 1) for i in range(32)],
        #     bins_labels=[f"from {hex(1 << i)} to {hex((1 << i + 1) - 1)}" if i != 0 else f"from {hex(0)} to {hex(1)}" for i in range(32)],
        #     rel=lambda val, b:  (val[0] == b[0]) and  (b[1] <= val[1] <= b[2])
        # )
        # @CoverPoint(
        #     f"{self.hierarchy}.Stereo.Received Data (right)",
        #     xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b11 , tr.sample),
        #     bins=[(True, 1 << i, (1 << i + 1) - 1) if i != 0 else (True, 0, 1) for i in range(32)],
        #     bins_labels=[f"from {hex(1 << i)} to {hex((1 << i + 1) - 1)}" if i != 0 else f"from {hex(0)} to {hex(1)}" for i in range(32)],
        #     rel=lambda val, b:  (val[0] == b[0]) and  (b[1] <= val[1] <= b[2])
        # )
        # @CoverPoint(
        #     f"{self.hierarchy}.Stereo.Received Data (left)",
        #     xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b11 , tr.channel == "left" ,tr.sample),
        #     bins=[(True, True,i)  for i in range(32)],
        #     bins_labels=[f"bit {i} = 1" for i in range(32)],
        #     rel=lambda val, b:  (val[0] == b[0]) and  (val[1] == b[1]) and ((val[2]>>b[2])&0b1) == 1  
        # )
        # @CoverPoint(
        #     f"{self.hierarchy}.Stereo.Received Data (right)",
        #     xf=lambda tr: (self.regs.read_reg_value("CFG") & 0b11 == 0b11 , tr.channel == "right" ,tr.sample),
        #     bins=[(True, True,i)  for i in range(32)],
        #     bins_labels=[f"bit {i} = 1" for i in range(32)],
        #     rel=lambda val, b:  (val[0] == b[0]) and  (val[1] == b[1]) and ((val[2]>>b[2])&0b1) == 1  
        # )


        def sample(tr):
            uvm_info("coverage_ip", tr.convert2string() , UVM_LOW)
        if do_sampling:
            sample(tr)

    def samples_cov(self):
        cov_points = []
        for i in range(32):
            cov_points.append(CoverPoint(
                f"{self.hierarchy}.Left Channel.Received Data.bit{i}",
                xf=lambda tr, i=i: (self.regs.read_reg_value("CFG") & 0b11 == 0b10 , (tr.sample >> i )&0b1),
                bins=[(True, 1), (True, 0)],
                bins_labels=[f"bit {i} = 1", f"bit {i} = 0"],
                # at_least=3,
            ))
            cov_points.append(CoverPoint(
                f"{self.hierarchy}.Right Channel.Received Data.bit{i}",
                xf=lambda tr, i=i: (self.regs.read_reg_value("CFG") & 0b11 == 0b01 , (tr.sample >> i )&0b1),
                bins=[(True, 1), (True, 0)],
                bins_labels=[f"bit {i} = 1", f"bit {i} = 0"],
                # at_least=3,
            ))
            cov_points.append(CoverPoint(
                f"{self.hierarchy}.Stereo.Received Data.bit{i}",
                xf=lambda tr, i=i: (self.regs.read_reg_value("CFG") & 0b11 == 0b11 , (tr.sample >> i )&0b1),
                bins=[(True, 1), (True, 0)],
                bins_labels=[f"bit {i} = 1", f"bit {i} = 0"],
                # at_least=3,
            ))

        return cov_points

    
    def get_gpios_value(self, tr):
        gpios_value = 0 
        for i in range(8):
            if(tr.gpios[f"gpio{i}"].val):
                gpios_value |= 1 << i
        return gpios_value



    def apply_decorators(self, decorators):
        def decorator_wrapper(func):
            for decorator in decorators:
                func = decorator(func)
            return func
        return decorator_wrapper