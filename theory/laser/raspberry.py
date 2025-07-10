from machine import Pin, ADC # type: ignore
from time import sleep

photo = ADC(Pin(26))

while True:
    print(photo.read_u16())
    sleep(0.5)
