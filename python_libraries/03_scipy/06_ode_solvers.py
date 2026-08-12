import numpy as np
from scipy.integrate import solve_ivp

# Physical System: Non-Linear Pendulum with Damping
# Equations:
#   d(theta)/dt = omega
#   d(omega)/dt = - (g / L) * sin(theta) - b * omega
g = 9.81
L = 1.0
b = 0.25  # Damping coefficient


def pendulum_system(t, state):
    theta, omega = state
    dtheta_dt = omega
    domega_dt = -(g / L) * np.sin(theta) - b * omega
    return [dtheta_dt, domega_dt]


# Initial conditions: theta(0) = 45 degrees (in rad), omega(0) = 0.0
initial_state = [np.radians(45.0), 0.0]
t_span = (0.0, 10.0)  # Time domain [0, 10] s
t_eval = np.linspace(0.0, 10.0, 100)  # Specific evaluation points

# Solve ODE using Runge-Kutta 4th/5th order adaptive scheme (RK45)
sol = solve_ivp(
    pendulum_system,
    t_span,
    initial_state,
    method="RK45",
    t_eval=t_eval,
    rtol=1e-8,
    atol=1e-10,
)

print("ODE Solver (scipy.integrate.solve_ivp)")
print(f"Solver Status          : {sol.message}")
print(f"Successful Convergence : {sol.success}")
print(f"Total Time Steps Taken : {sol.t.size}")
print(
    f"Final State [theta, w] : [{sol.y[0, -1]:.4f} rad, {sol.y[1, -1]:.4f} rad/s]"
)
