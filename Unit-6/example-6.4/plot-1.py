import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import remez, freqz
import mplcursors

# --- 1. Definir Especificaciones del Filtro (Lineales y Normalizadas) ---
W_PASS = 0.2  # Borde de la banda de paso (normalizado a pi)
W_STOP = 0.3  # Borde de la banda de rechazo (normalizado a pi)

# Desviaciones lineales calculadas a partir de dB
Gmin_dB_pass = -0.01
Gmax_dB_stop = -60
RIPPLE_PASS_LINEAR = 1 - 10 ** (Gmin_dB_pass / 20)  # Desviación δ1
RIPPLE_STOP_LINEAR = 10 ** (Gmax_dB_stop / 20)  # Desviación δ2

# --- 2. Preparar los parámetros para la función remez ---
# Bandas de frecuencia [0, W_PASS, W_STOP, 1], donde 1 corresponde a pi.
bands = [0, W_PASS, W_STOP, 1.0]

# La respuesta deseada en cada banda (amplitud)
desired = [1, 0]

# La ponderación para controlar los rizados. Le damos más peso a la
# banda con menor error permitido (la de rechazo en este caso).
# weight = [δ_stop / δ_pass, 1]
weights = [RIPPLE_STOP_LINEAR / RIPPLE_PASS_LINEAR, 1]

# --- 3. Estimar el orden del filtro y Diseñar ---
# Fórmula empírica para estimar el orden M

M = int(np.ceil((-10 * np.log10(RIPPLE_PASS_LINEAR * RIPPLE_STOP_LINEAR) - 13) / (2.324 * (W_STOP - W_PASS) * np.pi)))

if M % 2 != 0:  # Para un filtro Tipo I, M debe ser par
    M += 1

# Diseñar el filtro usando el algoritmo de Parks-McClellan
# Añadimos fs=2.0 para hacer explícito el contexto de normalización
h = remez(M+1, bands, desired, weight=weights, fs=2.0)

# --- 4. Analizar y Graficar los Resultados ---
# Calcular la respuesta en frecuencia
w, H = freqz(h, 1, worN=1024*10)

# w está en radianes. Lo normalizamos por pi para el eje x.
w_norm = w / np.pi

# Calculate amplitude and amplitude in dB
amplitude = np.abs(H)
amplitude_db = 20 * np.log10(np.maximum(amplitude, 1e-12))  # Prevent log10 from taking too small numbers

phase = np.angle(H)

n = np.arange(0, M+1)

# Create the plot
fig, ax = plt.subplots(2, 2, figsize=(8, 6))

ax[0][0].plot(n, h, ".")
ax[0][0].set_title(f"Impulse Response. M = {M}")
ax[0][0].set_xlabel("n")
ax[0][0].set_ylabel("h[n]")
ax[0][0].grid(True)

ax[0][1].plot(w_norm, amplitude_db, "-")
ax[0][1].set_title("Amplitude Response (dB)")
ax[0][1].set_xlabel("ω (π rad)")
ax[0][1].set_ylabel("20Log|H(e^jω)| (dB)")
ax[0][1].grid(True)

ax[1][0].plot(w_norm, amplitude, "-")
ax[1][0].set_title(f"Amplitude Response. δ1 = {round(RIPPLE_PASS_LINEAR, 5)}, δ2 = {round(RIPPLE_STOP_LINEAR, 5)}")
ax[1][0].set_xlabel("ω (π rad)")
ax[1][0].set_ylabel("H(e^jω)")
ax[1][0].grid(True)

ax[1][1].plot(w_norm, phase, "-")
ax[1][1].set_title("Phase Response")
ax[1][1].set_xlabel("ω (π rad)")
ax[1][1].set_ylabel("/_H(e^jω) (rad)")
ax[1][1].grid(True)

mplcursors.cursor(ax[0][0], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"n={sel.target[0]}, h[n]={sel.target[1]:.5f}"))
mplcursors.cursor(ax[0][1], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"ω={sel.target[0]:.5f}π, 20Log|H(e^jω)|={sel.target[1]:.5f}dB"))
mplcursors.cursor(ax[1][0], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"ω={sel.target[0]:.5f}π, H(e^jω)={sel.target[1]:.5f}"))
mplcursors.cursor(ax[1][1], hover=True).connect("add", lambda sel: sel.annotation.set_text(f"ω={sel.target[0]:.5f}π, /_H(e^jω)={sel.target[1]:.5f}rad"))

plt.tight_layout()
plt.show()
