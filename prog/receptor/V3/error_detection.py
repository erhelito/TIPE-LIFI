def clean_signal(bits, bit_duration):
    output = rmv_first_zeros(bits, bit_duration)
    output = filtering(output, bit_duration)
    output = rmv_last_zeros(output)

    output = output[1:-1]

    print("clean_signal")
    print(output)

    return output

def rmv_first_zeros(bits, bit_duration):
    init = True

    while init :
        while bits[0] == 0:
            bits.pop(0)

        mean = round(sum(bits[:bit_duration])/bit_duration)

        if mean == 1:
            init = False

        else:
            bits.pop(0)

    return bits

def filtering(bits, bit_duration):
    n = len(bits)
    groups = [bits[i:i+bit_duration] for i in range(0, n, bit_duration)]
    output = []

    for group in groups:
        mean = round(sum(group)/bit_duration)
        output.append(mean)

    return output

def fintering2(bits, bit_duration):
    n = len(bits)
    groups = [bits[i:i+bit_duration] for i in range(0, n, bit_duration)]
    output = []

    for group in groups:
        mean = round(sum(group[1:-1])/(bit_duration-2))
        output.append(mean)

    return output

def rmv_last_zeros(bits):
    while bits[-1] == 0:
      bits.pop(-1)

    return bits