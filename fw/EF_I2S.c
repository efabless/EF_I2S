#ifndef EF_I2S_C
#define EF_I2S_C

#include <EF_I2S.h>

void EF_I2S_enable (uint32_t i2s_base){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->control = 0x1;
}

void EF_I2S_disable (uint32_t i2s_base){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->control = 0x0;
}

void EF_I2S_setConfigReg (uint32_t i2s_base, int config){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    
    i2s->config = config;

}

int EF_I2S_getConfigReg (uint32_t i2s_base){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    
    return (i2s->config);

}

void EF_I2S_setPrescaler(uint32_t i2s_base, int prescaler){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->prescale = prescaler;
}


int EF_I2S_getPrescaler(uint32_t i2s_base){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    return (i2s->prescale);
}


int EF_I2S_getRxFifoLevel(uint32_t i2s_base){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    return (i2s->FIFOLEVEL);
}

void EF_I2S_setRxFifoThreshold(uint32_t i2s_base, int threshold){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->RXFIFOT = threshold;
}

int EF_I2S_getRxFifoThreshold(uint32_t i2s_base){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    return (i2s->RXFIFOT) ;
}

// bit 0: RX FIFO is Empty
// bit 1: RX FIFO level is above the value in the RX FIFO Level Threshold Register
// bit 2: RX FIFO is Full


int EF_I2S_getRIS(uint32_t i2s_base){
    
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;
    
    return (i2s->ris);
}



int EF_I2S_getMIS(uint32_t i2s_base){

    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    return (i2s->mis);
}

void EF_I2S_setIM(uint32_t i2s_base, int mask){
 
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->im = mask;
}


int EF_I2S_getIM(uint32_t i2s_base){
    
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    return (i2s->im);
}


void EF_I2S_clearIrqRxLevel(uint32_t i2s_base){
    
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->icr = 0x2;
}

void EF_I2S_clearIrqRxempty(uint32_t i2s_base){
    
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    i2s->icr = 0x1;
}

int EF_I2S_readData(uint32_t i2s_base){
    
    EF_I2S_TYPE* i2s = (EF_I2S_TYPE*)i2s_base;

    while((EF_I2S_getRIS(i2s_base) & 0x2) == 0x0); // wait over RX fifo is above Flag to unset  
    //while (EF_I2S_getRIS(i2s_base) & 0x1);
    int data = i2s->rxdata;
    EF_I2S_clearIrqRxLevel(i2s_base);
    //EF_I2S_clearIrqRxLevel(i2s_base);
    return data;
}

#endif