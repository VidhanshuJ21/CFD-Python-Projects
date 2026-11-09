import numpy as np
import plotly.graph_objects as go

#Fluid Properties

Mu = 0.001 #Dynamic viscosity of fluid [Pa.S]
dpdx = -10 #Pressure gradient [Pa/m]

#Channel geometry
H = 0.005 #Channel height [m]
L = 1.0 #Channel length [m]
Pin = 10000 #Inlet pressure [Pa]
Pout = 0.0 #Outlet pressure [Pa]

#Pressure Gradient
dpdx = (Pout - Pin)/L

#Channel coordinates

x = np.linspace(0, L, 50)
y = np.linspace(-H, H, 100) 

#Poiseuille velocity profile
u = -(dpdx/(2*Mu))*(H**2-y**2)

# 2D Velocity field
U = np.tile(u,(len(x),1))

#Plot
fig = go.Figure(data=go.Heatmap(x=x,y=y*1000,z=U.T,colorbar_title='Velocity [m/s]'))
fig.update_layout(title='2D Poiseuille Flow Velocity Profile',xaxis_title='Channel Length [m]',yaxis_title='Channel Height [mm]')
fig.show()
print("Maximum velocity =", u.max(), "m/s")
