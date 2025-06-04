import sympy as sp

atez = sp.symbols("atez")

r1 = sp.Rational(1, 2) - sp.I * sp.sqrt(3) * sp.Rational(1, 2)
r2 = sp.Rational(1, 2) + sp.I * sp.sqrt(3) * sp.Rational(1, 2)

num = (atez - 4) * (atez - 3)
den = (atez - 1) * (atez - r1) * (atez - r2)

############################################
# Method 1: Using sympy's solve function
############################################

A1, A2, A3 = sp.symbols("A1 A2 A3")

part1 = num / den
part2 = A1 / (atez - 1) + A2 / (atez - r1) + A3 / (atez - r2)
eq1 = sp.Eq(part1, part2)

# sp.pprint(eq1)

solution = sp.solve((eq1), (A1, A2, A3))
print(solution)

############################################
# Method 2: Using sympy's apart function
############################################

den_roots = sp.roots(den, atez)

# print("den roots:", den_roots)

sp.pprint(sp.apart(num / den, atez, extension=den_roots))
