import numpy as np
import matplotlib.pyplot as plt
import mplcursors


def complete_with_zeros(arr, final_len):
    if final_len >= len(arr):
        arr = np.concatenate((arr, np.zeros(final_len - len(arr))))

    return arr


N = 5

n = np.linspace(0, 50, 51)

x_n = np.array([1, 1, 1, 1, 1])
x_n = complete_with_zeros(x_n, N)
# print(x_n)

p_n = np.array([1])
p_n = complete_with_zeros(p_n, N)
# print(p_n)

pp_n = np.zeros(len(n))
p_n_index = -1
for i, ni in enumerate(n):
    p_n_index += 1
    if p_n_index >= len(p_n):
        p_n_index = 0

    pp_n[i] = p_n[p_n_index]

# print(pp_n)

xp_n = np.convolve(x_n, pp_n)
xp_n = xp_n[: len(n)]
# print(xp_n)


fig1, axs1 = plt.subplots(2, 2)

axs1[0, 0].set_title(f"N = {N}")
axs1[0, 0].plot(n, complete_with_zeros(x_n, len(n)), ".r", label="x[n]")
axs1[0, 0].set_xlabel("n")
axs1[0, 0].grid(True)
axs1[0, 0].legend()

axs1[0, 1].set_title(f"N = {N}")
axs1[0, 1].plot(n, pp_n, ".r", label="pp[n]")
axs1[0, 1].set_xlabel("n")
axs1[0, 1].grid(True)
axs1[0, 1].legend()

axs1[1, 0].set_title(f"N = {N}")
axs1[1, 0].plot(n, xp_n, ".r", label="xp[n]")
axs1[1, 0].set_xlabel("n")
axs1[1, 0].grid(True)
axs1[1, 0].legend()

fig1.tight_layout()
mplcursors.cursor(hover=True)
plt.show(block=False)

######################################################################################33

w = np.linspace(0, 3 * (2 * np.pi), 500)
k = np.zeros(len(w))
prev_ki = -1
for i, wi in enumerate(w):
    ki = (wi * N) / (2 * np.pi)

    if int(ki) == int(prev_ki) + 1:
        k[i] = int(ki)
        prev_ki = ki
    else:
        k[i] = None

X_ejw = np.e ** (-1j * 2 * w) * (np.sin(5 * w / 2) / np.sin(w / 2))
for i, wi in enumerate(w):  # Correct invalid values
    if (wi) % (2 * np.pi) == 0:
        X_ejw[i] = 5 * (np.cos((wi) * (5 / 2))) / (np.cos(wi / 2))


Xp_k = np.e ** (-1j * 4 * np.pi * k / N) * (np.sin((2 * np.pi * k / N) * (5 / 2)) / np.sin(np.pi * k / N))
for i, ki in enumerate(k):  # Correct invalid values
    if (ki) % (N) == 0:
        Xp_k[i] = 5 * (np.cos((2 * np.pi * ki / N) * (5 / 2))) / (np.cos(np.pi * ki / N))


fig2, axs2 = plt.subplots(2, 2)

axs2[0, 0].set_title(f"")
axs2[0, 0].plot(w, np.absolute(X_ejw))
axs2[0, 0].set_xlabel("w")
axs2[0, 0].set_ylabel("|X(ejw)|")
axs2[0, 0].grid(True)
axs2[0, 0].legend()

axs2[0, 1].set_title(f"")
axs2[0, 1].plot(w, np.angle(X_ejw))
axs2[0, 1].set_xlabel("w")
axs2[0, 1].set_ylabel("/_X(ejw)")
axs2[0, 1].grid(True)
axs2[0, 1].legend()

axs2[1, 0].set_title(f"N = {N}")
axs2[1, 0].plot(k, np.absolute(Xp_k), ".r")
axs2[1, 0].set_xlabel("k")
axs2[1, 0].set_ylabel("|Xp[k]|")
axs2[1, 0].grid(True)
axs2[1, 0].legend()

axs2[1, 1].set_title(f"N = {N}")
axs2[1, 1].plot(k, np.angle(Xp_k), ".r")
axs2[1, 1].set_xlabel("k")
axs2[1, 1].set_ylabel("/_Xp[k]")
axs2[1, 1].grid(True)
axs2[1, 1].legend()


fig2.tight_layout()
mplcursors.cursor(hover=True)
plt.show()
