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


EF_DRIVER_STATUS EF_I2S_setGclkEnable (EF_I2S_TYPE_PTR i2s, uint32_t value);

EF_DRIVER_STATUS EF_I2S_enable (EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_disable (EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_enableFifo (EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_disableFifo (EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_enableAVG (EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_disableAVG (EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_enableZCR(EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_disableZCR(EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_setConfigReg (EF_I2S_TYPE_PTR i2s, uint32_t config);

EF_DRIVER_STATUS EF_I2S_getConfigReg (EF_I2S_TYPE_PTR i2s, uint32_t* config);

EF_DRIVER_STATUS EF_I2S_setPrescaler(EF_I2S_TYPE_PTR i2s, uint32_t prescaler);

EF_DRIVER_STATUS EF_I2S_getPrescaler(EF_I2S_TYPE_PTR i2s, uint32_t* prescaler);

EF_DRIVER_STATUS EF_I2S_setAVGT(EF_I2S_TYPE_PTR i2s, uint32_t average);

EF_DRIVER_STATUS EF_I2S_setZCRT(EF_I2S_TYPE_PTR i2s, uint32_t average);

EF_DRIVER_STATUS EF_I2S_getRxFifoLevel(EF_I2S_TYPE_PTR i2s, uint32_t* level);

EF_DRIVER_STATUS EF_I2S_setRxFifoThreshold(EF_I2S_TYPE_PTR i2s, uint32_t threshold);

EF_DRIVER_STATUS EF_I2S_getRxFifoThreshold(EF_I2S_TYPE_PTR i2s, uint32_t* threshold);

EF_DRIVER_STATUS EF_I2S_getRIS(EF_I2S_TYPE_PTR i2s, uint32_t* ris_value);

EF_DRIVER_STATUS EF_I2S_getMIS(EF_I2S_TYPE_PTR i2s, uint32_t* mis_value);

EF_DRIVER_STATUS EF_I2S_setIM(EF_I2S_TYPE_PTR i2s, uint32_t mask);

EF_DRIVER_STATUS EF_I2S_setIC(EF_I2S_TYPE_PTR i2s, uint32_t mask);

EF_DRIVER_STATUS EF_I2S_getIM(EF_I2S_TYPE_PTR i2s, uint32_t* im_value);

EF_DRIVER_STATUS EF_I2S_readData(EF_I2S_TYPE_PTR i2s, uint32_t* data);

// The following functions are not verified yet
/******************************************************************************************************************************************/
/******************************************************************************************************************************************/

EF_DRIVER_STATUS EF_I2S_clearIrqRxLevel(EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_clearIrqRxEmpty(EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_clearIrqRxFull(EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_clearIrqAVGAboveThreshold(EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_clearIrqZCR(EF_I2S_TYPE_PTR i2s);

EF_DRIVER_STATUS EF_I2S_clearIrqVAD(EF_I2S_TYPE_PTR i2s);

/******************************************************************************
* External Variables
******************************************************************************/


#endif // EF_I2S_H

/******************************************************************************
* End of File
******************************************************************************/
