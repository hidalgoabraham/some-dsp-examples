import sympy as sp

Td = 1

Omega_c = sp.symbols("Omega_c", real=True, positive=True)

N = sp.symbols("N", real=True)

eq1 = sp.Eq(1 + (2*sp.tan(0.1*sp.pi)/Omega_c) ** (2 * N), 1/(0.89125) ** 2)
eq2 = sp.Eq(1 + (2 * sp.tan(0.15 * sp.pi) / Omega_c) ** (2 * N), 1 / (0.17783) ** 2)

solution = sp.solve((eq1, eq2), (N, Omega_c))
print(solution)

N = 6
eq1 = sp.Eq(1 + (2 * sp.tan(0.1 * sp.pi) / Omega_c) ** (2 * N), 1 / (0.89125) ** 2)
eq2 = sp.Eq(1 + (2 * sp.tan(0.15 * sp.pi) / Omega_c) ** (2 * N), 1 / (0.17783) ** 2)

solution = sp.solve((eq1), (Omega_c))
print(solution)
solution = sp.solve((eq2), (Omega_c))
print(solution)

Omega_c = 0.766230957887133

abs_H_02 = sp.sqrt(1 / (1 + (2 * sp.tan(0.1 * sp.pi) / Omega_c) ** (2 * N)))
print(f"abs_H_02 = {round(abs_H_02, 5)}")

abs_H_03 = sp.sqrt(1 / (1 + (2 * sp.tan(0.15 * sp.pi) / Omega_c) ** (2 * N)))
print(f"abs_H_03 = {round(abs_H_03, 5)}")

##################################################################################

S = sp.symbols("S", complex=True)

dens = []

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
        dens.append(S - Sk)

den05 = (dens[0] * dens[5]).simplify()
den14 = (dens[1] * dens[4]).simplify()
den23 = (dens[2] * dens[3]).simplify()

den = den05 * den14 * den23

Hc_s = Omega_c**N / den

print("Hc_s:")
sp.pprint(Hc_s)

print("\n\n")

atez = sp.symbols("atez", complex=True)

Hz = Hc_s.subs(S, (2/Td)*((1 - atez)/(1 + atez)))

Hz = Hz.factor()

print("Hz:")
sp.pprint(Hz)

print("\n\n")

print(f"0.354520856402654 / 0.989533514129787 = {0.354520856402654 / 0.989533514129787}")
print(f"1 / 0.989533514129787 = {1 / 0.989533514129787}")
print(f"0.555811803039819 / 0.788242567492622 = {0.555811803039819 / 0.788242567492622}")
print(f"1 / 0.788242567492622 = {1 / 0.788242567492622}")
print(f"0.000575499232340151 / (0.989533514129787 * 0.788242567492622) = {0.000575499232340151 / (0.989533514129787 * 0.788242567492622)}")
