import streamlit as st
from utils import plot_line_code
import line_codes

if __name__ == "__main__":
    line_code = st.selectbox("Selecione o código de linha", ["NRZ-L", "NRZ-I", "AMI", "Pseudoternário", "Manchester", "Manchester Diferencial"])
    bits_sequence = st.text_input("Digite a sequência de bits e confirme com Enter")
    bits_sequence = [int(bit) for bit in bits_sequence]

    if bits_sequence:
        match line_code:
            case "NRZ-L":
                offset = 2
                # Turn all the 0 to -1
                nrz_l_bits = [-1 if bit == 0 else bit for bit in bits_sequence]

                nrz_l_bits = [bit + offset for bit in nrz_l_bits]

                st.text("".join([str(bit) for bit in bits_sequence]))
                st.pyplot(plot_line_code(nrz_l_bits, offset = offset))
            case "NRZ-I":
                offset = 2
                nrz_i_bits = line_codes.nrz_i(bits_sequence)
                st.text("".join([str(bit) for bit in nrz_i_bits]))

                # Add offset to each bit to plot the bits correctly
                nrz_i_bits = [bit + offset for bit in nrz_i_bits]

                st.pyplot(plot_line_code(nrz_i_bits, offset = offset))
            case "AMI":
                offset = 2
                ami_bits = line_codes.ami(bits_sequence)
                st.text("".join([str(bit) for bit in ami_bits]))

                # Add offset to each bit to plot the bits correctly
                ami_bits = [bit + offset for bit in ami_bits]

                st.pyplot(plot_line_code(ami_bits, offset = offset))
            case "Pseudoternário":
                offset = 2
                pseudoternary_bits = line_codes.pseudoternary(bits_sequence)
                st.text("".join([str(bit) for bit in pseudoternary_bits]))
                
                # Add offset to each bit to plot the bits correctly
                pseudoternary_bits = [bit + offset for bit in pseudoternary_bits]

                st.pyplot(plot_line_code(pseudoternary_bits, offset = offset))
            case "Manchester":
                offset = 2
                manchester_bits = line_codes.manchester(bits_sequence)
                st.text("".join([str(bit) for bit in manchester_bits]))
                
                # Add offset to each bit to plot the bits correctly
                manchester_bits = [bit + offset for bit in manchester_bits]

                st.pyplot(plot_line_code(manchester_bits, offset = offset, line_offset = 2))
            case "Manchester Diferencial":
                offset = 2
                d_manchester_bits = line_codes.d_manchester(bits_sequence)
                st.text("".join([str(bit) for bit in d_manchester_bits]))
                
                # Add offset to each bit to plot the bits correctly
                d_manchester_bits = [bit + offset for bit in d_manchester_bits]

                st.pyplot(plot_line_code(d_manchester_bits, offset = offset, line_offset = 2))

