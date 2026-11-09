import numpy as np
import plotly.graph_objects as go


# Fluid Properties
Mu = 0.001 # Dynamic Viscosity of fluid [Pa.S]

# Pipe Geometry and Pressure

L = 1.0 # Pipe length [m]
R = 0.1 # Pipe radius [m]
Pin = 1000 # Inlet pressure [Pa]
Pout = 0.0 # Outlet pressure [Pa]

# Create 3D cylindrical coordinates

x = np.linspace(0,L,30)
r = np.linspace(0,R,20)
theta = np.linspace(0, 2*np.pi, 40)

X, Rg, T = np.meshgrid(x,r,theta)

Y = Rg*np.cos(T)
Z = Rg*np.sin(T)

u = (Pin-Pout)/(4*Mu*L)*(R**2 - Rg**2)

# Plot

theta_s = np.linspace(0, 2*np.pi, 50)
x_s = np.linspace(0, L, 30)

X_s, T_s = np.meshgrid(x_s, theta_s)
Y_s = R * np.cos(T_s)
Z_s = R * np.sin(T_s)

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    mode='markers',
    marker=dict(
        size=2,
        color=u.flatten(),
        colorscale='Turbo',
        colorbar=dict(title='Velocity [m/s]')
    ),
    name='Flow'
))

fig.add_trace(go.Surface(
    x=X_s,
    y=Y_s,
    z=Z_s,
    opacity=0.2,
    showscale=False,
    name='Pipe Wall'
))

fig.update_layout(
    title='3D Pipe Flow with Transparent Pipe Wall',
    scene=dict(
        xaxis_title='Length x [m]',
        yaxis_title='Y [m]',
        zaxis_title='Z [m]',
        aspectmode='data'
    )
)

fig.show()