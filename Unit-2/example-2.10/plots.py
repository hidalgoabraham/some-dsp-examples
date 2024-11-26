import numpy as np
import matplotlib.pyplot as plt
import mplcursors

a = 1
T = 0.1

Omega = np.linspace(-3 * np.pi / T, 3 * np.pi / T, 1001)


H_jOmega = 1 / (a + 1j * Omega)

w = np.linspace(-3 * np.pi, 3 * np.pi, 1001)


H_ejw = T / (1 - np.e ** (-a * T) * np.e ** (-1j * w))

fig, axs = plt.subplots(2, 1)

axs[0].set_title(f"")
axs[0].plot(Omega, np.absolute(H_jOmega), "", label="Abs[H(jΩ)]")
axs[0].set_xlabel("Ω")
axs[0].grid(True)
axs[0].legend()

axs[1].set_title(f"")
axs[1].plot(w, np.absolute(H_ejw), "", label="Abs[H(ejω)]")
axs[1].set_xlabel("ω")
axs[1].grid(True)
axs[1].legend()

fig.tight_layout()
mplcursors.cursor(hover=True)
plt.show()
