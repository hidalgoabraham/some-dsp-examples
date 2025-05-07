import sympy as sp
import numpy as np

atez = sp.symbols("atez")
A1, A2, A3 = sp.symbols("A1 A2 A3")

r1 = (1 / 2) - 1j * np.sqrt(3) / 2

r2 = (1 / 2) + 1j * np.sqrt(3) / 2

part1 = ((atez - 4) * (atez - 3)) / ((atez - 1) * (atez - r1) * (atez - r2))
part2 = A1 / (atez - 1) + A2 / (atez - r1) + A3 / (atez - r2)
eq1 = sp.Eq(part1, part2)

# sp.pprint(eq1)

solution = sp.solve((eq1), (A1, A2, A3))
print(solution)
