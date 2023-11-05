
/*
	Copyright 2023 Efabless Corp.

	Author: Mohamed Shalan (mshalan@efabless.com)

	This file is auto-generated by wrapper_gen.py on 2023-11-05

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


#ifndef IO_TYPES
#define IO_TYPES
#define   __R     volatile const unsigned int
#define   __W     volatile       unsigned int
#define   __RW    volatile       unsigned int
#endif

#define I2S_PRESCALE_REG_PRESCALE		0
#define I2S_PRESCALE_REG_PRESCALE_LEN	8
#define I2S_FIFOLEVEL_REG_FIFO_LEVEL		0
#define I2S_FIFOLEVEL_REG_FIFO_LEVEL_LEN	4
#define I2S_RXFIFOT_REG_FIFO_LEVEL_THRESHOLD		0
#define I2S_RXFIFOT_REG_FIFO_LEVEL_THRESHOLD_LEN	5
#define I2S_CONTROL_REG_EN		0
#define I2S_CONTROL_REG_EN_LEN	1
#define I2S_CONTROL_REG_CHANNELS		1
#define I2S_CONTROL_REG_CHANNELS_LEN	2
#define I2S_EMPTY_FLAG_FLAG	0x1
#define I2S_ABOVE_FLAG_FLAG	0x2
#define I2S_FULL_FLAG_FLAG	0x4

typedef struct {
	__RW	rxdata;
	__RW	prescale;
	__R 	FIFOLEVEL;
	__RW	RXFIFOT;
	__RW	control;
	__R 	reserved[955];
	__W 	icr;
	__R 	ris;
	__RW	im;
	__R 	mis;
} I2S_TYPE;
