import sympy


k, wo, t, W = sympy.symbols("k, wo, t, W")
Integral = sympy.integrate(sympy.E ** (-sympy.I * k * wo * t), (t, -W / 2, W / 2))

sympy.pprint(Integral.simplify())
