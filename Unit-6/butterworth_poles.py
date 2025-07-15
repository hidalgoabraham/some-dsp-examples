import sympy as sp

Omega_c = 0.703204446623272
N = 6

for k in range(0, 2*N):

    Sk = Omega_c * sp.E ** (sp.I * (sp.pi/(2*N))*(N+1+2*k))

    real_part, imag_part = Sk.as_real_imag()

    real_part = round(real_part, 5)
    imag_part = round(imag_part, 5)

    frac = sp.Rational(N+1+2*k, 2*N)

    if frac > 2:
        frac = frac - 2

    if frac > 1:
        frac = frac - 2

    print(f"S{k} = {Omega_c} exp(π*{frac})  ==>  {real_part}{'+' if imag_part > 0 else ''}{imag_part}{'j' if imag_part != 0 else ''}")
