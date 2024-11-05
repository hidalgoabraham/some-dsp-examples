import sympy

# Define symbolic variables
R = sympy.symbols("R", real=True, positive=True)  # Resistance
C = sympy.symbols("C", real=True, positive=True)  # Capacitance
L = sympy.symbols("L", real=True, positive=True)  # Inductance
w = sympy.symbols("w", real=True)  # Angular frequency

# Impedance of capacitor (Xc)
Xc = 1 / (sympy.I * w * C)

# Impedance of inductor (Xl)
Xl = sympy.I * w * L

# Impedance of parallel capacitor and inductor (Z_parallel)
Z_parallel = (Xl * Xc) / (Xl + Xc)

H = Z_parallel / (R + Z_parallel)


print("H(jw)=")
# sympy.pprint(H.simplify().expand(complex=True), use_unicode=False)
sympy.pprint(H.simplify())
# sympy.pprint(H)

# sympy.pprint(H.simplify(), use_unicode=False)

print("\n" + "#" * 100 + "\n")
print("Re{H(jw)}=")
sympy.pprint(sympy.re(H).simplify())

print("\n" + "#" * 100 + "\n")
print("Im{H(jw)}=")
sympy.pprint(sympy.im(H).simplify())

print("\n" + "#" * 100 + "\n")
print("|H(jw)|=")
sympy.pprint(abs(H).simplify())
# sympy.pprint(abs(H))

print("\n" + "#" * 100 + "\n")
print("/_H(jw)=")
sympy.pprint(sympy.arg(H).simplify())


# phase_H = sympy.atan(sympy.im(H) / sympy.re(H))

# print("\n" + "#" * 100 + "\n")
# print("/_H(jw)=")
# sympy.pprint(phase_H.simplify())
