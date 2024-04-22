def nrz_i(bits_sequence):
    nrz_i_bits = []
    prev_bit = 1
    for bit in bits_sequence:
        # If bit is 1 invert the previous bit if is 0 keep the same level
        if bit == 1:
            prev_bit = 1 - prev_bit
            nrz_i_bits.append(prev_bit)
        else:
            nrz_i_bits.append(prev_bit)

    return nrz_i_bits