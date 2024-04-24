try:
    import numpy as np
    import matplotlib.pyplot as plt
    import mplcursors
except ModuleNotFoundError:
    import os

    os.system("pip install -r ./requirements.txt")


# Define k values for the plot
K = np.linspace(-50, 50, 101)

# Calculate ak_x1 values, W=T/2
ak_x1 = np.sin(K * np.pi / 2) / (K * np.pi)
ak_x1[50] = 1 / 2  # To correct the invalid values

# Calculate ak_x2 values, W=T/4
ak_x2 = np.sin(K * np.pi / 4) / (K * np.pi)
ak_x2[50] = 1 / 4  # To correct the invalid values

# Calculate ak_x3 values, W=T/8
ak_x3 = np.sin(K * np.pi / 8) / (K * np.pi)
ak_x3[50] = 1 / 8  # To correct the invalid values

# Configure the plot
plt.title("Fourier ak Coefficients")
plt.xlabel("k")
plt.ylabel("ak")
axis = plt.plot(K, ak_x1, ".", label="W=T/2")
# axis = plt.plot(K, ak_x2, ".-", label="W=T/4")
# axis = plt.plot(K, ak_x3, ".-", label="W=T/8")


plt.grid(True)
plt.legend()

# labels = []
# for i in range(len(K)):
#     labels.append(f"x[n]={str(round(ak_x1[i], 3))}" + f"\nn={str(round(K[i], 3))}")
# mplcursors.cursor(axis, hover=True).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.index)]))

mplcursors.cursor(hover=True)

# Show the plot
plt.show()
