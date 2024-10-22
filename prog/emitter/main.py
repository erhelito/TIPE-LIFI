from machine import Pin, PWM, ADC # type: ignore
from math import cos, pi
from time import sleep
from modules import *

photo = ADC(Pin(26))

f=10

while True :
    led = Pin(16, Pin.OUT)
    led.value(1)
    print(photo.read_u16())
    sleep(1/(2*f))
    led.value(0)
    print(photo.read_u16())
    sleep(1/(2*f))