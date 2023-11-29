#ifndef EF_I2S_H
#define EF_I2S_H

#include <stdint.h>
#include <EF_I2S_regs.h>

void EF_I2S_enable (uint32_t i2s_base);

void EF_I2S_disable (uint32_t i2s_base);

void EF_I2S_setConfigReg (uint32_t i2s_base, int config);

int EF_I2S_getConfigReg (uint32_t i2s_base);

void EF_I2S_setPrescaler(uint32_t i2s_base, int prescaler);

int EF_I2S_getPrescaler(uint32_t i2s_base);

int EF_I2S_getRxFifoLevel(uint32_t i2s_base);

void EF_I2S_setRxFifoThreshold(uint32_t i2s_base, int threshold);

int EF_I2S_getRxFifoThreshold(uint32_t i2s_base);

int EF_I2S_getRIS(uint32_t i2s_base);

int EF_I2S_getMIS(uint32_t i2s_base);

void EF_I2S_setIM(uint32_t i2s_base, int mask);

int EF_I2S_getIM(uint32_t i2s_base);

void EF_I2S_clearIrqRxLevel(uint32_t i2s_base);

int EF_I2S_readData(uint32_t i2s_base);

#endif