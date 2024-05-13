import lcapy as lp
import sympy as sp

x1 = lp.delta(lp.n)
X1 = x1.ZT()
sp.pprint(X1)
print("\n" + "#" * 100 + "\n")

x2 = lp.us(lp.n)
X2 = x2.ZT()
sp.pprint(X2)
print("\n" + "#" * 100 + "\n")

x2 = lp.n * lp.us(lp.n)
X2 = x2.ZT()
sp.pprint(X2)
print("\n" + "#" * 100 + "\n")
