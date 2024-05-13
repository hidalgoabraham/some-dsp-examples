import sympy

n, w, N1 = sympy.symbols("n, w, N1")

X = sympy.Sum(sympy.E ** (-sympy.I * w * n), (n, -N1, N1)).doit()

sympy.pprint(sympy.trigsimp(X))
