# EF_I2S
Two-wire I2S synchronous serial interface, compatible with I2S specification.

## Features
- Receiver only
- 32x32 Receive FIFO
- Sample Size selection
- Left channel, Right channel only or Stereo
- Programmable prescaler

## Registers
| Offset | Register | Size | Description |
|--------|----------|------|-------------|
| 0x0000 | RX Data | 32 | The received sample |
| 0x0004 | Prescaler | 8 | Prescaler = clk_freq/(2 x sck_freq) - 1 |
| 0x0008 | FIFO Level | 5 | The current receive FIFO level |
| 0x000C | FIFO level threshold | The threshold above which the controller causes an interrupt |
| 0x0010 | Control | 0: Enable|
| 0x0014 | Configuration | 0-1: Chnnels to read, 0: right, 1: left, 11: Both (stereo)<br> 2: Sign Extend<br> 3: Left Justify<br> 4-8: Sample Size (0-31)|



