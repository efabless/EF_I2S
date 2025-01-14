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

/******************************************************************************
* Includes
******************************************************************************/
#include "EF_Driver_Common.h"


/******************************************************************************
* Macros and Constants
******************************************************************************/
#ifndef IO_TYPES
#define IO_TYPES
#define   __R     volatile const uint32_t
#define   __W     volatile       uint32_t
#define   __RW    volatile       uint32_t
#endif

#define EF_I2S_CTRL_REG_EN_BIT	                    ((uint32_t)0)
#define EF_I2S_CTRL_REG_EN_MASK	                    ((uint32_t)0x1)
#define EF_I2S_CTRL_REG_FIFO_EN_BIT	                ((uint32_t)1)
#define EF_I2S_CTRL_REG_FIFO_EN_MASK	            ((uint32_t)0x2)
#define EF_I2S_CTRL_REG_AVG_EN_BIT	                ((uint32_t)2)
#define EF_I2S_CTRL_REG_AVG_EN_MASK	                ((uint32_t)0x4)
#define EF_I2S_CTRL_REG_ZCR_EN_BIT	                ((uint32_t)3)
#define EF_I2S_CTRL_REG_ZCR_EN_MASK	                ((uint32_t)0x8)
#define EF_I2S_CFG_REG_CHANNELS_BIT	                ((uint32_t)0)
#define EF_I2S_CFG_REG_CHANNELS_MASK	            ((uint32_t)0x3)
#define EF_I2S_CFG_REG_SIGN_EXTEND_BIT	            ((uint32_t)2)
#define EF_I2S_CFG_REG_SIGN_EXTEND_MASK	            ((uint32_t)0x4)
#define EF_I2S_CFG_REG_LEFT_JUSTIFIED_BIT	        ((uint32_t)3)
#define EF_I2S_CFG_REG_LEFT_JUSTIFIED_MASK	        ((uint32_t)0x8)
#define EF_I2S_CFG_REG_SAMPLE_SIZE_BIT	            ((uint32_t)4)
#define EF_I2S_CFG_REG_SAMPLE_SIZE_MASK	            ((uint32_t)0x3f0)
#define EF_I2S_CFG_REG_AVGSEL_BIT	                ((uint32_t)10)
#define EF_I2S_CFG_REG_AVGSEL_MASK	                ((uint32_t)0x400)
#define EF_I2S_CFG_REG_ZCRSEL_BIT	                ((uint32_t)11)
#define EF_I2S_CFG_REG_ZCRSEL_MASK	                ((uint32_t)0x800)
#define EF_I2S_RX_FIFO_LEVEL_REG_LEVEL_BIT	        ((uint32_t)0)
#define EF_I2S_RX_FIFO_LEVEL_REG_LEVEL_MASK	        ((uint32_t)0xf)
#define EF_I2S_RX_FIFO_THRESHOLD_REG_THRESHOLD_BIT	((uint32_t)0)
#define EF_I2S_RX_FIFO_THRESHOLD_REG_THRESHOLD_MASK	((uint32_t)0xf)
#define EF_I2S_RX_FIFO_FLUSH_REG_FLUSH_BIT	        ((uint32_t)0)
#define EF_I2S_RX_FIFO_FLUSH_REG_FLUSH_MASK	        ((uint32_t)0x1)
#define EF_I2S_FIFOE_FLAG	                        ((uint32_t)0x1)
#define EF_I2S_FIFOA_FLAG	                        ((uint32_t)0x2)
#define EF_I2S_FIFOF_FLAG	                        ((uint32_t)0x4)
#define EF_I2S_AVGF_FLAG	                        ((uint32_t)0x8)
#define EF_I2S_ZCRF_FLAG	                        ((uint32_t)0x10)
#define EF_I2S_VADF_FLAG	                        ((uint32_t)0x20)

/******************************************************************************
* Typedefs and Enums
******************************************************************************/
typedef struct _EF_I2S_TYPE_ {
	__R 	RXDATA;
	__W 	PR;
	__W 	AVGT;
	__W 	ZCRT;
	__W 	CTRL;
	__W 	CFG;
	__R 	reserved_0[16250];
	__R 	RX_FIFO_LEVEL;
	__W 	RX_FIFO_THRESHOLD;
	__W 	RX_FIFO_FLUSH;
	__R 	reserved_1[61];
	__RW	IM;
	__R 	MIS;
	__R 	RIS;
	__W 	IC;
	__W 	GCLK;
} EF_I2S_TYPE;

typedef EF_I2S_TYPE*   EF_I2S_TYPE_PTR;               // EF_I2S Type Pointer


/******************************************************************************
* Function Prototypes
******************************************************************************/



/******************************************************************************
* External Variables
******************************************************************************/




#endif // EF_I2SREGS_H

/******************************************************************************
* End of File
******************************************************************************/