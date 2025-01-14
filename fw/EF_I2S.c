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


//! Sets the GCLK enable bit in the I2S register to a certain value
    /*!
        \param [in] i2s An \ref EF_I2S_TYPE_PTR , which points to the base memory address of I2S registers. \ref EF_I2S_TYPE is a structure that contains the I2S registers.
        \param [in] value The value of the GCLK enable bit
        
        \return status A value of type \ref EF_DRIVER_STATUS : returns a success or error code 
    */
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


#define EF_I2S_CFG_REG_MAX_VALUE    0x00000FFF                      // 12 bits
#define EF_I2S_PR_REG_MAX_VALUE     0x000000FF                      // 8 bits

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


EF_DRIVER_STATUS EF_I2S_getConfigReg (EF_I2S_TYPE_PTR i2s, uint32_t* config){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (config == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if config is NULL
    } else {
        *config = i2s->CFG;                     // Get the configuration register value
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


EF_DRIVER_STATUS EF_I2S_getPrescaler(EF_I2S_TYPE_PTR i2s, uint32_t* prescaler){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (prescaler == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if prescaler is NULL
    } else {
        *prescaler = i2s->PR;                   // Get the prescaler register value
    }
    return status;
}

#define EF_I2S_AVGT_REG_MAX_VALUE       0x0000FFFF                      // 16 bits


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

#define EF_I2S_ZCRT_REG_MAX_VALUE       0x0000FFFF                      // 16 bits

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


#define EF_I2S_RX_FIFO_THRESHOLD_REG_MAX_VALUE       0x0000000F                      // 4 bits

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

EF_DRIVER_STATUS EF_I2S_getRxFifoThreshold(EF_I2S_TYPE_PTR i2s, uint32_t* threshold){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    } else if (threshold == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if threshold is NULL
    } else {    

        *threshold = i2s->RX_FIFO_THRESHOLD;
    }
    return status;
}

// bit 0: RX FIFO is Empty
// bit 1: RX FIFO level is above the value in the RX FIFO Level Threshold Register
// bit 2: RX FIFO is Full


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

#define EF_I2S_RX_FIFO_IM_REG_MAX_VALUE       0x0000003F                      // 6 bits

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


#define EF_I2S_RX_FIFO_IC_REG_MAX_VALUE       0x0000003F                      // 6 bits

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
    

    uint32_t ris_value;
    do {
        // wait until RX FIFO is not empty
        EF_I2S_getRIS(i2s, ris_value);
    }
    while((ris_value & 0x2) == 0x0); // wait over RX fifo is above Flag to unset  
    //while (EF_I2S_getRIS(i2s) & 0x1);
     *data = i2s->RXDATA;
    EF_I2S_clearIrqRxLevel(i2s);
    //EF_I2S_clearIrqRxLevel(i2s);

}
// The following functions are not verified yet
/******************************************************************************************************************************************/
/******************************************************************************************************************************************/


EF_DRIVER_STATUS EF_I2S_clearIrqRxLevel(EF_I2S_TYPE_PTR i2s){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, 0x2);
    }
    return status;
}

EF_DRIVER_STATUS EF_I2S_clearIrqRxempty(EF_I2S_TYPE_PTR i2s){

    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, 0x1);
    }
    return status;
}

EF_DRIVER_STATUS EF_I2S_clearIrqRxFull(EF_I2S_TYPE_PTR i2s){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, 0x4);
    }
    return status;
}


EF_DRIVER_STATUS EF_I2S_clearIrqAVGAboveThreshold(EF_I2S_TYPE_PTR i2s){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, 0x8);
    }
    return status;
}

EF_DRIVER_STATUS EF_I2S_clearIrqZCRAboveThreshold(EF_I2S_TYPE_PTR i2s){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, 0x10);       
    }
    return status;
}

EF_DRIVER_STATUS EF_I2S_clearIrqVADFlag(EF_I2S_TYPE_PTR i2s){
    
    EF_DRIVER_STATUS status = EF_DRIVER_OK;

    if (i2s == NULL) {
        status = EF_DRIVER_ERROR_PARAMETER;     // Return EF_DRIVER_ERROR_PARAMETER if i2s is NULL
    }else{
        status = EF_I2S_setIC(i2s, 0x20);
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
