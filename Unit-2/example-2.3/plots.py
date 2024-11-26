import numpy as np
import matplotlib.pyplot as plt

import mplcursors

ti = 0
tf = 200


def sample_this_signal(signal, t, T):
    xs = []
    n = []
    last_sample_time = t[0] - T
    ni = 0
    for i in range(len(signal)):

        if t[i] >= last_sample_time + T:
            last_sample_time = t[i]

            xs.append(signal[i])
            n.append(ni)
            ni += 1
        else:
            xs.append(None)
            n.append(None)

    return np.array(xs), np.array(n)


t = np.linspace(ti, tf, 201)
xc_t = 0.01 * (t / 10 - 10) * ((t / 10 - 10) - 10) * ((t / 10 - 10) + 10) * ((t / 10 - 10) + 5) + 20

T = 20
xs_t, n = sample_this_signal(xc_t, t, T)
x_n = xs_t

xr_t = np.zeros(len(t))

signals = []
for i in range(len(n)):
    if not n[i] is None:
        signal = x_n[i] * np.sin(np.pi * (t - n[i] * T) / T) / (np.pi * (t - n[i] * T) / T)

        # Correct invalid values
        for index, value in enumerate(signal):
            if t[index] - n[i] * T == 0:
                signal[index] = x_n[i]

        signals.append(signal)
        xr_t += signal


fig, axs = plt.subplots(2, 2)

axs[0, 0].set_title(f"")
axs[0, 0].plot(t, xc_t, "b", label="Xc(t)")
axs[0, 0].set_xlabel("t (s)")
axs[0, 0].grid(True)
axs[0, 0].legend()

axs[0, 1].set_title(f"T = {T} (s)")
axs[0, 1].plot(t, xs_t, ".r", label="Xs(t)")
axs[0, 1].set_xlabel("t (s)")
axs[0, 1].grid(True)
axs[0, 1].legend()

axs[1, 0].set_title(f"")
for signal in signals:
    axs[1, 0].plot(t, signal, "", label="")
axs[1, 0].plot(t, xs_t, ".r", label="Xs(t)")
axs[1, 0].set_xlabel("t")
axs[1, 0].grid(True)
axs[1, 0].legend()

axs[1, 1].set_title(f"")
axs[1, 1].plot(t, xr_t, "", label="Xr(t)")
axs[1, 1].set_xlabel("t")
axs[1, 1].grid(True)
axs[1, 1].legend()

fig.tight_layout()
mplcursors.cursor(hover=True)
plt.show()
