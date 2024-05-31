import pandas as pd

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

def _8B6T(bits_sequence):
    if len(bits_sequence) % 8 != 0:
        raise ValueError("The sequence must have a multiple of 8 bits")
    
    _8B6T_sequence = []
    outputs = ""
    weight = 0

    bits_sequence = "".join([str(bit) for bit in bits_sequence])

    # Turn the bits sequence into a hex code and load the table
    hex_codes = hex(int(bits_sequence, 2))[2:]
    df = pd.read_csv("8B6T_table.csv")
    
    # Split the hex code into pairs of two
    hex_codes = [hex_codes[i:i+2] for i in range(0, len(hex_codes), 2)]
    invert = False

    for hex_code in hex_codes:
        # look for the hex code in the table to define the output
        output = df.loc[df["hex_code"] == hex_code, "bits_sequence"].values[0]
        outputs = "".join([outputs, output])
        for id, bit in enumerate(output):
            # Every 8 bits invert the output if the weight is different from 0
            if id % 8 == 0:
                if weight != 0:
                    invert = True
                else:
                    invert = False

            if bit == "0":
                _8B6T_sequence.append(0)
            elif (bit == "+" and not invert) or (bit == "-" and invert):
                _8B6T_sequence.append(1)
                weight += 1
            elif (bit == "-" and not invert) or (bit == "+" and invert):
                _8B6T_sequence.append(-1)
                weight -= 1

    
    return _8B6T_sequence, outputs

def mlt_3(bits_sequence):
    mlt_3_bits = []
    positive_wave = True
    current_wave = 0

    for bit in bits_sequence:
        if bit == 1:
            if positive_wave:
                current_wave += 1

                # If the current wave is 1 change the wave to negative
                if current_wave == 1:
                    positive_wave = False
            else:
                current_wave -= 1
                # If the current wave is -1 change the wave to positive
                if current_wave == -1:
                    positive_wave = True

            mlt_3_bits.append(current_wave)
        else:
            mlt_3_bits.append(current_wave)

    return mlt_3_bits

def _4D_PAM5(bits_sequence):
    if len(bits_sequence) % 2 != 0:
        raise ValueError("The sequence must have an even number of bits")
    
    _4D_PAM5_sequence = []
    # Split the sequence into pairs
    bits_pairs = [bits_sequence[i:i+2] for i in range(0, len(bits_sequence), 2)]
    bits_pairs = ["".join([str(bit) for bit in pair]) for pair in bits_pairs]

    # Create a list with unique pairs for the encoding
    unique_pairs = list(set(bits_pairs))

    # Exclude 0 because it's only for error detection
    levels = [-2, -1, 1, 2]

    # Create a dictionary with the encoding
    encoding = {}
    for pair in unique_pairs:
        encoding[pair] = levels.pop()
    
    # Create the 4D-PAM5 sequence
    for pair in bits_pairs:
        _4D_PAM5_sequence.append(encoding[pair])

    return _4D_PAM5_sequence


    
