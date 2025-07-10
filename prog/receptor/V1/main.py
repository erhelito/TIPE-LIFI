from machine import Pin, PWM, ADC # type: ignore
from convertors import *
from tools import *
from time import ticks_ms, sleep


photo = ADC(Pin(26))
base = ADC(Pin(27))

state = "0"
bits = ""
n = 35

f = 10
T = 1/f
time_treshold = T/2
sensor_treshold = 100


wait = True

while wait :
    t = ticks_ms() # temps en milli secondes
    while binary(photo, base, sensor_treshold) :
        print(binary(photo,base,sensor_treshold))

        if (ticks_ms() - t)/1000 > time_treshold:
            wait = False
            break

sleep(T/2)

t = ticks_ms() # temps en milli secondes

while len(bits) < n:
    print(1)
    while binary(photo, base, sensor_treshold) :
        print(2, ticks_ms() - t, bits)

        if (ticks_ms() - t)/1000 > time_treshold:
            state = "1"
            bits += state
            t = ticks_ms()
            print(bits)
            break

        sleep(T/2)

    while not binary(photo, base, sensor_treshold) :
        print(3, ticks_ms() - t, bits)

        if (ticks_ms() - t)/1000 > time_treshold:
            state = "0"
            bits += state
            t = ticks_ms()
            print(bits)
            break

        sleep(T/2)

text = binary_to_text(bits)
print(text)