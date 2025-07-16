import numpy as np
import matplotlib.pyplot as plt
import mplcursors


def barlett_window(n):
    window = np.zeros(len(n))
    M = len(n) - 1
    for i in range(M + 1):
        if 0 <= n[i] <= M / 2:
            window[i] = 2 * n[i] / M
        else:
            window[i] = 2 - 2 * n[i] / M

    return window


def hann_window(n):
    window = np.zeros(len(n))
    M = len(n) - 1
    for i in range(M + 1):
        window[i] = 0.5 - 0.5 * np.cos(2 * np.pi * n[i] / M)

    return window


def hamming_window(n):
    window = np.zeros(len(n))
    M = len(n) - 1
    for i in range(M + 1):
        window[i] = 0.54 - 0.46 * np.cos(2 * np.pi * n[i] / M)

    return window


def blackman_window(n):
    window = np.zeros(len(n))
    M = len(n) - 1
    for i in range(M + 1):
        window[i] = 0.42 - 0.5 * np.cos(2 * np.pi * n[i] / M) + 0.08 * np.cos(4 * np.pi * n[i] / M)

    return window


M = 50
n = np.linspace(0, M, M + 1)

barlett_window = barlett_window(n)
hann_window = hann_window(n)
hamming_window = hamming_window(n)
blackman_window = blackman_window(n)


# Create the plot
fig, ax = plt.subplots(2, 2, figsize=(8, 8))

ax[0][0].plot(n, barlett_window, ".")
ax[0][0].set_title("Barlett Window")
ax[0][0].set_xlabel("n")
ax[0][0].set_ylabel("w[n]")
ax[0][0].grid(True)

ax[0][1].plot(n, hann_window, ".")
ax[0][1].set_title("Hann Window")
ax[0][1].set_xlabel("n")
ax[0][1].set_ylabel("w[n]")
ax[0][1].grid(True)

ax[1][0].plot(n, hamming_window, ".")
ax[1][0].set_title("Hamming Window")
ax[1][0].set_xlabel("n")
ax[1][0].set_ylabel("w[n]")
ax[1][0].grid(True)

ax[1][1].plot(n, blackman_window, ".")
ax[1][1].set_title("Blackman Window")
ax[1][1].set_xlabel("n")
ax[1][1].set_ylabel("w[n]")
ax[1][1].grid(True)

mplcursors.cursor(ax[0][0], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"n={int(sel.target[0])}, w[n]={sel.target[1]:.3f}"))
mplcursors.cursor(ax[0][1], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"n={int(sel.target[0])}, w[n]={sel.target[1]:.3f}"))
mplcursors.cursor(ax[1][0], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"n={int(sel.target[0])}, w[n]={sel.target[1]:.3f}"))
mplcursors.cursor(ax[1][1], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"n={int(sel.target[0])}, w[n]={sel.target[1]:.3f}"))

plt.tight_layout()
plt.show()
