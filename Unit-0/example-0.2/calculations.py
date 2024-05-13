import sympy

k, n, N, N1 = sympy.symbols("k, n, N, N1")
Summation = sympy.Sum(sympy.E ** (-sympy.I * k * (2 * sympy.pi / N) * n), (n, -N1, N1)).doit()

# sympy.pprint(Summation)

sympy.pprint(sympy.trigsimp(Summation))
