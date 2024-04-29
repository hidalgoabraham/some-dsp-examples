import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

N1 = 3

fig = make_subplots(rows=1, cols=2, specs=[[{"type": "surface"}, {"type": "surface"}]])

re_z = np.linspace(-1.5, 1.5, 500)
im_z = np.linspace(-1.5, 1.5, 500)

x_grid, y_grid = np.meshgrid(re_z, im_z)
r_grid = np.sqrt(x_grid**2 + y_grid**2)
w_grid = np.arctan(y_grid / x_grid)
zeta = r_grid * np.e ** (-1j * w_grid)
Xz = zeta**3 + zeta**2 + zeta + 1 + zeta**-1 + zeta**-2 + zeta**-3

Xz_abs = abs(Xz)
Xz_abs = np.clip(Xz_abs, None, 20)

surface = go.Surface(x=re_z, y=im_z, z=Xz_abs, colorscale="Turbo", showscale=False)
fig.add_trace(surface, row=1, col=1)


Xz_r1 = np.empty(shape=[len(x_grid), len(x_grid[0])])
Xz_r1[:] = np.NaN

for i in range(len(x_grid)):
    for j in range(len(x_grid[0])):
        x = x_grid[i][j]
        y = y_grid[i][j]
        r = np.sqrt(x**2 + y**2)
        if x == 0:
            if y > 0:
                w = np.pi / 2
            elif y < 0:
                w = -np.pi / 2
            else:
                w = None
        else:
            w = np.arctan(y / x)

        if round(r, 2) == 1:
            zeta = r * np.e ** (-1j * w)
            Xz_r1[i][j] = zeta**3 + zeta**2 + zeta + 1 + zeta**-1 + zeta**-2 + zeta**-3
        else:
            Xz_r1[i][j] = 0

surface = go.Surface(x=re_z, y=im_z, z=abs(Xz_r1), colorscale="Turbo", showscale=False)
fig.add_trace(surface, row=1, col=2)

fig.update_layout(title_text="Z Transform", height=800, width=1600)

fig.update_layout(
    scene1_xaxis_title="Re[z]",
    scene1_yaxis_title="Im[z]",
    scene1_zaxis_title="Abs[X(z)]",
    scene2_xaxis_title="Re[z]",
    scene2_yaxis_title="Im[z]",
    scene2_zaxis_title="Abs[X(z)]",
)
fig.show()
