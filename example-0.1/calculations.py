try:
    import sympy
except ModuleNotFoundError:
    import os

    os.system("pip install -r ./requirements.txt")


k, wo, t, W = sympy.symbols("k, wo, t, W")
Integral = sympy.integrate(sympy.E ** (-sympy.I * k * wo * t), (t, -W / 2, W / 2))

sympy.pprint(Integral.simplify())
