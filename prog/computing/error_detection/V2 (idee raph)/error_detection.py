"""
new idea
only works for bit_duration > 3
2 "security" bits
"""

bits = []

# emission frequency
f_emit = 3
# reception frequency
f_recv = 9

bit_duration = int(f_recv/f_emit)
n = len(bits)

# remove leading zeros
init = True

while init :
    while bits[0] == 0:
        bits.pop(0)

    mean = round(sum(bits[:bit_duration])/bit_duration)

    if mean == 1:
        init = False

    else:
        bits.pop(0)

# decode the signal
groups = [bits[i:i+bit_duration] for i in range(0, n, bit_duration)]
output = []

for group in groups:
    mean = round(sum(group[1:-1])/(bit_duration-2))
    output.append(mean)

# remove the last zeros
while output[-1] == 0:
    output.pop(-1)