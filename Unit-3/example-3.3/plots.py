import numpy as np
import matplotlib.pyplot as plt
import mplcursors


def zero_padding(arr, final_len):
    if final_len >= len(arr):
        arr = np.concatenate((arr, np.zeros(final_len - len(arr))))

    return arr


def DFT(x):
    N = len(x)
    W = np.e ** (-1j * 2 * np.pi / N)
    X = np.zeros(N, dtype=np.complex64)
    for k in range(N):
        Xk = 0
        for n, xn in enumerate(x):
            Xk += xn * W ** (k * n)

        X[k] = Xk

    return X


def IDFT(X):
    N = len(X)
    W = np.e ** (-1j * 2 * np.pi / N)
    x = np.zeros(N, dtype=np.complex64)
    for n in range(N):
        xn = 0
        for k, Xk in enumerate(X):
            xn += Xk * W ** (-k * n)

        x[n] = xn / N

    return x


N = 3

x = np.array([1, 1, 1, 1, 1])
x = zero_padding(x, N)
# print(x)

X = DFT(x)
# print(X)

# x = IDFT(X)
# print(x)

nk = np.linspace(0, len(x) - 1, len(x))


fig1, axs1 = plt.subplots(1, 2)

axs1[0].set_title(f"N = {N}")
axs1[0].plot(nk, x, "ob", label="x[n]")
axs1[0].set_ylabel("x[n]")
axs1[0].set_xlabel("n")
axs1[0].grid(True)
axs1[0].legend()

axs1[1].set_title(f"N = {N}")
axs1[1].plot(nk, np.absolute(X), "or", label="|X[k]|")
axs1[1].set_ylabel("|X[k]|")
axs1[1].set_xlabel("k")
axs1[1].grid(True)
axs1[1].legend()

fig1.tight_layout()
mplcursors.cursor(hover=True)
plt.show()
