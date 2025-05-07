import sympy as sp
import lcapy as lp

A, a = sp.symbols("A, a")

Y = A / ((1 - lp.z**-1) * (1 - a * lp.z**-1))

y = Y.IZT()

sp.pprint(y)
