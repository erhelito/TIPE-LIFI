from time import sleep
from machine import Pin, PWM # type: ignore
from math import cos, pi

def power(high=True) -> None:
    """Simply turn on/off the builtin led"""
    led = Pin('LED', Pin.OUT)
    if high: led.high()
    else: led.low()

def laser_on(high=True) -> None:
    """Simply turn on/off the laser"""
    laser = Pin(16, Pin.OUT)
    if high: laser.high()
    else: laser.low()

def visualize(value, min=0, max=1) -> None:
    """Visualize a value between a min/max value, thanks to the builtin led.
    Default: min=0, max=1"""

    led = PWM(Pin('LED', Pin.OUT))
    led.freq(1000)
    
    value = (value-min)/(max-min) # % value
    value = int(value*65535) # convert to PWM
    led.duty_u16(value)

def freq(f) :
    for i in range(3*f):
        led = Pin(16, Pin.OUT)
        led.value(1)
        sleep(1/(2*f))
        led.value(0)
        sleep(1/(2*f))

def test_pwm(value):
    #50000 - 65535
    led = PWM(Pin(16, Pin.OUT))
    led.freq(1000)

    led.duty_u16(value)

def sine():    
    led = PWM(Pin(16, Pin.OUT))
    led.freq(1000)

    list = [cos(x*pi/180) for x in range(0,360)]
    list = [int(x*(65535-50000)+50000) for x in list]
    print(list)

    for i in list:
        led.duty_u16(i)
        sleep(0.01)

def ramp():
    led = PWM(Pin(16, Pin.OUT))
    led.freq(1000)

    for i in range(50000,65535):
        led.duty_u16(i)
        sleep(0.1)

    for i in range(65535,50000,-1):
        led.duty_u16(i)
        sleep(0.1)