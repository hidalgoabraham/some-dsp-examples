import numpy as np
import matplotlib.pyplot as plt

import mplcursors


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


ti = 0
tf = 0.0005

t = np.linspace(ti, tf, 1000)
x1c_t = np.cos(4000 * np.pi * t)
x2c_t = np.cos(16000 * np.pi * t)

T = 1 / 6000

x1s_t, na = sample_this_signal(x1c_t, t, T)
x2s_t, nb = sample_this_signal(x2c_t, t, T)

x1_n = x1s_t
x2_n = x2s_t


fig, axs = plt.subplots(2, 2)

axs[0, 0].set_title(f"X1c(t) = cos(4000*pi*t)")
axs[0, 0].plot(t, x1c_t, "b", label="X1c(t)")
axs[0, 0].plot(t, x1s_t, "ob", label="X1s(t)")
axs[0, 0].set_xlabel("t (s)")
axs[0, 0].grid(True)
axs[0, 0].legend()

axs[0, 1].set_title(f"X1c(t) = cos(16000*pi*t)")
axs[0, 1].plot(t, x2c_t, "b", label="X2c(t)")
axs[0, 1].plot(t, x2s_t, "ob", label="X2s(t)")
axs[0, 1].set_xlabel("t (s)")
axs[0, 1].grid(True)
axs[0, 1].legend()

axs[1, 0].set_title(f"")
axs[1, 0].plot(na, x1_n, "or", label="X1[n]")
axs[1, 0].set_xlabel("n")
axs[1, 0].grid(True)
axs[1, 0].legend()

axs[1, 1].set_title(f"")
axs[1, 1].plot(nb, x2_n, "or", label="X2[n]")
axs[1, 1].set_xlabel("n")
axs[1, 1].grid(True)
axs[1, 1].legend()

fig.tight_layout()
mplcursors.cursor(hover=True)
plt.show()
