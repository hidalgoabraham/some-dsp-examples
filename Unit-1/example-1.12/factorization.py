import sympy as sp

atez = sp.symbols("atez")
den = 1 - (3 / 2) * atez + (1 / 2) * atez**2

sp.pprint(den.factor())
