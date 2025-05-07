import sympy as sp
import lcapy as lp

X1 = lp.z**-1
x1 = X1.IZT()
sp.pprint(x1)
print("\n" + "#" * 100 + "\n")

X2 = lp.z**-4
x2 = X2.IZT()
sp.pprint(x2)
print("\n" + "#" * 100 + "\n")

X3 = 1 / (1 - lp.z**-1)
x3 = X3.IZT(causal=False)
sp.pprint(x3)
print("\n" + "#" * 100 + "\n")

X4 = 1 / (1 - lp.z**-2)
x4 = X4.IZT()
sp.pprint(x4)
print("\n" + "#" * 100 + "\n")
