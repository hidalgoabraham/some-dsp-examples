import sympy as sp
import numpy as np

atez = sp.symbols("atez")
A1, A2 = sp.symbols("A1 A2")

part1 = (1 - atez) / ((1 - (1 / 2) * atez) * (1 - 2 * atez))
part2 = A1 / (1 - (1 / 2) * atez) + A2 / (1 - 2 * atez)
eq1 = sp.Eq(part1, part2)

# sp.pprint(eq1)

solution = sp.solve((eq1), (A1, A2))
print(solution)
