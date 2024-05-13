import lcapy as lp
import sympy as sp

N, a = sp.symbols("N, a")

x = lp.us(lp.n - a) - lp.us(lp.n - a - N)
X = x.ZT()
sp.pprint(X)
