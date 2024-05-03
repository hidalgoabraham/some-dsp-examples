import sympy as sp
import lcapy as lp  # type: ignore

X = (1 + 2 * lp.z**-1 + lp.z**-2) / (1 - (3 / 2) * lp.z**-1 + (1 / 2) * lp.z**-2)

x = X.IZT()

sp.pprint(x)
