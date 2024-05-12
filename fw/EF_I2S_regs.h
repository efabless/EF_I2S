/*
	Copyright 2024 Efabless Corp.

	Author: Mohamed Shalan (mshalan@efabless.com)

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	    http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

*/

#ifndef EF_I2SREGS_H
#define EF_I2SREGS_H

#ifndef IO_TYPES
#define IO_TYPES
#define   __R     volatile const unsigned int
#define   __W     volatile       unsigned int
#define   __RW    volatile       unsigned int
#endif

#define EF_I2S_CTRL_REG_EN_BIT	0
#define EF_I2S_CTRL_REG_EN_MASK	0x1
#define EF_I2S_CTRL_REG_FIFO_EN_BIT	1
#define EF_I2S_CTRL_REG_FIFO_EN_MASK	0x2
#define EF_I2S_CTRL_REG_AVG_EN_BIT	2
#define EF_I2S_CTRL_REG_AVG_EN_MASK	0x4
#define EF_I2S_CFG_REG_CHANNELS_BIT	0
#define EF_I2S_CFG_REG_CHANNELS_MASK	0x3
#define EF_I2S_CFG_REG_SIGN_EXTEND_BIT	2
#define EF_I2S_CFG_REG_SIGN_EXTEND_MASK	0x4
#define EF_I2S_CFG_REG_LEFT_JUSTIFIED_BIT	3
#define EF_I2S_CFG_REG_LEFT_JUSTIFIED_MASK	0x8
#define EF_I2S_CFG_REG_SAMPLE_SIZE_BIT	4
#define EF_I2S_CFG_REG_SAMPLE_SIZE_MASK	0x3f0
#define EF_I2S_RX_FIFO_LEVEL_REG_LEVEL_BIT	0
#define EF_I2S_RX_FIFO_LEVEL_REG_LEVEL_MASK	0xf
#define EF_I2S_RX_FIFO_THRESHOLD_REG_THRESHOLD_BIT	0
#define EF_I2S_RX_FIFO_THRESHOLD_REG_THRESHOLD_MASK	0xf
#define EF_I2S_RX_FIFO_FLUSH_REG_FLUSH_BIT	0
#define EF_I2S_RX_FIFO_FLUSH_REG_FLUSH_MASK	0x1

#define EF_I2S_FIFOE_FLAG	0x1
#define EF_I2S_FIFOA_FLAG	0x2
#define EF_I2S_FIFOF_FLAG	0x4
#define EF_I2S_AVGF_FLAG	0x8

typedef struct _EF_I2S_TYPE_ {
	__R 	RXDATA;
	__W 	PR;
	__W 	AVGT;
	__W 	CTRL;
	__W 	CFG;
	__R 	reserved_0[16251];
	__R 	RX_FIFO_LEVEL;
	__W 	RX_FIFO_THRESHOLD;
	__W 	RX_FIFO_FLUSH;
	__R 	reserved_1[61];
	__RW	IM;
	__R 	MIS;
	__R 	RIS;
	__W 	IC;
} EF_I2S_TYPE;

#endif

