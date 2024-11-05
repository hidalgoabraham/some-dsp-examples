import numpy as np
import matplotlib.pyplot as plt
import mplcursors
import math

# Define n values for the plot
n = np.linspace(-100, 100, 201)  # Adjust range and number of points

# Calculate the x1 values
x1 = 5 / (5 + math.e ** (0.001 * n**2))

# Calculate the x2 values
x2 = np.sin(n / 5)

# Calculate the x2 values
x3 = x1 * x2

# Configure the plot
plt.title("Sine Pulse Function")
plt.xlabel("n")
# plt.ylabel("")
# plt.plot(n, x1, "-", label="x1[n]")
# plt.plot(n, x2, "-", label="x2[n]")
axis = plt.plot(n, x3, ".", label="x3[n]")

plt.grid(True)
plt.legend()
mplcursors.cursor(hover=True)

# Show the plot
plt.show()
