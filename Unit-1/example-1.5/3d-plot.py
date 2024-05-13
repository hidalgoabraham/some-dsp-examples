import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

N = 16
a = 0.8

fig = make_subplots(rows=1, cols=1, specs=[[{"type": "surface"}]])

re_z = np.linspace(-1.5, 1.5, 500)
im_z = np.linspace(-1.5, 1.5, 500)

y_grid, x_grid = np.meshgrid(im_z, re_z)
C = x_grid + 1j * y_grid
r_grid = np.absolute(C)
w_grid = np.angle(C)
zeta = r_grid * np.e ** (1j * w_grid)
Xz = 0 + 0 * 1j
for n in range(N):
    Xz += (a * zeta**-1) ** n

Xz_abs = np.absolute(Xz)
Xz_abs = np.clip(Xz_abs, None, 5)

surface = go.Surface(x=re_z, y=im_z, z=Xz_abs, colorscale="Turbo", showscale=False)
fig.add_trace(surface, row=1, col=1)

fig.update_layout(title_text="Z Transform", height=800, width=1600)

fig.update_layout(
    scene1_xaxis_title="Re[z]",
    scene1_yaxis_title="Im[z]",
    scene1_zaxis_title="Abs[X(z)]",
)
fig.show()
