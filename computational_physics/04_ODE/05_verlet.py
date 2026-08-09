import numpy as np
import matplotlib.pyplot as plt

m = 1.0          # Mass (kg)
k = 1.0          # Spring constant (N/m)
omega = np.sqrt(k / m)

def acceleration(x):
    """Computes acceleration a(x) = - (k/m) * x."""
    return -(omega**2) * x

# Parameters
t_max = 50.0
dt = 0.1
time = np.arange(0, t_max, dt)
steps = len(time)

# Initial conditions: x(0) = 1.0, v(0) = 0.0
x0 = 1.0
v0 = 0.0

# Position Verlet
x_verlet = np.zeros(steps)
v_verlet = np.zeros(steps)

x_verlet[0] = x0
# First step x(dt) computed using Euler/Taylor approximation:
x_verlet[1] = x0 + v0 * dt + 0.5 * acceleration(x0) * (dt**2)

for i in range(1, steps - 1):
    a_current = acceleration(x_verlet[i])
    # Core Verlet formula: x_{n+1} = 2*x_n - x_{n-1} + a_n * dt^2
    x_verlet[i+1] = 2 * x_verlet[i] - x_verlet[i-1] + a_current * (dt**2)
    # Estimate velocity using central differences: v_n = (x_{n+1} - x_{n-1}) / (2*dt)
    v_verlet[i] = (x_verlet[i+1] - x_verlet[i-1]) / (2 * dt)

# Velocity Verlet
x_vverlet = np.zeros(steps)
v_vverlet = np.zeros(steps)

x_vverlet[0] = x0
v_vverlet[0] = v0

for i in range(steps - 1):
    a_curr = acceleration(x_vverlet[i])
    
    # Step 1: Update position x_{n+1} = x_n + v_n*dt + 0.5*a_n*dt^2
    x_vverlet[i+1] = x_vverlet[i] + v_vverlet[i] * dt + 0.5 * a_curr * (dt**2)
    
    # Step 2: Compute new acceleration a_{n+1}
    a_next = acceleration(x_vverlet[i+1])
    
    # Step 3: Update velocity v_{n+1} = v_n + 0.5*(a_n + a_{n+1})*dt
    v_vverlet[i+1] = v_vverlet[i] + 0.5 * (a_curr + a_next) * dt

# Energy Conservation Check
def total_energy(x, v):
    return 0.5 * m * (v**2) + 0.5 * k * (x**2)

E_vverlet = total_energy(x_vverlet, v_vverlet)

print(f"Initial Energy: {E_vverlet[0]:.6f} J")
print(f"Final Energy  : {E_vverlet[-1]:.6f} J")
print(f"Max Energy Drift: {np.max(np.abs(E_vverlet - E_vverlet[0])):.6f} J")
