import numpy as np
import matplotlib.pyplot as plt
import mplcursors
import math

wp = 0.2 * np.pi
ws = 0.3 * np.pi

delta_w = ws - wp

M = 4 * np.pi / delta_w - 1 # Rectanular window

M = math.ceil(M)

wc = (wp + ws) / 2

n = np.linspace(0, M, M + 1)

no = M / 2

hd = np.zeros(len(n))

wn = np.zeros(len(n))

for i in range(len(n)):
    if no != n[i]:
        hd[i] = np.sin(wc * (n[i] - no)) / (np.pi * (n[i] - no))

    else:
        hd[i] = wc / np.pi

    wn[i] = 1

h = hd * wn


def plot_filter_response(frequency_response):
    """
    Plot the amplitude and amplitude in dB of a digital filter.

    Parameters:
    frequency_response (callable): Frequency response of the digital filter.
        It should take a single argument, w, and return the complex response.
    """
    w = np.linspace(0, 1, 1001)  # Frequency axis

    # Evaluate the transfer function
    response = np.array([frequency_response(wi * np.pi) for wi in w])

    # Calculate amplitude and amplitude in dB
    amplitude = np.abs(response)
    amplitude_db = 20 * np.log10(np.maximum(amplitude, 1e-12))  # Prevent log10 from taking too small numbers

    phase = np.angle(response)

    # Create the plot
    fig, ax = plt.subplots(2, 2, figsize=(8, 6))

    ax[0][0].plot(n, h, ".")
    ax[0][0].set_title(f"Impulse Response. M = {M}. Rectangular Window")
    ax[0][0].set_xlabel("n")
    ax[0][0].set_ylabel("h[n]")
    ax[0][0].grid(True)

    ax[0][1].plot(w, amplitude_db, "-")
    ax[0][1].set_title("Amplitude Response (dB)")
    ax[0][1].set_xlabel("ω (π rad)")
    ax[0][1].set_ylabel("20Log|H(e^jω)| (dB)")
    ax[0][1].grid(True)
    ax[0][1].set_ylim(bottom=-100)

    ax[1][0].plot(w, amplitude, "-")
    ax[1][0].set_title("Amplitude Response")
    ax[1][0].set_xlabel("ω (π rad)")
    ax[1][0].set_ylabel("H(e^jω)")
    ax[1][0].grid(True)

    ax[1][1].plot(w, phase, "-")
    ax[1][1].set_title("Phase Response")
    ax[1][1].set_xlabel("ω (π rad)")
    ax[1][1].set_ylabel("/_H(e^jω) (rad)")
    ax[1][1].grid(True)

    mplcursors.cursor(ax[0][0], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"n={sel.target[0]}, h[n]={sel.target[1]:.5f}"))
    mplcursors.cursor(ax[0][1], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"ω={sel.target[0]:.5f}π, 20Log|H(e^jω)|={sel.target[1]:.5f}dB"))
    mplcursors.cursor(ax[1][0], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"ω={sel.target[0]:.5f}π, H(e^jω)={sel.target[1]:.5f}"))
    mplcursors.cursor(ax[1][1], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"ω={sel.target[0]:.5f}π, /_H(e^jω)={sel.target[1]:.5f}rad"))

    plt.tight_layout()
    plt.show()


# Example usage:
def LPF_frequency_response(w):

    ejw_1 = np.exp(-1j * w)

    H_ejw = np.sum(h * ejw_1**n)

    return H_ejw


plot_filter_response(LPF_frequency_response)
