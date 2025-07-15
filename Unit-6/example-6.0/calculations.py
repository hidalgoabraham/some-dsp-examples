import sympy as sp

Td = 1

Omega_c = sp.symbols("Omega_c", real=True, positive=True)

N = sp.symbols("N", real=True)

eq1 = sp.Eq(1/(1+(0.2*sp.pi / Omega_c)**(2*N)), (0.89125)**2)
eq2 = sp.Eq(1/(1+(0.3*sp.pi / Omega_c)**(2*N)), (0.17783)**2)

solution = sp.solve((eq1, eq2), (N, Omega_c))
print(solution)

N= 6
eq1 = sp.Eq(1 / (1 + (0.2 * sp.pi / Omega_c) ** (2 * N)), (0.89125) ** 2)
eq2 = sp.Eq(1 / (1 + (0.3 * sp.pi / Omega_c) ** (2 * N)), (0.17783) ** 2)

solution = sp.solve((eq1), (Omega_c))
print(solution)
solution = sp.solve((eq2), (Omega_c))
print(solution)

Omega_c = 0.703204446623272

abs_H_02 = sp.sqrt(1/(1+(0.2*sp.pi / Omega_c)**(2*N)))
print(f"abs_H_02 = {round(abs_H_02, 5)}")

abs_H_03 = sp.sqrt(1/(1+(0.3*sp.pi / Omega_c)**(2*N)))
print(f"abs_H_03 = {round(abs_H_03, 5)}")

##################################################################################

S = sp.symbols("S", complex=True)

A0, A1, A2, A3, A4, A5 = sp.symbols("A0 A1 A2 A3 A4 A5")

AK = [A0, A1, A2, A3, A4, A5]

dens = []
den = 1
SK = []

part2 = 0

for k in range(0, 2 * N):

    Sk = Omega_c * sp.E ** (sp.I * (sp.pi / (2 * N)) * (N + 1 + 2 * k))

    Sk_real, Sk_imag = Sk.as_real_imag()

    Sk_real = float(Sk_real)
    Sk_imag = float(Sk_imag)

    frac = sp.Rational(N + 1 + 2 * k, 2 * N)

    if frac > 2:
        frac = frac - 2

    if frac > 1:
        frac = frac - 2

    if Sk_real < 0:
        print(f"S{k} = {Omega_c} exp(π*{frac})  ==>  {Sk_real}{'+' if Sk_imag > 0 else ''}{Sk_imag}{'j' if Sk_imag != 0 else ''}")
        Sk = Sk_real + sp.I * Sk_imag
        den *= (S - Sk)
        dens.append(S - Sk)
        SK.append(Sk)

Hc_s = Omega_c**N / den

for i in range(0, len(dens)):
    part2 += AK[i] / dens[i]

print("Hc_s:")
sp.pprint(Hc_s)

print("\n\n")

print("part2:")
sp.pprint(part2)

eq = sp.Eq(Hc_s, part2)

solution = sp.solve((eq), (A0, A1, A2, A3, A4, A5))
print("\n\n")
print("Solution:")
print(solution)

for key, value in solution.items():
    index = AK.index(key)
    AK[index] = value
    print(f"{key} = {round(value, 5)}")

print("\n\n")

atez = sp.symbols("atez", complex=True)

HZ = []
for k in range(0, N):
    num = Td * AK[k]
    D = sp.E ** (SK[k] * Td)
    D_real, D_imag = D.as_real_imag()
    D = float(D_real) + sp.I * float(D_imag)
    
    den = 1 - D * atez

    HZ.append(num / den)

print("HZ:")
sp.pprint(HZ)

print("\n\n")

H05z = (HZ[0] + HZ[5]).simplify()
H14z = (HZ[1] + HZ[4]).simplify()
H23z = (HZ[2] + HZ[3]).simplify()

print("Hz:\n")

sp.pprint(H05z)
print("\n+\n")
sp.pprint(H14z)
print("\n+\n")
sp.pprint(H23z)