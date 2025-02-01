from machine import Pin, ADC # type: ignore
from modules import *
from time import sleep

photo = ADC(Pin(26))
base = ADC(Pin(27))

f = 15

while True :
    print(photo.read_u16(),",", base.read_u16())
    sleep(1/f)