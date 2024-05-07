from uvm.base.sv import sv_if


class i2s_if(sv_if):
    def __init__(self, dut):
        bus_map = {"CLK": "CLK", "RESETn": "RESETn", "ws": "ws", "sck": "sck", "sdi": "sdi"}
        super().__init__(dut, "", bus_map)
