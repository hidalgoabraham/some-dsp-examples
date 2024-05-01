# import sympy as sp

# r, n, wo, z = sp.symbols("r, n, wo, z")

# # r = sp.symbols("r", type=sp.Integer, real=True)
# # n = sp.symbols("n", type=sp.Integer, real=True)
# # wo = sp.symbols("wo", type=sp.Float, real=True, positive=True)
# # z = sp.symbols("z", type=sp.ComplexField, complex=True)

# # expr1 = (r * sp.E ** (sp.I * wo) * z**-1) ** n
# # expr2 = (r * sp.E ** (-sp.I * wo) * z**-1) ** n
# # S1 = sp.Sum(expr1, (n, 0, sp.oo)).doit()
# # S2 = sp.Sum(expr2, (n, 0, sp.oo)).doit()

# # Xz = S1 + S2

# expr = sp.cos(wo * n) * z**-n

# Xz = sp.Sum(expr, (n, 0, sp.oo)).doit()

# response =

# sp.pprint(response)

import lcapy as lp
import sympy as sp

wo = sp.symbols("wo")
r = sp.symbols("r")


x = r**lp.n * lp.cos(wo * lp.n)

Xz = x.ZT()

sp.pprint(Xz)

#############################
print("#" * 50)
z = sp.symbols("z")

cos_wo = sp.symbols("cos_wo")

cos_wo = (sp.E ** (sp.I * wo) + sp.E ** (-sp.I * wo)) / 2
den = z**2 - 2 * r * z * cos_wo + r**2

sp.pprint(den.factor())
