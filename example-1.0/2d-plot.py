import numpy as np
import matplotlib.pyplot as plt
import mplcursors

W = np.linspace(-6.5, 6.5, 501)

# Calculate X values
expo = np.e ** (1j * W)
X_ejw = expo**3 + expo**2 + expo**1 + expo**0 + expo**-1 + expo**-2 + expo**-3

# Configure the plot
plt.title("Fourier Transform")
plt.xlabel("w")
plt.ylabel("Abs[X]")
axis = plt.plot(W, np.absolute(X_ejw), "-", label="Abs[X]")


plt.grid(True)
plt.legend()

mplcursors.cursor(hover=True)

# Show the plot
plt.show()
