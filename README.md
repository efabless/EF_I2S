# EF_I2S
Two-wire I2S synchronous serial interface, compatible with I2S specification.

## Features
- Receiver only
- 32x32 Receive FIFO
- Sample Size selection
- Left channel, Right channel only or Stereo
- Programmable prescaler
- Suports both the classical I2S and the Left-aligned formats
- Programmable sample size
- Zero/Sign extension for the samples

## Registers
| Offset | Register | Size | Description |
|--------|----------|------|-------------|
| 0x0000 | RX Data | 32 | The received sample |
| 0x0004 | Prescaler | 8 | Prescaler = clk_freq/(2 x sck_freq) - 1 |
| 0x0008 | FIFO Level | 5 | The current receive FIFO level |
| 0x000C | FIFO level threshold | 5|The threshold above which the controller causes an interrupt |
| 0x0010 | Control |1| 0: Enable|
| 0x0014 | Configuration |9| 0-1: Channels to read, 0: right, 1: left, 11: Both (stereo)<br> 2: Sign Extend<br> 3: Left Justify<br> 4-8: Sample Size (0-31)|
| 0x0F00 | ICR | 3 | Interrupts Clear Register |
| 0x0F04 | RIS | 3 | Raw Interrupts Status Register |
| 0x0F08 | IM | Interrupts Masking Register |
| 0x0F0C | MIS | Masked Inetrrupts Status Register |

## Inetrrupt Flags
| Bit | Flag |
|-----|------|
| 0   | Receive FIFO is Empty |
| 1   | FIFO level is above the set level threshold |
| 2   | Receive FIFO is Full |
