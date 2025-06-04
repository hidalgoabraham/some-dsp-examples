import numpy as np
import matplotlib.pyplot as plt
import mplcursors


x1 = np.array([6, 5, 4, 3, 2, 1])
x2 = np.roll(x1, -2)

x1 = np.concatenate((x1, np.concatenate((x1, x1))))

x2 = np.concatenate((x2, np.concatenate((x2, x2))))

n = np.linspace(-6, 11, 18)


fig1, axs1 = plt.subplots(2, 1)

axs1[0].set_title(f"")
axs1[0].plot(n, x1, "o", label="x~[n]")
axs1[0].axvline(x=0, color="r", linestyle="--")
axs1[0].axvline(x=5, color="r", linestyle="--")
axs1[0].set_ylabel("x~[n]")
axs1[0].set_xlabel("n")
axs1[0].grid(True)
axs1[0].legend()

axs1[1].set_title(f"")
axs1[1].plot(n, x2, "o", label=f"x[((n+2))6]")
axs1[1].axvline(x=0, color="r", linestyle="--")
axs1[1].axvline(x=5, color="r", linestyle="--")
axs1[1].set_ylabel("x[((n+2))6]")
axs1[1].set_xlabel("n")
axs1[1].grid(True)
axs1[1].legend()

fig1.tight_layout()
mplcursors.cursor(hover=True)
plt.show()
