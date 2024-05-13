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

Ta = 10
xsa_t, na = sample_this_signal(xc_t, t, Ta)

Tb = 2 * Ta
xsb_t, nb = sample_this_signal(xc_t, t, Tb)

xa_n = xsa_t
xb_n = xsb_t


fig, axs = plt.subplots(2, 2)

axs[0, 0].set_title(f"T = {Ta} (s)")
axs[0, 0].plot(t, xc_t, "b", label="Xc(t)")
axs[0, 0].plot(t, xsa_t, "ob", label="Xs(t)")
axs[0, 0].set_xlabel("t (s)")
axs[0, 0].grid(True)
axs[0, 0].legend()

axs[0, 1].set_title(f"T = {Tb} (s)")
axs[0, 1].plot(t, xc_t, "b", label="Xc(t)")
axs[0, 1].plot(t, xsb_t, "ob", label="Xs(t)")
axs[0, 1].set_xlabel("t (s)")
axs[0, 1].grid(True)
axs[0, 1].legend()

axs[1, 0].set_title(f"T = {Ta} (s)")
axs[1, 0].plot(na, xa_n, "or", label="X[n]")
axs[1, 0].set_xlabel("n")
axs[1, 0].grid(True)
axs[1, 0].legend()

axs[1, 1].set_title(f"T = {Tb} (s)")
axs[1, 1].plot(nb, xb_n, "or", label="X[n]")
axs[1, 1].set_xlabel("n")
axs[1, 1].grid(True)
axs[1, 1].legend()

fig.tight_layout()
mplcursors.cursor(hover=True)
plt.show()
