from machine import Pin, ADC # type: ignore
import knn
import error_detection
import convertors
import hamming
from time import sleep

photo = ADC(Pin(26))
base = ADC(Pin(27))
switch = Pin(0, Pin.IN)

f_emit = 7
bit_duration = 3
f_recep = f_emit*bit_duration

data = []

print("waiting")

while switch.value() == 0:
    pass

print("rec")

while switch.value() == 1:
    data.append([photo.read_u16(), base.read_u16()])
    sleep(1/f_recep)

print("done")
print(data)

centers = [[min(point[0] for point in data), min(point[1] for point in data)],[max(point[0] for point in data), max(point[1] for point in data)]]

centers, labels = knn.k_means(data, centers, n = 100)

bits = error_detection.clean_signal(labels, bit_duration)

bits = convertors.list_to_str(bits)

### sans hamming
message = convertors.binary_to_text(bits)

### avec hamming
hamminged_message = hamming.hamming_decode(bits)

message = convertors.binary_to_text(hamminged_message)


print(message)