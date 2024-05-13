import sympy as sp

B, C, a = sp.symbols("B, C, a")

res = sp.solve([B + C - 1, a * B + C], [B, C])

sp.pprint(res)
