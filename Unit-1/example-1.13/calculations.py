import sympy as sp
import lcapy as lp

x = lp.delta(lp.n + 2) - (1 / 2) * lp.delta(lp.n + 1) - lp.delta(lp.n) + (1 / 2) * lp.delta(lp.n - 1)

sp.pprint(x)
print("")

X = x.ZT()
sp.pprint(X)
print("")

x = X.IZT()
sp.pprint(x)
