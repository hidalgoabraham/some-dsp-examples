import sympy as sp
import numpy as np


def complex_cartesian_to_polar(z, in_deg=False):
    module = np.absolute(z)
    phase = np.angle(z)

    if in_deg:
        phase = phase * 180 / np.pi

    return module, round(phase, 5)


z_1 = sp.symbols("z_1")

num = z_1**2 - 7 * z_1 + 12
# sp.pprint(sp.factor(num, z_1))

den = z_1**3 - 2 * z_1**2 + 2 * z_1 - 1
# sp.pprint(sp.factor(den, z_1))
# sp.pprint(sp.roots(den, z_1))

r1 = (1 / 2) - 1j * np.sqrt(3) / 2
# r1_module, r1_phase = complex_cartesian_to_polar(r1, True)
# print(f"r1 = {r1_module}/_{r1_phase}")

r2 = (1 / 2) + 1j * np.sqrt(3) / 2
# r2_module, r2_phase = complex_cartesian_to_polar(r2, in_deg=True)
# print(f"r2 = {r2_module}/_{r2_phase}")

# X = sp.factor(num) / sp.factor(den)

A1 = ((1 - 4) * (1 - 3)) / ((1 - r1) * (1 - r2))
print(A1)

A2 = ((r1 - 4) * (r1 - 3)) / ((r1 - 1) * (r1 - r2))
print(A2)

A3 = ((r2 - 4) * (r2 - 3)) / ((r2 - 1) * (r2 - r1))
print(A3)
