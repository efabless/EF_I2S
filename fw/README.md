# API Reference

## Header files

- [EF_Driver_Common.h](#file-ef_driver_commonh)
- [EF_I2S.h](#file-ef_i2sh)
- [EF_I2S_regs.h](#file-ef_i2s_regsh)

## File EF_Driver_Common.h

_C header file for common driver definitions and types._



## Structures and Types

| Type | Name |
| ---: | :--- |
| typedef uint32\_t | [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status)  <br>_A type that is used to return the status of the driver functions._ |


## Macros

| Type | Name |
| ---: | :--- |
| define  | [**EF\_DRIVER\_ERROR**](#define-ef_driver_error)  ((uint32\_t)1)<br>_Unspecified error._ |
| define  | [**EF\_DRIVER\_ERROR\_BUSY**](#define-ef_driver_error_busy)  ((uint32\_t)2)<br>_Driver is busy._ |
| define  | [**EF\_DRIVER\_ERROR\_PARAMETER**](#define-ef_driver_error_parameter)  ((uint32\_t)5)<br>_Parameter error._ |
| define  | [**EF\_DRIVER\_ERROR\_SPECIFIC**](#define-ef_driver_error_specific)  ((uint32\_t)6)<br>_Start of driver specific errors._ |
| define  | [**EF\_DRIVER\_ERROR\_TIMEOUT**](#define-ef_driver_error_timeout)  ((uint32\_t)3)<br>_Timeout occurred._ |
| define  | [**EF\_DRIVER\_ERROR\_UNSUPPORTED**](#define-ef_driver_error_unsupported)  ((uint32\_t)4)<br>_Operation not supported._ |
| define  | [**EF\_DRIVER\_OK**](#define-ef_driver_ok)  ((uint32\_t)0)<br>_Operation succeeded._ |

## Structures and Types Documentation

### typedef `EF_DRIVER_STATUS`

_A type that is used to return the status of the driver functions._
```c
typedef uint32_t EF_DRIVER_STATUS;
```



## Macros Documentation

### define `EF_DRIVER_ERROR`

_Unspecified error._
```c
#define EF_DRIVER_ERROR ((uint32_t)1)
```

### define `EF_DRIVER_ERROR_BUSY`

_Driver is busy._
```c
#define EF_DRIVER_ERROR_BUSY ((uint32_t)2)
```

### define `EF_DRIVER_ERROR_PARAMETER`

_Parameter error._
```c
#define EF_DRIVER_ERROR_PARAMETER ((uint32_t)5)
```

### define `EF_DRIVER_ERROR_SPECIFIC`

_Start of driver specific errors._
```c
#define EF_DRIVER_ERROR_SPECIFIC ((uint32_t)6)
```

### define `EF_DRIVER_ERROR_TIMEOUT`

_Timeout occurred._
```c
#define EF_DRIVER_ERROR_TIMEOUT ((uint32_t)3)
```

### define `EF_DRIVER_ERROR_UNSUPPORTED`

_Operation not supported._
```c
#define EF_DRIVER_ERROR_UNSUPPORTED ((uint32_t)4)
```

### define `EF_DRIVER_OK`

_Operation succeeded._
```c
#define EF_DRIVER_OK ((uint32_t)0)
```


## File EF_I2S.h

_C header file for I2S APIs which contains the function prototypes._




## Functions

| Type | Name |
| ---: | :--- |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_Busy**](#function-ef_i2s_busy) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, bool \*isBusy) <br>_Checks if the I2S peripheral is busy._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_FIFOOverThreshold**](#function-ef_i2s_fifooverthreshold) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, bool \*isOverThreshold) <br>_Checks if the RX FIFO level is over the threshold in the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_RxFIFOAvailable**](#function-ef_i2s_rxfifoavailable) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, bool \*isAvailable) <br>_Checks if the RX FIFO has available space in the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_RxFIFOEmpty**](#function-ef_i2s_rxfifoempty) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, bool \*isEmpty) <br>_Checks if the RX FIFO is empty in the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_RxFIFOFull**](#function-ef_i2s_rxfifofull) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, bool \*isFull) <br>_Checks if the RX FIFO is full in the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_VADFlag**](#function-ef_i2s_vadflag) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, bool \*isOverThreshold) <br>_Checks if the Voice Activity Detector (VAD) flag is set in the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_ZCROverThreshold**](#function-ef_i2s_zcroverthreshold) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, bool \*isOverThreshold) <br>_Checks if the zero-crossing rate exceeds the threshold in the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_clearIrqAVGAboveThreshold**](#function-ef_i2s_clearirqavgabovethreshold) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Clears the average above threshold interrupt for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_clearIrqRxFull**](#function-ef_i2s_clearirqrxfull) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Clears the receive FIFO full interrupt for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_clearIrqRxLevel**](#function-ef_i2s_clearirqrxlevel) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Clears the receive FIFO level interrupt for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_clearIrqRxempty**](#function-ef_i2s_clearirqrxempty) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br> |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_clearIrqVADFlag**](#function-ef_i2s_clearirqvadflag) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Clears the Voice Activity Detector (VAD) flag interrupt for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_clearIrqZCRAboveThreshold**](#function-ef_i2s_clearirqzcrabovethreshold) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Clears the zero-crossing rate above threshold interrupt for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_disable**](#function-ef_i2s_disable) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Disables the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_disableAVG**](#function-ef_i2s_disableavg) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Disables the AVG feature for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_disableFifo**](#function-ef_i2s_disablefifo) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Disables the FIFO feature for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_disableZCR**](#function-ef_i2s_disablezcr) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Disables the ZCR feature for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_enable**](#function-ef_i2s_enable) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Enables the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_enableAVG**](#function-ef_i2s_enableavg) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Enables the AVG feature for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_enableFifo**](#function-ef_i2s_enablefifo) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Enables the FIFO feature for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_enableZCR**](#function-ef_i2s_enablezcr) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s) <br>_Enables the ZCR feature for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_getIM**](#function-ef_i2s_getim) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t \*im\_value) <br>_Reads the Interrupt Mask (IM) register for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_getMIS**](#function-ef_i2s_getmis) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t \*mis\_value) <br>_Reads the Masked Interrupt Status (MIS) register for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_getRIS**](#function-ef_i2s_getris) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t \*ris\_value) <br>_Reads the Raw Interrupt Status (RIS) register for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_getRxFifoLevel**](#function-ef_i2s_getrxfifolevel) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t \*level) <br>_Gets the RX FIFO level of the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_readData**](#function-ef_i2s_readdata) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t \*data) <br>_Reads data from the RX FIFO of the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_setAVGT**](#function-ef_i2s_setavgt) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t average) <br>_Sets the AVGT register for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_setConfigReg**](#function-ef_i2s_setconfigreg) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t config) <br>_Sets the configuration register for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_setGclkEnable**](#function-ef_i2s_setgclkenable) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t value) <br>_Sets the GCLK enable bit in the I2S register to a certain value._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_setIC**](#function-ef_i2s_setic) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t mask) <br>_Writes a value to the Interrupt Clear (IC) register for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_setIM**](#function-ef_i2s_setim) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t mask) <br>_Writes a value to the Interrupt Mask (IM) register for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_setPrescaler**](#function-ef_i2s_setprescaler) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t prescaler) <br>_Sets the prescaler register for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_setRxFifoThreshold**](#function-ef_i2s_setrxfifothreshold) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t threshold) <br>_Sets the RX FIFO threshold for the I2S peripheral._ |
|  [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) | [**EF\_I2S\_setZCRT**](#function-ef_i2s_setzcrt) ([**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) i2s, uint32\_t average) <br>_Sets the ZCRT register for the I2S peripheral._ |

## Macros

| Type | Name |
| ---: | :--- |
| define  | [**EF\_I2S\_AVGT\_REG\_MAX\_VALUE**](#define-ef_i2s_avgt_reg_max_value)  ((uint32\_t)0x0000FFFF)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_MAX\_VALUE**](#define-ef_i2s_cfg_reg_max_value)  ((uint32\_t)0x00000FFF)<br> |
| define  | [**EF\_I2S\_PR\_REG\_MAX\_VALUE**](#define-ef_i2s_pr_reg_max_value)  ((uint32\_t)0x000000FF)<br> |
| define  | [**EF\_I2S\_RX\_FIFO\_IC\_REG\_MAX\_VALUE**](#define-ef_i2s_rx_fifo_ic_reg_max_value)  ((uint32\_t)0x0000003F)<br> |
| define  | [**EF\_I2S\_RX\_FIFO\_IM\_REG\_MAX\_VALUE**](#define-ef_i2s_rx_fifo_im_reg_max_value)  ((uint32\_t)0x0000003F)<br> |
| define  | [**EF\_I2S\_RX\_FIFO\_THRESHOLD\_REG\_MAX\_VALUE**](#define-ef_i2s_rx_fifo_threshold_reg_max_value)  ((uint32\_t)0x0000000F)<br> |
| define  | [**EF\_I2S\_ZCRT\_REG\_MAX\_VALUE**](#define-ef_i2s_zcrt_reg_max_value)  ((uint32\_t)0x0000FFFF)<br> |


## Functions Documentation

### function `EF_I2S_Busy`

_Checks if the I2S peripheral is busy._
```c
EF_DRIVER_STATUS EF_I2S_Busy (
    EF_I2S_TYPE_PTR i2s,
    bool *isBusy
) 
```


This function checks whether the I2S peripheral is currently busy.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `isBusy` Pointer to a boolean variable that will be set to true if the peripheral is busy, or false otherwise.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_FIFOOverThreshold`

_Checks if the RX FIFO level is over the threshold in the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_FIFOOverThreshold (
    EF_I2S_TYPE_PTR i2s,
    bool *isOverThreshold
) 
```


This function checks whether the RX FIFO level has exceeded the threshold in the I2S peripheral.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `isOverThreshold` Pointer to a boolean variable that will be set to true if the RX FIFO level is over the threshold, or false otherwise.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_RxFIFOAvailable`

_Checks if the RX FIFO has available space in the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_RxFIFOAvailable (
    EF_I2S_TYPE_PTR i2s,
    bool *isAvailable
) 
```


This function checks whether the RX FIFO of the I2S peripheral has available space.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `isAvailable` Pointer to a boolean variable that will be set to true if the RX FIFO has available space, or false if it is full.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_RxFIFOEmpty`

_Checks if the RX FIFO is empty in the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_RxFIFOEmpty (
    EF_I2S_TYPE_PTR i2s,
    bool *isEmpty
) 
```


This function checks whether the RX FIFO of the I2S peripheral is empty.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `isEmpty` Pointer to a boolean variable that will be set to true if the RX FIFO is empty, or false otherwise.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_RxFIFOFull`

_Checks if the RX FIFO is full in the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_RxFIFOFull (
    EF_I2S_TYPE_PTR i2s,
    bool *isFull
) 
```


This function checks whether the RX FIFO of the I2S peripheral is full.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `isFull` Pointer to a boolean variable that will be set to true if the RX FIFO is full, or false otherwise.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_VADFlag`

_Checks if the Voice Activity Detector (VAD) flag is set in the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_VADFlag (
    EF_I2S_TYPE_PTR i2s,
    bool *isOverThreshold
) 
```


This function checks whether the Voice Activity Detector (VAD) flag is set in the I2S peripheral.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `isOverThreshold` Pointer to a boolean variable that will be set to true if the VAD flag is set, or false otherwise.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_ZCROverThreshold`

_Checks if the zero-crossing rate exceeds the threshold in the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_ZCROverThreshold (
    EF_I2S_TYPE_PTR i2s,
    bool *isOverThreshold
) 
```


This function checks whether the zero-crossing rate (ZCR) has exceeded the threshold in the I2S peripheral.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `isOverThreshold` Pointer to a boolean variable that will be set to true if the ZCR exceeds the threshold, or false otherwise.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_clearIrqAVGAboveThreshold`

_Clears the average above threshold interrupt for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_clearIrqAVGAboveThreshold (
    EF_I2S_TYPE_PTR i2s
) 
```


This function clears the interrupt corresponding to the average (AVG) being above the threshold in the I2S peripheral by writing to the Interrupt Clear (IC) register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_clearIrqRxFull`

_Clears the receive FIFO full interrupt for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_clearIrqRxFull (
    EF_I2S_TYPE_PTR i2s
) 
```


This function clears the interrupt corresponding to the receive FIFO full condition in the I2S peripheral by writing to the Interrupt Clear (IC) register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_clearIrqRxLevel`

_Clears the receive FIFO level interrupt for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_clearIrqRxLevel (
    EF_I2S_TYPE_PTR i2s
) 
```


This function clears the interrupt corresponding to the receive FIFO level condition in the I2S peripheral by writing to the Interrupt Clear (IC) register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_clearIrqRxempty`

```c
EF_DRIVER_STATUS EF_I2S_clearIrqRxempty (
    EF_I2S_TYPE_PTR i2s
) 
```


This function clears the interrupt corresponding to the receive FIFO empty condition in the I2S peripheral by writing to the Interrupt Clear (IC) register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_clearIrqVADFlag`

_Clears the Voice Activity Detector (VAD) flag interrupt for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_clearIrqVADFlag (
    EF_I2S_TYPE_PTR i2s
) 
```


This function clears the interrupt corresponding to the Voice Activity Detector (VAD) flag in the I2S peripheral by writing to the Interrupt Clear (IC) register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_clearIrqZCRAboveThreshold`

_Clears the zero-crossing rate above threshold interrupt for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_clearIrqZCRAboveThreshold (
    EF_I2S_TYPE_PTR i2s
) 
```


This function clears the interrupt corresponding to the zero-crossing rate (ZCR) being above the threshold in the I2S peripheral by writing to the Interrupt Clear (IC) register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_disable`

_Disables the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_disable (
    EF_I2S_TYPE_PTR i2s
) 
```


This function disables the I2S peripheral by clearing the enable bit in the control register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_disableAVG`

_Disables the AVG feature for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_disableAVG (
    EF_I2S_TYPE_PTR i2s
) 
```


This function disables the AVG feature of the I2S peripheral by clearing the AVG enable bit in the control register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_disableFifo`

_Disables the FIFO feature for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_disableFifo (
    EF_I2S_TYPE_PTR i2s
) 
```


This function disables the FIFO feature of the I2S peripheral by clearing the FIFO enable bit in the control register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_disableZCR`

_Disables the ZCR feature for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_disableZCR (
    EF_I2S_TYPE_PTR i2s
) 
```


This function disables the ZCR feature of the I2S peripheral by clearing the ZCR enable bit in the control register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_enable`

_Enables the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_enable (
    EF_I2S_TYPE_PTR i2s
) 
```


This function enables the I2S peripheral by setting the enable bit in the control register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_enableAVG`

_Enables the AVG feature for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_enableAVG (
    EF_I2S_TYPE_PTR i2s
) 
```


This function enables the AVG feature of the I2S peripheral by setting the AVG enable bit in the control register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_enableFifo`

_Enables the FIFO feature for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_enableFifo (
    EF_I2S_TYPE_PTR i2s
) 
```


This function enables the FIFO feature of the I2S peripheral by setting the FIFO enable bit in the control register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_enableZCR`

_Enables the ZCR feature for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_enableZCR (
    EF_I2S_TYPE_PTR i2s
) 
```


This function enables the ZCR feature of the I2S peripheral by setting the ZCR enable bit in the control register.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_getIM`

_Reads the Interrupt Mask (IM) register for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_getIM (
    EF_I2S_TYPE_PTR i2s,
    uint32_t *im_value
) 
```


This function retrieves the value of the Interrupt Mask (IM) register for the I2S peripheral and stores it in the provided variable. The IM register indicates which interrupts are enabled. RIS Register Breakdown\*\*:

* Bit 0: FIFOE - Receive FIFO is Empty
* Bit 1: FIFOA - FIFO level is above the set level threshold
* Bit 2: FIFOF - Receive FIFO is Full.
* Bit 3: AVGF - The avg is above the threshold.
* Bit 4: ZCRF - The ZCR is above the threshold.
* Bit 5: VADF - The Voice Activity Detector flag; active when both ZCR & AVG flags are active.
* Bits [6-31]: Reserved.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `im_value` Pointer to a variable where the IM register value will be stored.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_getMIS`

_Reads the Masked Interrupt Status (MIS) register for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_getMIS (
    EF_I2S_TYPE_PTR i2s,
    uint32_t *mis_value
) 
```


This function retrieves the value of the Masked Interrupt Status (MIS) register for the I2S peripheral and stores it in the provided variable. The MIS register indicates the current interrupt status after masking. RIS Register Breakdown\*\*:

* Bit 0: FIFOE - Receive FIFO is Empty
* Bit 1: FIFOA - FIFO level is above the set level threshold
* Bit 2: FIFOF - Receive FIFO is Full.
* Bit 3: AVGF - The avg is above the threshold.
* Bit 4: ZCRF - The ZCR is above the threshold.
* Bit 5: VADF - The Voice Activity Detector flag; active when both ZCR & AVG flags are active.
* Bits [6-31]: Reserved.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `mis_value` Pointer to a variable where the MIS register value will be stored.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_getRIS`

_Reads the Raw Interrupt Status (RIS) register for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_getRIS (
    EF_I2S_TYPE_PTR i2s,
    uint32_t *ris_value
) 
```


This function retrieves the value of the Raw Interrupt Status (RIS) register for the I2S peripheral and stores it in the provided variable. The RIS register contains various status flags that indicate the state of the I2S peripheral. RIS Register Breakdown\*\*:

* Bit 0: FIFOE - Receive FIFO is Empty
* Bit 1: FIFOA - FIFO level is above the set level threshold
* Bit 2: FIFOF - Receive FIFO is Full.
* Bit 3: AVGF - The avg is above the threshold.
* Bit 4: ZCRF - The ZCR is above the threshold.
* Bit 5: VADF - The Voice Activity Detector flag; active when both ZCR & AVG flags are active.
* Bits [6-31]: Reserved.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `ris_value` Pointer to a variable where the RIS register value will be stored.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_getRxFifoLevel`

_Gets the RX FIFO level of the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_getRxFifoLevel (
    EF_I2S_TYPE_PTR i2s,
    uint32_t *level
) 
```


This function retrieves the current level of the RX FIFO register from the I2S peripheral and stores it in the memory location pointed to by `level`.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `level` Pointer to a variable where the RX FIFO level will be stored.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_readData`

_Reads data from the RX FIFO of the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_readData (
    EF_I2S_TYPE_PTR i2s,
    uint32_t *data
) 
```


This function retrieves a data word from the RX FIFO of the specified I2S peripheral. It waits until the RX FIFO has data available before performing the read operation. After reading the data, the RX level interrupt is cleared.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `data` Pointer to a variable where the read data will be stored.


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.



**Note:**

The function uses a busy-wait loop to check the RX FIFO status. Ensure proper system design to avoid potential blocking or infinite loops in case of hardware issues.
### function `EF_I2S_setAVGT`

_Sets the AVGT register for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_setAVGT (
    EF_I2S_TYPE_PTR i2s,
    uint32_t average
) 
```


This function sets the average threshold (AVGT) register for the I2S peripheral to the specified value. It ensures that the input pointer and average value are valid.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `average` The average threshold value to be set. Must be less than or equal to [**EF\_I2S\_AVGT\_REG\_MAX\_VALUE**](#define-ef_i2s_avgt_reg_max_value).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_setConfigReg`

_Sets the configuration register for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_setConfigReg (
    EF_I2S_TYPE_PTR i2s,
    uint32_t config
) 
```


This function sets the configuration register of the I2S peripheral to the specified value. It validates the input parameters to ensure the I2S pointer is not NULL and the configuration value is within the allowed range.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `config` The configuration value to be set. Must be less than or equal to [**EF\_I2S\_CFG\_REG\_MAX\_VALUE**](#define-ef_i2s_cfg_reg_max_value).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_setGclkEnable`

_Sets the GCLK enable bit in the I2S register to a certain value._
```c
EF_DRIVER_STATUS EF_I2S_setGclkEnable (
    EF_I2S_TYPE_PTR i2s,
    uint32_t value
) 
```


**Parameters:**


* `i2s` An [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr) , which points to the base memory address of I2S registers.[**EF\_I2S\_TYPE**](#typedef-ef_i2s_type) is a structure that contains the I2S registers.
* `value` The value of the GCLK enable bit


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code
### function `EF_I2S_setIC`

_Writes a value to the Interrupt Clear (IC) register for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_setIC (
    EF_I2S_TYPE_PTR i2s,
    uint32_t mask
) 
```


This function clears specific interrupts in the I2S peripheral by writing to the Interrupt Clear (IC) register. RIS Register Breakdown\*\*:

* Bit 0: FIFOE - Receive FIFO is Empty
* Bit 1: FIFOA - FIFO level is above the set level threshold
* Bit 2: FIFOF - Receive FIFO is Full.
* Bit 3: AVGF - The avg is above the threshold.
* Bit 4: ZCRF - The ZCR is above the threshold.
* Bit 5: VADF - The Voice Activity Detector flag; active when both ZCR & AVG flags are active.
* Bits [6-31]: Reserved.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `mask` The value to be written to the IC register. Must be within the valid range [**EF\_I2S\_RX\_FIFO\_IC\_REG\_MAX\_VALUE**](#define-ef_i2s_rx_fifo_ic_reg_max_value).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_setIM`

_Writes a value to the Interrupt Mask (IM) register for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_setIM (
    EF_I2S_TYPE_PTR i2s,
    uint32_t mask
) 
```


This function sets the value of the Interrupt Mask (IM) register for the I2S peripheral. The IM register determines which interrupts are enabled or disabled. RIS Register Breakdown\*\*:

* Bit 0: FIFOE - Receive FIFO is Empty
* Bit 1: FIFOA - FIFO level is above the set level threshold
* Bit 2: FIFOF - Receive FIFO is Full.
* Bit 3: AVGF - The avg is above the threshold.
* Bit 4: ZCRF - The ZCR is above the threshold.
* Bit 5: VADF - The Voice Activity Detector flag; active when both ZCR & AVG flags are active.
* Bits [6-31]: Reserved.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `mask` The value to be written to the IM register. Must be within the valid range [**EF\_I2S\_RX\_FIFO\_IM\_REG\_MAX\_VALUE**](#define-ef_i2s_rx_fifo_im_reg_max_value).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_setPrescaler`

_Sets the prescaler register for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_setPrescaler (
    EF_I2S_TYPE_PTR i2s,
    uint32_t prescaler
) 
```


This function configures the prescaler register of the I2S peripheral with the specified value. It ensures that the I2S pointer is not NULL and that the prescaler value is within the valid range.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `prescaler` The prescaler value to be set. Must be less than or equal to [**EF\_I2S\_PR\_REG\_MAX\_VALUE**](#define-ef_i2s_pr_reg_max_value).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_setRxFifoThreshold`

_Sets the RX FIFO threshold for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_setRxFifoThreshold (
    EF_I2S_TYPE_PTR i2s,
    uint32_t threshold
) 
```


This function sets the RX FIFO threshold register for the I2S peripheral to the specified value. It ensures that the input pointer and threshold value are valid.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `threshold` The RX FIFO threshold value to be set. Must be less than or equal to [**EF\_I2S\_RX\_FIFO\_THRESHOLD\_REG\_MAX\_VALUE**](#define-ef_i2s_rx_fifo_threshold_reg_max_value).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.
### function `EF_I2S_setZCRT`

_Sets the ZCRT register for the I2S peripheral._
```c
EF_DRIVER_STATUS EF_I2S_setZCRT (
    EF_I2S_TYPE_PTR i2s,
    uint32_t average
) 
```


This function sets the zero-crossing threshold (ZCRT) register for the I2S peripheral to the specified value. It validates the input pointer and the threshold value.



**Parameters:**


* `i2s` Pointer to the I2S base address structure [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr).
* `average` The zero-crossing threshold value to be set. Must be less than or equal to [**EF\_I2S\_ZCRT\_REG\_MAX\_VALUE**](#define-ef_i2s_zcrt_reg_max_value).


**Returns:**

status A value of type [**EF\_DRIVER\_STATUS**](#typedef-ef_driver_status) : returns a success or error code.

## Macros Documentation

### define `EF_I2S_AVGT_REG_MAX_VALUE`

```c
#define EF_I2S_AVGT_REG_MAX_VALUE ((uint32_t)0x0000FFFF)
```

### define `EF_I2S_CFG_REG_MAX_VALUE`

```c
#define EF_I2S_CFG_REG_MAX_VALUE ((uint32_t)0x00000FFF)
```

### define `EF_I2S_PR_REG_MAX_VALUE`

```c
#define EF_I2S_PR_REG_MAX_VALUE ((uint32_t)0x000000FF)
```

### define `EF_I2S_RX_FIFO_IC_REG_MAX_VALUE`

```c
#define EF_I2S_RX_FIFO_IC_REG_MAX_VALUE ((uint32_t)0x0000003F)
```

### define `EF_I2S_RX_FIFO_IM_REG_MAX_VALUE`

```c
#define EF_I2S_RX_FIFO_IM_REG_MAX_VALUE ((uint32_t)0x0000003F)
```

### define `EF_I2S_RX_FIFO_THRESHOLD_REG_MAX_VALUE`

```c
#define EF_I2S_RX_FIFO_THRESHOLD_REG_MAX_VALUE ((uint32_t)0x0000000F)
```

### define `EF_I2S_ZCRT_REG_MAX_VALUE`

```c
#define EF_I2S_ZCRT_REG_MAX_VALUE ((uint32_t)0x0000FFFF)
```


## File EF_I2S_regs.h





## Structures and Types

| Type | Name |
| ---: | :--- |
| typedef struct [**\_EF\_I2S\_TYPE\_**](#struct-_ef_i2s_type_) | [**EF\_I2S\_TYPE**](#typedef-ef_i2s_type)  <br> |
| typedef [**EF\_I2S\_TYPE**](#typedef-ef_i2s_type) \* | [**EF\_I2S\_TYPE\_PTR**](#typedef-ef_i2s_type_ptr)  <br> |
| struct | [**\_EF\_I2S\_TYPE\_**](#struct-_ef_i2s_type_) <br> |


## Macros

| Type | Name |
| ---: | :--- |
| define  | [**EF\_I2S\_AVGF\_FLAG**](#define-ef_i2s_avgf_flag)  ((uint32\_t)0x8)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_AVGSEL\_BIT**](#define-ef_i2s_cfg_reg_avgsel_bit)  ((uint32\_t)10)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_AVGSEL\_MASK**](#define-ef_i2s_cfg_reg_avgsel_mask)  ((uint32\_t)0x400)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_CHANNELS\_BIT**](#define-ef_i2s_cfg_reg_channels_bit)  ((uint32\_t)0)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_CHANNELS\_MASK**](#define-ef_i2s_cfg_reg_channels_mask)  ((uint32\_t)0x3)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_LEFT\_JUSTIFIED\_BIT**](#define-ef_i2s_cfg_reg_left_justified_bit)  ((uint32\_t)3)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_LEFT\_JUSTIFIED\_MASK**](#define-ef_i2s_cfg_reg_left_justified_mask)  ((uint32\_t)0x8)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_SAMPLE\_SIZE\_BIT**](#define-ef_i2s_cfg_reg_sample_size_bit)  ((uint32\_t)4)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_SAMPLE\_SIZE\_MASK**](#define-ef_i2s_cfg_reg_sample_size_mask)  ((uint32\_t)0x3f0)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_SIGN\_EXTEND\_BIT**](#define-ef_i2s_cfg_reg_sign_extend_bit)  ((uint32\_t)2)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_SIGN\_EXTEND\_MASK**](#define-ef_i2s_cfg_reg_sign_extend_mask)  ((uint32\_t)0x4)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_ZCRSEL\_BIT**](#define-ef_i2s_cfg_reg_zcrsel_bit)  ((uint32\_t)11)<br> |
| define  | [**EF\_I2S\_CFG\_REG\_ZCRSEL\_MASK**](#define-ef_i2s_cfg_reg_zcrsel_mask)  ((uint32\_t)0x800)<br> |
| define  | [**EF\_I2S\_CTRL\_REG\_AVG\_EN\_BIT**](#define-ef_i2s_ctrl_reg_avg_en_bit)  ((uint32\_t)2)<br> |
| define  | [**EF\_I2S\_CTRL\_REG\_AVG\_EN\_MASK**](#define-ef_i2s_ctrl_reg_avg_en_mask)  ((uint32\_t)0x4)<br> |
| define  | [**EF\_I2S\_CTRL\_REG\_EN\_BIT**](#define-ef_i2s_ctrl_reg_en_bit)  ((uint32\_t)0)<br> |
| define  | [**EF\_I2S\_CTRL\_REG\_EN\_MASK**](#define-ef_i2s_ctrl_reg_en_mask)  ((uint32\_t)0x1)<br> |
| define  | [**EF\_I2S\_CTRL\_REG\_FIFO\_EN\_BIT**](#define-ef_i2s_ctrl_reg_fifo_en_bit)  ((uint32\_t)1)<br> |
| define  | [**EF\_I2S\_CTRL\_REG\_FIFO\_EN\_MASK**](#define-ef_i2s_ctrl_reg_fifo_en_mask)  ((uint32\_t)0x2)<br> |
| define  | [**EF\_I2S\_CTRL\_REG\_ZCR\_EN\_BIT**](#define-ef_i2s_ctrl_reg_zcr_en_bit)  ((uint32\_t)3)<br> |
| define  | [**EF\_I2S\_CTRL\_REG\_ZCR\_EN\_MASK**](#define-ef_i2s_ctrl_reg_zcr_en_mask)  ((uint32\_t)0x8)<br> |
| define  | [**EF\_I2S\_FIFOA\_FLAG**](#define-ef_i2s_fifoa_flag)  ((uint32\_t)0x2)<br> |
| define  | [**EF\_I2S\_FIFOE\_FLAG**](#define-ef_i2s_fifoe_flag)  ((uint32\_t)0x1)<br> |
| define  | [**EF\_I2S\_FIFOF\_FLAG**](#define-ef_i2s_fifof_flag)  ((uint32\_t)0x4)<br> |
| define  | [**EF\_I2S\_RX\_FIFO\_FLUSH\_REG\_FLUSH\_BIT**](#define-ef_i2s_rx_fifo_flush_reg_flush_bit)  ((uint32\_t)0)<br> |
| define  | [**EF\_I2S\_RX\_FIFO\_FLUSH\_REG\_FLUSH\_MASK**](#define-ef_i2s_rx_fifo_flush_reg_flush_mask)  ((uint32\_t)0x1)<br> |
| define  | [**EF\_I2S\_RX\_FIFO\_LEVEL\_REG\_LEVEL\_BIT**](#define-ef_i2s_rx_fifo_level_reg_level_bit)  ((uint32\_t)0)<br> |
| define  | [**EF\_I2S\_RX\_FIFO\_LEVEL\_REG\_LEVEL\_MASK**](#define-ef_i2s_rx_fifo_level_reg_level_mask)  ((uint32\_t)0xf)<br> |
| define  | [**EF\_I2S\_RX\_FIFO\_THRESHOLD\_REG\_THRESHOLD\_BIT**](#define-ef_i2s_rx_fifo_threshold_reg_threshold_bit)  ((uint32\_t)0)<br> |
| define  | [**EF\_I2S\_RX\_FIFO\_THRESHOLD\_REG\_THRESHOLD\_MASK**](#define-ef_i2s_rx_fifo_threshold_reg_threshold_mask)  ((uint32\_t)0xf)<br> |
| define  | [**EF\_I2S\_VADF\_FLAG**](#define-ef_i2s_vadf_flag)  ((uint32\_t)0x20)<br> |
| define  | [**EF\_I2S\_ZCRF\_FLAG**](#define-ef_i2s_zcrf_flag)  ((uint32\_t)0x10)<br> |
| define  | [**IO\_TYPES**](#define-io_types)  <br> |
| define  | [**\_\_R**](#define-__r)  volatile const uint32\_t<br> |
| define  | [**\_\_RW**](#define-__rw)  volatile       uint32\_t<br> |
| define  | [**\_\_W**](#define-__w)  volatile       uint32\_t<br> |

## Structures and Types Documentation

### typedef `EF_I2S_TYPE`

```c
typedef struct _EF_I2S_TYPE_ EF_I2S_TYPE;
```

### typedef `EF_I2S_TYPE_PTR`

```c
typedef EF_I2S_TYPE* EF_I2S_TYPE_PTR;
```

### struct `_EF_I2S_TYPE_`


Variables:

-  [**\_\_W**](#define-__w) AVGT  

-  [**\_\_W**](#define-__w) CFG  

-  [**\_\_W**](#define-__w) CTRL  

-  [**\_\_W**](#define-__w) GCLK  

-  [**\_\_W**](#define-__w) IC  

-  [**\_\_RW**](#define-__rw) IM  

-  [**\_\_R**](#define-__r) MIS  

-  [**\_\_W**](#define-__w) PR  

-  [**\_\_R**](#define-__r) RIS  

-  [**\_\_R**](#define-__r) RXDATA  

-  [**\_\_W**](#define-__w) RX_FIFO_FLUSH  

-  [**\_\_R**](#define-__r) RX_FIFO_LEVEL  

-  [**\_\_W**](#define-__w) RX_FIFO_THRESHOLD  

-  [**\_\_W**](#define-__w) ZCRT  

-  [**\_\_R**](#define-__r) reserved_0  

-  [**\_\_R**](#define-__r) reserved_1  



## Macros Documentation

### define `EF_I2S_AVGF_FLAG`

```c
#define EF_I2S_AVGF_FLAG ((uint32_t)0x8)
```

### define `EF_I2S_CFG_REG_AVGSEL_BIT`

```c
#define EF_I2S_CFG_REG_AVGSEL_BIT ((uint32_t)10)
```

### define `EF_I2S_CFG_REG_AVGSEL_MASK`

```c
#define EF_I2S_CFG_REG_AVGSEL_MASK ((uint32_t)0x400)
```

### define `EF_I2S_CFG_REG_CHANNELS_BIT`

```c
#define EF_I2S_CFG_REG_CHANNELS_BIT ((uint32_t)0)
```

### define `EF_I2S_CFG_REG_CHANNELS_MASK`

```c
#define EF_I2S_CFG_REG_CHANNELS_MASK ((uint32_t)0x3)
```

### define `EF_I2S_CFG_REG_LEFT_JUSTIFIED_BIT`

```c
#define EF_I2S_CFG_REG_LEFT_JUSTIFIED_BIT ((uint32_t)3)
```

### define `EF_I2S_CFG_REG_LEFT_JUSTIFIED_MASK`

```c
#define EF_I2S_CFG_REG_LEFT_JUSTIFIED_MASK ((uint32_t)0x8)
```

### define `EF_I2S_CFG_REG_SAMPLE_SIZE_BIT`

```c
#define EF_I2S_CFG_REG_SAMPLE_SIZE_BIT ((uint32_t)4)
```

### define `EF_I2S_CFG_REG_SAMPLE_SIZE_MASK`

```c
#define EF_I2S_CFG_REG_SAMPLE_SIZE_MASK ((uint32_t)0x3f0)
```

### define `EF_I2S_CFG_REG_SIGN_EXTEND_BIT`

```c
#define EF_I2S_CFG_REG_SIGN_EXTEND_BIT ((uint32_t)2)
```

### define `EF_I2S_CFG_REG_SIGN_EXTEND_MASK`

```c
#define EF_I2S_CFG_REG_SIGN_EXTEND_MASK ((uint32_t)0x4)
```

### define `EF_I2S_CFG_REG_ZCRSEL_BIT`

```c
#define EF_I2S_CFG_REG_ZCRSEL_BIT ((uint32_t)11)
```

### define `EF_I2S_CFG_REG_ZCRSEL_MASK`

```c
#define EF_I2S_CFG_REG_ZCRSEL_MASK ((uint32_t)0x800)
```

### define `EF_I2S_CTRL_REG_AVG_EN_BIT`

```c
#define EF_I2S_CTRL_REG_AVG_EN_BIT ((uint32_t)2)
```

### define `EF_I2S_CTRL_REG_AVG_EN_MASK`

```c
#define EF_I2S_CTRL_REG_AVG_EN_MASK ((uint32_t)0x4)
```

### define `EF_I2S_CTRL_REG_EN_BIT`

```c
#define EF_I2S_CTRL_REG_EN_BIT ((uint32_t)0)
```

### define `EF_I2S_CTRL_REG_EN_MASK`

```c
#define EF_I2S_CTRL_REG_EN_MASK ((uint32_t)0x1)
```

### define `EF_I2S_CTRL_REG_FIFO_EN_BIT`

```c
#define EF_I2S_CTRL_REG_FIFO_EN_BIT ((uint32_t)1)
```

### define `EF_I2S_CTRL_REG_FIFO_EN_MASK`

```c
#define EF_I2S_CTRL_REG_FIFO_EN_MASK ((uint32_t)0x2)
```

### define `EF_I2S_CTRL_REG_ZCR_EN_BIT`

```c
#define EF_I2S_CTRL_REG_ZCR_EN_BIT ((uint32_t)3)
```

### define `EF_I2S_CTRL_REG_ZCR_EN_MASK`

```c
#define EF_I2S_CTRL_REG_ZCR_EN_MASK ((uint32_t)0x8)
```

### define `EF_I2S_FIFOA_FLAG`

```c
#define EF_I2S_FIFOA_FLAG ((uint32_t)0x2)
```

### define `EF_I2S_FIFOE_FLAG`

```c
#define EF_I2S_FIFOE_FLAG ((uint32_t)0x1)
```

### define `EF_I2S_FIFOF_FLAG`

```c
#define EF_I2S_FIFOF_FLAG ((uint32_t)0x4)
```

### define `EF_I2S_RX_FIFO_FLUSH_REG_FLUSH_BIT`

```c
#define EF_I2S_RX_FIFO_FLUSH_REG_FLUSH_BIT ((uint32_t)0)
```

### define `EF_I2S_RX_FIFO_FLUSH_REG_FLUSH_MASK`

```c
#define EF_I2S_RX_FIFO_FLUSH_REG_FLUSH_MASK ((uint32_t)0x1)
```

### define `EF_I2S_RX_FIFO_LEVEL_REG_LEVEL_BIT`

```c
#define EF_I2S_RX_FIFO_LEVEL_REG_LEVEL_BIT ((uint32_t)0)
```

### define `EF_I2S_RX_FIFO_LEVEL_REG_LEVEL_MASK`

```c
#define EF_I2S_RX_FIFO_LEVEL_REG_LEVEL_MASK ((uint32_t)0xf)
```

### define `EF_I2S_RX_FIFO_THRESHOLD_REG_THRESHOLD_BIT`

```c
#define EF_I2S_RX_FIFO_THRESHOLD_REG_THRESHOLD_BIT ((uint32_t)0)
```

### define `EF_I2S_RX_FIFO_THRESHOLD_REG_THRESHOLD_MASK`

```c
#define EF_I2S_RX_FIFO_THRESHOLD_REG_THRESHOLD_MASK ((uint32_t)0xf)
```

### define `EF_I2S_VADF_FLAG`

```c
#define EF_I2S_VADF_FLAG ((uint32_t)0x20)
```

### define `EF_I2S_ZCRF_FLAG`

```c
#define EF_I2S_ZCRF_FLAG ((uint32_t)0x10)
```

### define `IO_TYPES`

```c
#define IO_TYPES 
```

### define `__R`

```c
#define __R volatile const uint32_t
```

### define `__RW`

```c
#define __RW volatile       uint32_t
```

### define `__W`

```c
#define __W volatile       uint32_t
```


