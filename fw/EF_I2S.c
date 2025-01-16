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


EF_DRIVER_STATUS EF_I2S_setGclkEnable (EF_I2S_TYPE_PTR i2s, uint32_t value){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (value > (uint32_t)0x1) {  
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if value is out of range
    }else {
        i2s->GCLK = value;                      // Set the GCLK enable bit to the given value
    }
    return status;
}

EF_DRIVER_STATUS EF_I2S_enable (EF_I2S_TYPE_PTR i2s){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }
    else{
        i2s->CTRL |= EF_I2S_CTRL_REG_EN_MASK;
    }
    return status;
}

EF_DRIVER_STATUS EF_I2S_disable (EF_I2S_TYPE_PTR i2s){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }
    else{
        i2s->CTRL &= ~EF_I2S_CTRL_REG_EN_MASK;
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_enableFifo(EF_I2S_TYPE_PTR i2s){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }
    else{
        i2s->CTRL |= EF_I2S_CTRL_REG_FIFO_EN_MASK;
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_disableFifo(EF_I2S_TYPE_PTR i2s){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }
    else{
        i2s->CTRL &= ~EF_I2S_CTRL_REG_FIFO_EN_MASK;
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_enableAVG(EF_I2S_TYPE_PTR i2s){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }
    else{
        i2s->CTRL |= EF_I2S_CTRL_REG_AVG_EN_MASK;
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_disableAVG(EF_I2S_TYPE_PTR i2s){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }
    else{
        i2s->CTRL &= ~EF_I2S_CTRL_REG_AVG_EN_MASK;
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_enableZCR(EF_I2S_TYPE_PTR i2s){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }
    else{
        i2s->CTRL |= EF_I2S_CTRL_REG_ZCR_EN_MASK;
    }
    return status;
}

EF_DRIVER_STATUS EF_I2S_disableZCR(EF_I2S_TYPE_PTR i2s){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }
    else{
        i2s->CTRL &= ~EF_I2S_CTRL_REG_ZCR_EN_MASK;
    }
    return status;
}



EF_DRIVER_STATUS EF_I2S_setConfigReg (EF_I2S_TYPE_PTR i2s, uint32_t config){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (config > EF_I2S_CFG_REG_MAX_VALUE) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if config is out of range
    }else {
        i2s->CFG = config;                      // Set the configuration register to the given value
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_setPrescaler(EF_I2S_TYPE_PTR i2s, uint32_t prescaler){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (prescaler > EF_I2S_PR_REG_MAX_VALUE) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if prescaler is out of range
    }else {
        i2s->PR = prescaler;                    // Set the prescaler register to the given value
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_setAVGT(EF_I2S_TYPE_PTR i2s, uint32_t average){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (average > EF_I2S_AVGT_REG_MAX_VALUE) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if average is out of range
    }else {
        i2s->AVGT = average;                    // Set the AVGT register to the given value
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_setZCRT(EF_I2S_TYPE_PTR i2s, uint32_t average){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (average > EF_I2S_ZCRT_REG_MAX_VALUE) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if average is out of range
    }else {
        i2s->ZCRT = average;                    // Set the ZCRT register to the given value
    }
    return status;
}

EF_DRIVER_STATUS EF_I2S_getRxFifoLevel(EF_I2S_TYPE_PTR i2s, uint32_t* level){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (level == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if level is NULL
    } else {
        *level = i2s->RX_FIFO_LEVEL;            // Get the RX FIFO level
    }
    return status;
}

EF_DRIVER_STATUS EF_I2S_setRxFifoThreshold(EF_I2S_TYPE_PTR i2s, uint32_t threshold){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (threshold > EF_I2S_RX_FIFO_THRESHOLD_REG_MAX_VALUE) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if average is out of range
    } else {
        i2s->RX_FIFO_THRESHOLD = threshold;
    }
    return status;

}


EF_DRIVER_STATUS EF_I2S_getRIS(EF_I2S_TYPE_PTR i2s, uint32_t* ris_value){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (ris_value == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if ris_value is NULL
    } else {
        *ris_value = i2s->RIS;
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_getMIS(EF_I2S_TYPE_PTR i2s, uint32_t* mis_value){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (mis_value == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if mis_value is NULL
    } else {
        *mis_value = i2s->MIS;
    }
    return status;
}



EF_DRIVER_STATUS EF_I2S_setIM(EF_I2S_TYPE_PTR i2s, uint32_t mask){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else if (mask > EF_I2S_RX_FIFO_IM_REG_MAX_VALUE){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if mask is out of range
    } else {
        i2s->IM = mask;
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_setIC(EF_I2S_TYPE_PTR i2s, uint32_t mask){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else if (mask > EF_I2S_RX_FIFO_IC_REG_MAX_VALUE){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if mask is out of range
    } else {
        i2s->IC = mask;
    }
    return status;
}



EF_DRIVER_STATUS EF_I2S_getIM(EF_I2S_TYPE_PTR i2s, uint32_t* im_value){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else if (im_value == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if im_value is NULL
    } else {
        *im_value = i2s->IM;
    }
    return status;
}

EF_DRIVER_STATUS EF_I2S_readData(EF_I2S_TYPE_PTR i2s, uint32_t* data){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }
    else if (data == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if data is NULL
    } else {
        uint32_t ris_value;
        do {
            // wait until RX FIFO is not empty
            EF_I2S_getRIS(i2s, ris_value);
        }
        while((ris_value & 0x2) == 0x0); // wait over RX fifo is above Flag to unset  
        //while (EF_I2S_getRIS(i2s) & 0x1);
        *data = i2s->RXDATA;
        EF_I2S_clearIrqRxLevel(i2s);
    }
}
// The following functions are not verified yet
/******************************************************************************************************************************************/
/******************************************************************************************************************************************/


EF_DRIVER_STATUS EF_I2S_clearIrqRxempty(EF_I2S_TYPE_PTR i2s){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, EF_I2S_FIFOE_FLAG);
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_clearIrqRxLevel(EF_I2S_TYPE_PTR i2s){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, EF_I2S_FIFOA_FLAG);
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_clearIrqRxFull(EF_I2S_TYPE_PTR i2s){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, EF_I2S_FIFOF_FLAG);
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_clearIrqAVGAboveThreshold(EF_I2S_TYPE_PTR i2s){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, EF_I2S_AVGF_FLAG);
    }
    return status;
}



EF_DRIVER_STATUS EF_I2S_clearIrqZCRAboveThreshold(EF_I2S_TYPE_PTR i2s){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, EF_I2S_ZCRF_FLAG);       
    }
    return status;
}



EF_DRIVER_STATUS EF_I2S_clearIrqVADFlag(EF_I2S_TYPE_PTR i2s){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, EF_I2S_VADF_FLAG);
    }
    return status;
}

EF_DRIVER_STATUS EF_I2S_RxFIFOAvailable(EF_I2S_TYPE_PTR i2s, bool* isAvailable){
    EF_DRIVER_STATUS status = EF_DRIVER_OK;
    uint32_t ris_value;
    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else if (isAvailable == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if isAvailable is NULL
    } else {
        EF_I2S_getRIS(i2s, ris_value);
        if((ris_value & EF_I2S_FIFOF_FLAG)){   // check if RX FIFO is full
            *isAvailable = false;
        }else{
            *isAvailable = true;
        }
    }
    return status;
}



EF_DRIVER_STATUS EF_I2S_RxFIFOEmpty(EF_I2S_TYPE_PTR i2s, bool* isEmpty){
    EF_DRIVER_STATUS status = EF_DRIVER_OK;
    uint32_t ris_value;
    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else if (isEmpty == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if isEmpty is NULL
    } else {
        EF_I2S_getRIS(i2s, ris_value);
        if((ris_value & EF_I2S_FIFOE_FLAG)){   // check if RX FIFO is empty
            *isEmpty = true;
        }else{
            *isEmpty = false;
        }
    }
    return status;
}



EF_DRIVER_STATUS EF_I2S_RxFIFOFull(EF_I2S_TYPE_PTR i2s, bool* isFull){
    EF_DRIVER_STATUS status = EF_DRIVER_OK;
    uint32_t ris_value;
    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else if (isFull == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if isFull is NULL
    } else {
        EF_I2S_getRIS(i2s, ris_value);
        if((ris_value & EF_I2S_FIFOF_FLAG)){   // check if RX FIFO is full
            *isFull = true;
        }else{
            *isFull = false;
        }
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_Busy(EF_I2S_TYPE_PTR i2s, bool* isBusy){
    EF_DRIVER_STATUS status = EF_DRIVER_OK;
    uint32_t ris_value;
    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else if (isBusy == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if isBusy is NULL
    } else {
        EF_I2S_getRIS(i2s, ris_value);
        if((ris_value & EF_I2S_FIFOE_FLAG)){   // check if RX FIFO is full
            *isBusy = false;
        }else{
            *isBusy = true;
        }
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_FIFOOverThreshold(EF_I2S_TYPE_PTR i2s, bool* isOverThreshold){
    EF_DRIVER_STATUS status = EF_DRIVER_OK;
    uint32_t ris_value;
    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else if (isOverThreshold == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if isOverThreshold is NULL
    } else {
        EF_I2S_getRIS(i2s, ris_value);
        if((ris_value & EF_I2S_FIFOA_FLAG)){   // check if RX FIFO is full
            *isOverThreshold = true;
        }else{
            *isOverThreshold = false;
        }
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_ZCROverThreshold(EF_I2S_TYPE_PTR i2s, bool* isOverThreshold){
    EF_DRIVER_STATUS status = EF_DRIVER_OK;
    uint32_t ris_value;
    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else if (isOverThreshold == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if isOverThreshold is NULL
    } else {
        EF_I2S_getRIS(i2s, ris_value);
        if((ris_value & EF_I2S_ZCRF_FLAG)){   // check if RX FIFO is full
            *isOverThreshold = true;
        }else{
            *isOverThreshold = false;
        }
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_VADFlag(EF_I2S_TYPE_PTR i2s, bool* isOverThreshold){
    EF_DRIVER_STATUS status = EF_DRIVER_OK;
    uint32_t ris_value;
    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else if (isOverThreshold == NULL){
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if isOverThreshold is NULL
    } else {
        EF_I2S_getRIS(i2s, ris_value);
        if((ris_value & EF_I2S_VADF_FLAG)){     // check if RX FIFO is full
            *isOverThreshold = true;
        }else{
            *isOverThreshold = false;
        }
    }
    return status;
}


/******************************************************************************
* Static Function Definitions
******************************************************************************/



#endif // EF_I2S_C

/******************************************************************************
* End of File
******************************************************************************/
