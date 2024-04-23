def nrz_i(bits_sequence):
    nrz_i_bits = []
    prev_bit = 1
    for bit in bits_sequence:
        # If bit is 1 invert the previous bit if is 0 keep the same level
        if bit == 1:
            prev_bit = 1 - prev_bit
        
        if prev_bit == 0:
            nrz_i_bits.append(-1)
        else:
            nrz_i_bits.append(prev_bit)

    return nrz_i_bits

def ami(bits_sequence):
    ami_bits = []
    positive_wave = True

    for bit in bits_sequence:
        if bit == 0:
            ami_bits.append(0)
        else:
            if positive_wave:
                ami_bits.append(1)
                positive_wave = False
            else:
                ami_bits.append(-1)
                positive_wave = True

    return ami_bits

def pseudoternary(bits_sequence):
    pseudoternary_bits = []
    positive_wave = True

    for bit in bits_sequence:
        if bit == 1:
            pseudoternary_bits.append(0)
        else:
            if positive_wave:
                pseudoternary_bits.append(1)
                positive_wave = False
            else:
                pseudoternary_bits.append(-1)
                positive_wave = True

    return pseudoternary_bits


def manchester(bits_sequence):
    manchester_bits = []

    for bit in bits_sequence:
        if bit == 0:
            manchester_bits.extend([1, -1])
        else:
            manchester_bits.extend([-1, 1])

    return manchester_bits

def d_manchester(bits_sequence):
    d_manchester_bits = []
    prev_bit = [-1, 1]

    for bit in bits_sequence:
        if bit == 0:
            d_manchester_bits.extend(prev_bit)
        else:
            prev_bit = prev_bit[::-1]
            d_manchester_bits.extend(prev_bit)

    return d_manchester_bits