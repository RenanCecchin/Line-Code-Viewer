import matplotlib.pyplot as plt

def plot_line_code(bits_sequence):
    fig, ax = plt.subplots()
    ax.stairs(bits_sequence, color="red")
    ax.set(xlim = (0.1, len(bits_sequence)), ylim = (0, 3))
    ax.vlines(range(0, len(bits_sequence)), 0, 3, color="green", linestyles = "dotted")
    ax.axis("off")
    return fig