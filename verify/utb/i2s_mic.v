module i2s_mic (
    input sck,
    input ws,
    output reg sdo
);

    localparam LEFT = 18'h1_0A0B, RIGHT = 18'h2_0D0F;
    reg [17:0] rdata = RIGHT;
    reg [17:0] ldata = LEFT;

    always @(posedge ws)
        rdata = RIGHT;

    always @(negedge ws)
        ldata = LEFT;

    always @(posedge sck)
        if(ws) begin
            sdo <= rdata[17];
            rdata <= (rdata << 1);
        end else begin
            sdo <= ldata[17];
            ldata <= (ldata << 1);
        end

endmodule