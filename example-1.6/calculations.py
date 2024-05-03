import lcapy as lp  # type: ignore
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
