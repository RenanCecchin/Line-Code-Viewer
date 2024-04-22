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
                nrz_l_bits = [bit + 1 for bit in bits_sequence]

                st.text("".join([str(bit) for bit in bits_sequence]))
                st.pyplot(plot_line_code(nrz_l_bits))
            case "NRZ-I":
                nrz_i_bits = line_codes.nrz_i(bits_sequence)
                st.text("".join([str(bit) for bit in nrz_i_bits]))
                # Add 1 to each bit to plot the bits correctly
                nrz_i_bits = [bit + 1 for bit in nrz_i_bits]
                st.pyplot(plot_line_code(nrz_i_bits))
            case "AMI":
                st.write("AMI")
            case "Pseudoternário":
                st.write("Pseudoternário")
            case "Manchester":
                st.write("Manchester")
            case "Manchester Diferencial":
                st.write("Manchester Diferencial")

