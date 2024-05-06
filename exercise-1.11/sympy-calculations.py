import sympy as sp

n = sp.symbols("n", Integer=True)
z = sp.symbols("z", Complex=True)

X1_z = sp.summation(sp.KroneckerDelta(n, 0) * z ** (-n), (n, -sp.oo, sp.oo))
sp.pprint(X1_z)
print("\n" + "#" * 100 + "\n")

X2_z = sp.summation(1 * z ** (-n), (n, 0, sp.oo))
sp.pprint(X2_z)
print("\n" + "#" * 100 + "\n")

X3_z = sp.summation(n * z ** (-n), (n, 0, sp.oo))
sp.pprint(X3_z)
print("\n" + "#" * 100 + "\n")
