import numpy as np

import math
import matplotlib.pyplot as plt

import mplcursors


R = 100  # 100 ohms
C = 8e-12  # 8 pF
L = 19.79e-9  # 19.79 nH

J = 1j

f = np.linspace(100e6, 700e6, 201)

H = 2 * math.pi * f * L / (2 * math.pi * f * L + J * R * ((2 * math.pi * f) ** 2 * L * C - 1))

H_mag = np.absolute(H)
H_phase = np.angle(H)
H_real = np.real(H)
H_imag = np.imag(H)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(f, H_mag)
axs[0, 0].set_ylabel("|H|")
axs[0, 0].grid(True)

axs[0, 1].plot(f, H_phase)
axs[0, 1].set_ylabel("/_H")
axs[0, 1].grid(True)

axs[1, 0].plot(f, H_real)
axs[1, 0].set_ylabel("Re[H]")
axs[1, 0].grid(True)

axs[1, 1].plot(f, H_imag)
axs[1, 1].set_ylabel("Im[H]")
axs[1, 1].grid(True)

fig.tight_layout()
mplcursors.cursor(hover=True)
plt.show()
