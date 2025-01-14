/*
	Copyright 2025 Efabless Corp.


	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	    www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.

*/


/*! \file EF_I2S.h
    \brief C header file for I2S APIs which contains the function prototypes 
    
*/

#ifndef EF_I2S_H
#define EF_I2S_H

/******************************************************************************
* Includes
******************************************************************************/
#include "EF_I2S_regs.h"
#include "EF_Driver_Common.h"

/******************************************************************************
* Macros and Constants
******************************************************************************/

/******************************************************************************
* Typedefs and Enums
******************************************************************************/

/******************************************************************************
* Function Prototypes
******************************************************************************/


EF_DRIVER_STATUS EF_I2S_setGclkEnable (uint32_t i2s_base, uint32_t value);

EF_DRIVER_STATUS EF_I2S_enable (uint32_t i2s_base);

EF_DRIVER_STATUS EF_I2S_disable (uint32_t i2s_base);

EF_DRIVER_STATUS EF_I2S_enableFifo (uint32_t i2s_base);

EF_DRIVER_STATUS EF_I2S_disableFifo (uint32_t i2s_base);

EF_DRIVER_STATUS EF_I2S_enableAVG (uint32_t i2s_base);

EF_DRIVER_STATUS EF_I2S_disableAVG (uint32_t i2s_base);

EF_DRIVER_STATUS EF_I2S_enableZCR(uint32_t i2s_base);

EF_DRIVER_STATUS EF_I2S_disableZCR(uint32_t i2s_base);

EF_DRIVER_STATUS EF_I2S_setConfigReg (uint32_t i2s_base, uint32_t config);

EF_DRIVER_STATUS EF_I2S_getConfigReg (uint32_t i2s_base, uint32_t* config);

EF_DRIVER_STATUS EF_I2S_setPrescaler(uint32_t i2s_base, uint32_t prescaler);

EF_DRIVER_STATUS EF_I2S_getPrescaler(uint32_t i2s_base, uint32_t* prescaler);

EF_DRIVER_STATUS EF_I2S_setAVGT(uint32_t i2s_base, uint32_t average);

EF_DRIVER_STATUS EF_I2S_setZCRT(uint32_t i2s_base, uint32_t average);

EF_DRIVER_STATUS EF_I2S_getRxFifoLevel(uint32_t i2s_base, uint32_t* level);

EF_DRIVER_STATUS EF_I2S_setRxFifoThreshold(uint32_t i2s_base, uint32_t threshold);

EF_DRIVER_STATUS EF_I2S_getRxFifoThreshold(uint32_t i2s_base, uint32_t* threshold);

EF_DRIVER_STATUS EF_I2S_getRIS(uint32_t i2s_base, uint32_t* ris_value);

EF_DRIVER_STATUS EF_I2S_getMIS(uint32_t i2s_base, uint32_t* mis_value);

EF_DRIVER_STATUS EF_I2S_setIM(uint32_t i2s_base, uint32_t mask);

EF_DRIVER_STATUS EF_I2S_setIC(uint32_t i2s_base, uint32_t mask);

EF_DRIVER_STATUS EF_I2S_getIM(uint32_t i2s_base, uint32_t* im_value);

EF_DRIVER_STATUS EF_I2S_clearIrqRxLevel(uint32_t i2s_base);

EF_DRIVER_STATUS EF_I2S_clearIrqRxLevel(uint32_t i2s_base);

EF_DRIVER_STATUS EF_I2S_readData(uint32_t i2s_base, uint32_t* data);


/******************************************************************************
* External Variables
******************************************************************************/


#endif // EF_I2S_H

/******************************************************************************
* End of File
******************************************************************************/
