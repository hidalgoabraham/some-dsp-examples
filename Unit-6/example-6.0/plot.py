import numpy as np
import matplotlib.pyplot as plt
import mplcursors


def plot_filter_response(frequency_response):
    """
    Plot the amplitude and amplitude in dB of a digital filter.

    Parameters:
    frequency_response (callable): Frequency response of the digital filter.
        It should take a single argument, w, and return the complex response.
    """
    w = np.linspace(0, 0.5, 501)  # Frequency axis

    # Evaluate the transfer function
    response = np.array([frequency_response(wi * np.pi) for wi in w])

    # Calculate amplitude and amplitude in dB
    amplitude = np.abs(response)
    amplitude_db = 20 * np.log10(np.maximum(amplitude, 1e-12))  # Prevent log10 from taking too small numbers

    # Create the plot
    fig, ax = plt.subplots(2, 1, figsize=(8, 6))

    ax[0].plot(w, amplitude, ".")
    ax[0].set_title("Amplitude Response")
    ax[0].set_xlabel("ω (π rad)")
    ax[0].set_ylabel("Amplitude")
    ax[0].grid(True)

    ax[1].plot(w, amplitude_db, ".")
    ax[1].set_title("Amplitude Response (dB)")
    ax[1].set_xlabel("ω (π rad)")
    ax[1].set_ylabel("Amplitude (dB)")
    ax[1].grid(True)
    ax[1].set_ylim(bottom=-50)

    mplcursors.cursor(ax[0], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"ω={sel.target[0]:.5f}π, Amplitude={sel.target[1]:.5f}"))
    mplcursors.cursor(ax[1], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"ω={sel.target[0]:.5f}π, Amplitude (dB)={sel.target[1]:.5f}"))

    plt.tight_layout()
    plt.show()


# Example usage:
def LPF_frequency_response(w):

    ejw_1 = np.exp(-1j * w)

    H1 = (0.287082013180539 - 0.446586090685371 * ejw_1) / (0.694887437633587 * ejw_1**2  - 1.29716067326293*ejw_1 + 1.0)
    H2 = (1.14544747821749*ejw_1 - 2.14280931825785) / (0.369915282589205*ejw_1**2  - 1.06910817351565*ejw_1 + 1.0)
    H3 = (1.85572730507731 - 0.630356363542051*ejw_1) / (0.257049482859917 * ejw_1**2  - 0.99725287801698*ejw_1 + 1.0)

    H = H1 + H2 + H3

    return H


plot_filter_response(LPF_frequency_response)
