import numpy as np
import matplotlib.pyplot as plt
import mplcursors

A = 1
N = 41
N1 = 2

# Define k values for the plot
K = np.linspace(-50, 50, 101)

# Calculate ak_x values
ak_x = (A / N) * (np.sin((2 * np.pi * K / N) * (N1 + 1 / 2)) / np.sin(np.pi * K / N))

# Correct invalid values
for i, k in enumerate(K):
    if k % N == 0:
        ak_x[i] = A * (2 * N1 + 1) / N


# Configure the plot
plt.title("Fourier ak Coefficients")
plt.xlabel("k")
plt.ylabel("ak")
axis = plt.plot(K, ak_x, ".", label="ak")


plt.grid(True)
plt.legend()

# # labels = []
# # for i in range(len(n)):
# #     labels.append(f"sinc[n]={str(round(ak_x[i], 3))}" + f"\nn={str(round(n[i], 3))}")
# # mplcursors.cursor(axis, hover=True).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.index)]))

mplcursors.cursor(hover=True)

# Show the plot
plt.show()
