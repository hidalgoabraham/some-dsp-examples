import sympy as sp

atez = sp.symbols("atez")

num = 1 - atez
den = (1 - sp.Rational(1, 2) * atez) * (1 - 2 * atez)

############################################
# Method 1: Using sympy's solve function
############################################

A1, A2 = sp.symbols("A1 A2")

part1 = num / den
part2 = A1 / (1 - sp.Rational(1, 2) * atez) + A2 / (1 - 2 * atez)

eq1 = sp.Eq(part1, part2)

# sp.pprint(eq1)

solution = sp.solve((eq1), (A1, A2))
print(solution)

############################################
# Method 2: Using sympy's apart function
############################################
den_roots = sp.roots(den, atez)
print("den roots:", den_roots)
sp.pprint(sp.apart(num / den, atez, extension=den_roots))