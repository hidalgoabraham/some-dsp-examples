import sympy as sp
import numpy as np


def complex_cartesian_to_polar(z, in_deg=False):
    module = np.absolute(z)
    phase = np.angle(z)

    if in_deg:
        phase = phase * 180 / np.pi

    return module, round(phase, 5)


z_1 = sp.symbols("z_1")

num = z_1 - 1

den = z_1**2 - (5 / 2) * z_1 + 1
sp.pprint(sp.factor(den, z_1))
# sp.pprint(sp.roots(den, z_1))

X = num / sp.factor(den)

A1 = (1 - 2) / (1 - 2 * 2)
print(A1)

A2 = (1 - 1 / 2) / (1 - (1 / 2) * (1 / 2))
print(A2)
