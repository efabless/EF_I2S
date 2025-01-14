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


/*! \file EF_I2C.c
    \brief C header file for I2S APIs which contains the function implementations 
    
*/

#ifndef EF_I2S_C
#define EF_I2S_C


/******************************************************************************
* Includes
******************************************************************************/
#include "EF_I2S.h"

/******************************************************************************
* File-Specific Macros and Constants
******************************************************************************/



/******************************************************************************
* Static Variables
******************************************************************************/



/******************************************************************************
* Static Function Prototypes
******************************************************************************/



/******************************************************************************
* Function Definitions
******************************************************************************/


EF_DRIVER_STATUS EF_I2S_setGclkEnable (uint32_t i2s_base, uint32_t value){
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    i2s->GCLK = value;
}

EF_DRIVER_STATUS EF_I2S_enable (uint32_t i2s_base){
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    uint32_t control = i2s->CTRL;
    control |= EF_I2S_CTRL_REG_EN_MASK;
    i2s->CTRL = control;
}

EF_DRIVER_STATUS EF_I2S_disable (uint32_t i2s_base){
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    uint32_t control = i2s->CTRL;
    control &= ~EF_I2S_CTRL_REG_EN_MASK;
    i2s->CTRL = control;
}

EF_DRIVER_STATUS EF_I2S_enableFifo(uint32_t i2s_base){
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    uint32_t control = i2s->CTRL;
    control |= EF_I2S_CTRL_REG_FIFO_EN_MASK;
    i2s->CTRL = control;
}

EF_DRIVER_STATUS EF_I2S_disableFifo(uint32_t i2s_base){
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    uint32_t control = i2s->CTRL;
    control &= ~EF_I2S_CTRL_REG_FIFO_EN_MASK;
    i2s->CTRL = control;
}

EF_DRIVER_STATUS EF_I2S_enableAVG(uint32_t i2s_base){
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    uint32_t control = i2s->CTRL;
    control |= EF_I2S_CTRL_REG_AVG_EN_MASK;
    i2s->CTRL = control;
}


EF_DRIVER_STATUS EF_I2S_disableAVG(uint32_t i2s_base){
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    uint32_t control = i2s->CTRL;
    control &= ~EF_I2S_CTRL_REG_AVG_EN_MASK;
    i2s->CTRL = control;
}

EF_DRIVER_STATUS EF_I2S_enableZCR(uint32_t i2s_base){
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    uint32_t control = i2s->CTRL;
    control |= EF_I2S_CTRL_REG_ZCR_EN_MASK;
    i2s->CTRL = control;
}

EF_DRIVER_STATUS EF_I2S_disableZCR(uint32_t i2s_base){
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    uint32_t control = i2s->CTRL;
    control &= ~EF_I2S_CTRL_REG_ZCR_EN_MASK;
    i2s->CTRL = control;
}



EF_DRIVER_STATUS EF_I2S_setConfigReg (uint32_t i2s_base, uint32_t config){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    
    i2s->CFG = config;

}

EF_DRIVER_STATUS EF_I2S_getConfigReg (uint32_t i2s_base, uint32_t* config){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    
    *config = i2s->CFG;

}

EF_DRIVER_STATUS EF_I2S_setPrescaler(uint32_t i2s_base, uint32_t prescaler){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->PR = prescaler;
}


EF_DRIVER_STATUS EF_I2S_getPrescaler(uint32_t i2s_base, uint32_t* prescaler){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    *prescaler = (i2s->PR);
}

EF_DRIVER_STATUS EF_I2S_setAVGT(uint32_t i2s_base, uint32_t average){
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->AVGT = average;
}

EF_DRIVER_STATUS EF_I2S_setZCRT(uint32_t i2s_base, uint32_t average){
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->ZCRT = average;
}



EF_DRIVER_STATUS EF_I2S_getRxFifoLevel(uint32_t i2s_base, uint32_t* level){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    *level = i2s->RX_FIFO_LEVEL;
}

EF_DRIVER_STATUS EF_I2S_setRxFifoThreshold(uint32_t i2s_base, uint32_t threshold){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->RX_FIFO_THRESHOLD = threshold;
}

EF_DRIVER_STATUS EF_I2S_getRxFifoThreshold(uint32_t i2s_base, uint32_t* threshold){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    *threshold = i2s->RX_FIFO_THRESHOLD;
}

// bit 0: RX FIFO is Empty
// bit 1: RX FIFO level is above the value in the RX FIFO Level Threshold Register
// bit 2: RX FIFO is Full


EF_DRIVER_STATUS EF_I2S_getRIS(uint32_t i2s_base, uint32_t* ris_value){
    
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    
    *ris_value = i2s->RIS;
}



EF_DRIVER_STATUS EF_I2S_getMIS(uint32_t i2s_base, uint32_t* mis_value){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    *mis_value = i2s->MIS;
}

EF_DRIVER_STATUS EF_I2S_setIM(uint32_t i2s_base, uint32_t mask){
 
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->IM = mask;
}

EF_DRIVER_STATUS EF_I2S_setIC(uint32_t i2s_base, uint32_t mask){
 
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->IC = mask;
}



EF_DRIVER_STATUS EF_I2S_getIM(uint32_t i2s_base, uint32_t* im_value){
    
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    *im_value = i2s->IM;
}


EF_DRIVER_STATUS EF_I2S_clearIrqRxLevel(uint32_t i2s_base){
    
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->IC = 0x2;
}

EF_DRIVER_STATUS EF_I2S_clearIrqRxempty(uint32_t i2s_base){
    
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->IC = 0x1;
}

EF_DRIVER_STATUS EF_I2S_readData(uint32_t i2s_base, uint32_t* data){
    
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    uint32_t ris_value;
    do {
        // wait until RX FIFO is not empty
        EF_I2S_getRIS(i2s_base, ris_value);
    }
    while((ris_value & 0x2) == 0x0); // wait over RX fifo is above Flag to unset  
    //while (EF_I2S_getRIS(i2s_base) & 0x1);
     *data = i2s->RXDATA;
    EF_I2S_clearIrqRxLevel(i2s_base);
    //EF_I2S_clearIrqRxLevel(i2s_base);

}


/******************************************************************************
* Static Function Definitions
******************************************************************************/



#endif // EF_I2S_C

/******************************************************************************
* End of File
******************************************************************************/

