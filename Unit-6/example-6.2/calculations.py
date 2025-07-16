"""
This script takes a prototype LPF with a cutoff frequency of theta_p
and transforms it into a BPF with cutoff frequencies of omega_p1 and omega_p2
"""

import sympy as sp

atez = sp.symbols("atez", complex=True)
theta_p = 0.3 * sp.pi

omega_p1 = 0.2 * sp.pi
omega_p2 = 0.6 * sp.pi

num = 0.0007378266819677075 * (atez + 1) ** 6

den = (1 - 0.904364456790627 * atez + 0.215515000703639 * atez**2) * (1 - 1.0105771918997786 * atez + 0.35827069153329877 * atez**2) * (1 - 1.2686450101026294 * atez + 0.7051278704826119 * atez**2)

H_lpf = num / den

a = sp.cos((omega_p2 + omega_p1) / 2) / sp.cos((omega_p2 - omega_p1) / 2)
k = sp.cot((omega_p2 - omega_p1) / 2) * sp.tan(theta_p / 2)

atez_2 = -1 * (atez**2 - ((2 * a * k) / (k + 1)) * atez + (k - 1) / (k + 1)) / (((k - 1) / (k + 1)) * atez**2 - ((2 * a * k) / (k + 1)) * atez + 1)

H_bpf = H_lpf.subs(atez, atez_2)

sp.pprint(H_bpf)
