from machine import Pin, PWM, ADC # type: ignore

# values from 0 to 65535
value = 0
E = PWM(Pin(16, Pin.OUT))
E.freq(1000)
E.duty_u16(value)