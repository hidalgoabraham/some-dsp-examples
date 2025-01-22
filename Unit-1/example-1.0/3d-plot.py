import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

fig = make_subplots(rows=1, cols=2, specs=[[{"type": "surface"}, {"type": "surface"}]])

re_z = np.linspace(-1.5, 1.5, 500)
im_z = np.linspace(-1.5, 1.5, 500)

x_grid, y_grid = np.meshgrid(re_z, im_z)
C = x_grid + 1j * y_grid
r_grid = np.absolute(C)
w_grid = np.angle(C)
zeta = r_grid * np.e ** (1j * w_grid)
Xz = zeta**3 + zeta**2 + zeta**1 + zeta**0 + zeta**-1 + zeta**-2 + zeta**-3

Xz_abs = np.absolute(Xz)
Xz_abs = np.clip(Xz_abs, None, 20)

surface = go.Surface(x=re_z, y=im_z, z=Xz_abs, colorscale="Turbo", showscale=False)
fig.add_trace(surface, row=1, col=1)


Xz_r1 = np.zeros(shape=[len(re_z), len(im_z)], dtype="complex")

for i in range(len(re_z)):
    for j in range(len(im_z)):
        r = np.sqrt(re_z[i]**2 + im_z[j]**2)

        if round(r, 2) == 1:
            c = re_z[i] + 1j * im_z[j]
            w = np.angle(c)

            zeta = round(r, 2) * np.e ** (1j * w)
            Xz_r1[j][i] = zeta**3 + zeta**2 + zeta**1 + zeta**0 + zeta**-1 + zeta**-2 + zeta**-3  # For some reason, Xz_r1[i][j] is calculated correctly but the plot is rotated by 90 degrees.

            # if abs(w) < 0.01:
            #     print(zeta)
            #     print(w)
            #     print(Xz_r1[i][j])
            #     print(i)
            #     print(re_z[i])
            #     print(j)
            #     print(im_z[j])
            #     print("")

        else:
            Xz_r1[i][j] = 0

surface = go.Surface(x=re_z, y=im_z, z=np.absolute(Xz_r1), colorscale="Turbo", showscale=False)
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
