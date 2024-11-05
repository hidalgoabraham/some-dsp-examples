import numpy as np
import matplotlib.pyplot as plt
import mplcursors


# Define n values for the plot
n = np.linspace(-100, 100, 201)  # Adjust range and number of points


# Calculate x1 values
x1 = np.sinc(n / 10)  # Normalized Cardinal Sine

# Configure the plot
plt.title("Normalized Cardinal Sine Function")
plt.xlabel("n")
plt.ylabel("sinc[n]")
# axis = plt.plot(n, x1, ".", label="sinc[n]")
plt.plot(n, x1, ".", label="sinc[n]")


plt.grid(True)
plt.legend()

# labels = []
# for i in range(len(n)):
#     labels.append(f"sinc[n]={str(round(x1[i], 3))}" + f"\nn={str(round(n[i], 3))}")
# mplcursors.cursor(axis, hover=True).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.index)]))

mplcursors.cursor(hover=True)

# Show the plot
plt.show()
