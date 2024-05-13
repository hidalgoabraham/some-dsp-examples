import lcapy as lp
import sympy as sp

N = sp.symbols("N")

x = lp.n * (lp.us(lp.n) - lp.us(lp.n - N)) + N * lp.us(lp.n - N)
X = x.ZT()
sp.pprint(X)
