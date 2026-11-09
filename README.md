# CFD-Python-Projects
Basic CFD simulations using Python, covering 2D Poiseuille flow, 3D pipe flow, and NACA 0012 airfoil flow, with interactive velocity-field visualisations using Plotly

# Basic CFD Python Projects

This folder contains three Python codes for visualising simple fluid-flow cases. The plots are interactive and they are generated using Plotly.

## 1. 2D Poiseuille Flow
It models fa laminar flow between two parallel plates using the analytical parabolic velocity profile. The velocity distribution is plotted as a 2D contour along the channel.

## 2. 3D Pipe Flow
It creates laminar flow through a circular pipe using the Hagen–Poiseuille velocity profile. The velocity distribution is displayed in 3D inside a transparent pipe wall.

## 3. Airfoil Flow – NACA 0012
Generates a NACA 0012 airfoil profile and estimates the surrounding flow using a source-panel potential-flow method. The velocity-magnitude contours are plotted around the airfoil. The current case uses an inlet velocity of 100 m/s and an AoA of 0°.

> **Note:** These are basic educational implementations intended to understand flow behaviour and visualisation. They are not substitutes for a validated CFD solver. In particular, the airfoil model is inviscid potential flow and does not capture boundary-layer separation or viscous effects.

## Requirements

Install Python, then install the required libraries:

```bash
pip install numpy plotly matplotlib
```

## How to Run

1. Save each code in a separate Python file.
2. Open a terminal in the project folder.
3. Run the required file:

```bash
python poiseuille_2d.py
python pipe_flow_3d.py
python airfoil_naca0012.py
```

A Plotly visualisation will open for each case. Run the files individually to view their respective contours fields.

## Learning Note

I developed and explored these codes myself, using basic AI assistance as a learning aid to understand selected concepts and implementation details. The work was not generated entirely by AI.
