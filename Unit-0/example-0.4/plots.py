import numpy as np
import matplotlib.pyplot as plt
import mplcursors

A = 1
N1 = 3

W = np.linspace(-15, 15, 501)

# Calculate X values
X = np.sin(W * (N1 + 1 / 2)) / np.sin(W / 2)

# Correct invalid values
for i, w in enumerate(W):
    if (w) % (2 * np.pi) == 0:
        X[i] = A * (2 * N1 + 1)

# Configure the plot
plt.title("Fourier Transform")
plt.xlabel("w")
plt.ylabel("Abs[X]")
axis = plt.plot(W, np.absolute(X), "-", label="Abs[X]")

plt.grid(True)
plt.legend()

mplcursors.cursor(hover=True)

# Show the plot
plt.show()
