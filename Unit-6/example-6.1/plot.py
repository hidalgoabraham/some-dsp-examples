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
    w = np.linspace(0, 1, 1001)  # Frequency axis

    # Evaluate the transfer function
    response = np.array([frequency_response(wi*np.pi) for wi in w])

    # Calculate amplitude and amplitude in dB
    amplitude = np.abs(response)
    amplitude_db = 20 * np.log10(np.maximum(amplitude, 1e-12))  # Prevent log10 from taking too small numbers

    # Create the plot
    fig, ax = plt.subplots(2, 1, figsize=(8, 6))

    ax[0].plot(w, amplitude, "-")
    ax[0].set_title("Amplitude Response")
    ax[0].set_xlabel("ω (π rad)")
    ax[0].set_ylabel("Amplitude")
    ax[0].grid(True)

    ax[1].plot(w, amplitude_db, "-")
    ax[1].set_title("Amplitude Response (dB)")
    ax[1].set_xlabel("ω (π rad)")
    ax[1].set_ylabel("Amplitude (dB)")
    ax[1].grid(True)
    ax[1].set_ylim(bottom=-200)

    mplcursors.cursor(ax[0], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"ω={sel.target[0]:.5f}π, Amplitude={sel.target[1]:.5f}"))
    mplcursors.cursor(ax[1], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"ω={sel.target[0]:.5f}π, Amplitude (dB)={sel.target[1]:.5f}"))

    plt.tight_layout()
    plt.show()


# Example usage:
def LPF_frequency_response(w):

    ejw_1 = np.exp(-1j * w)

    num = 0.0007378266819677075 * (ejw_1 + 1) ** 6

    den = (1 - 0.904364456790627 * ejw_1 + 0.215515000703639 * ejw_1**2) * (1 - 1.0105771918997786 * ejw_1 + 0.35827069153329877 * ejw_1**2) * (1 - 1.2686450101026294 * ejw_1 + 0.7051278704826119 * ejw_1**2)

    return num / den


plot_filter_response(LPF_frequency_response)
