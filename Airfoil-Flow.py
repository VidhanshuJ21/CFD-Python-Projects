import numpy as np
import plotly.graph_objects as go
from matplotlib.path import Path

NACA = "0012"
c = 1.0
Vin = 100.0
alpha = 0.0

t = int(NACA[2:]) / 100

n = 120
beta = np.linspace(0, np.pi, n)
x = c * (1 - np.cos(beta)) / 2

yt = 5*t*c*(
    0.2969*np.sqrt(x/c)
    - 0.1260*(x/c)
    - 0.3516*(x/c)**2
    + 0.2843*(x/c)**3
    - 0.1036*(x/c)**4
)

XB = np.r_[x, x[-2::-1]]
YB = np.r_[yt, -yt[-2::-1]]

x1, y1 = XB[:-1], YB[:-1]
x2, y2 = XB[1:], YB[1:]

dx = x2 - x1
dy = y2 - y1

S = np.sqrt(dx**2 + dy**2)
theta = np.arctan2(dy, dx)

# Control points
xc = (x1 + x2)/2
yc = (y1 + y2)/2

# Tangent and outward normal
tx = np.cos(theta)
ty = np.sin(theta)

nx = np.sin(theta)
ny = -np.cos(theta)

N = len(S)

A = np.zeros((N, N))

for i in range(N):

    for j in range(N):

        if i == j:
            A[i,j] = 0.5
            continue
        rx = xc[i] - x1[j]
        ry = yc[i] - y1[j]
        X =  rx*np.cos(theta[j]) + ry*np.sin(theta[j])
        Y = -rx*np.sin(theta[j]) + ry*np.cos(theta[j])

        r1 = X**2 + Y**2
        r2 = (X-S[j])**2 + Y**2
        u = (1/(4*np.pi))*np.log(r2/r1)

        v = (1/(2*np.pi))*(
            np.arctan2(Y, X-S[j])
            - np.arctan2(Y, X)
        )
        ug = u*np.cos(theta[j]) - v*np.sin(theta[j])
        vg = u*np.sin(theta[j]) + v*np.cos(theta[j])
        A[i,j] = ug*nx[i] + vg*ny[i]

a = np.radians(alpha)

Uinf = Vin*np.cos(a)
Vinf = Vin*np.sin(a)

b = -(Uinf*nx + Vinf*ny)

# Solve:
sigma = np.linalg.solve(A, b)

# FLOW FIELD

X, Y = np.meshgrid(
    np.linspace(-2*c, 5*c, 220),
    np.linspace(-2*c, 2*c, 140)
)

U = Uinf*np.ones_like(X)
V = Vinf*np.ones_like(Y)

for j in range(N):

    rx = X - x1[j]
    ry = Y - y1[j]

    xx =  rx*np.cos(theta[j]) + ry*np.sin(theta[j])
    yy = -rx*np.sin(theta[j]) + ry*np.cos(theta[j])

    r1 = xx**2 + yy**2
    r2 = (xx-S[j])**2 + yy**2

    r1 = np.maximum(r1, 1e-12)
    r2 = np.maximum(r2, 1e-12)

    u = sigma[j]/(4*np.pi)*np.log(r2/r1)

    v = sigma[j]/(2*np.pi)*(
        np.arctan2(yy, xx-S[j])
        - np.arctan2(yy, xx)
    )
    U += u*np.cos(theta[j]) - v*np.sin(theta[j])
    V += u*np.sin(theta[j]) + v*np.cos(theta[j])
speed = np.sqrt(U**2 + V**2)

airfoil = Path(np.column_stack((XB, YB)))
inside = airfoil.contains_points(
    np.column_stack((X.ravel(), Y.ravel()))
).reshape(X.shape)

speed[inside] = np.nan

#PLOT

fig = go.Figure()

fig.add_trace(go.Heatmap(
    x=X[0],
    y=Y[:,0],
    z=speed,
    colorscale="Turbo",
    colorbar=dict(title="Velocity [m/s]")
))

fig.add_trace(go.Scatter(
    x=XB,
    y=YB,
    mode="lines",
    line=dict(color="black", width=3),
    fill="toself",
    name="NACA 0012"
))

fig.update_layout(
    title=f"NACA 0012 | V = {Vin} m/s | AoA = {alpha}°",
    xaxis_title="x [m]",
    yaxis_title="y [m]",
    yaxis=dict(scaleanchor="x", scaleratio=1)
)

fig.show()
