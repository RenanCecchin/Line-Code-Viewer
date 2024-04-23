import matplotlib.pyplot as plt

def plot_line_code(bits_sequence, offset = 1, line_offset = 1):
    fig, ax = plt.subplots()
    ax.stairs(bits_sequence, color="red")
    height = 5
    ax.set(xlim = (0.1, len(bits_sequence) - 0.1), ylim = (0, height))
    ax.hlines(offset, 0, len(bits_sequence), color = "blue", linestyles = "dotted")
    ax.vlines(range(0, len(bits_sequence), line_offset), 0, height, color="green", linestyles = "dotted")
    ax.axis("off")
    return fig