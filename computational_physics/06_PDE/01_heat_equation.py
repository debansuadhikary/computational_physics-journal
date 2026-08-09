import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt

L = 1.0          # Length of rod (m)
Nx = 50          # Spatial grid points
x = np.linspace(0, L, Nx)
dx = x[1] - x[0]

alpha = 1e-4     # Thermal diffusivity (m^2/s)
t_max = 2.0      # Total time (s)

# Choose time step dt to satisfy stability for FTCS (r <= 0.5)
r_target = 0.4
dt = r_target * (dx**2) / alpha
Nt = int(t_max / dt)
r = alpha * dt / (dx**2)

print(f"dx = {dx:.4f}, dt = {dt:.6f}, r parameter = {r:.4f}, total steps = {Nt}")

# Initial Condition: Peak at center, zero elsewhere
u0 = np.sin(np.pi * x / L)  # Analytical mode profile
# Boundary Conditions: Fixed at 0 at ends (Dirichlet)

# 1. Explicit FTCS Solver
u_ftcs = u0.copy()
for n in range(Nt):
    u_next = u_ftcs.copy()
    # Vectorized internal grid updates
    u_next[1:-1] = u_ftcs[1:-1] + r * (u_ftcs[2:] - 2*u_ftcs[1:-1] + u_ftcs[:-1])
    # Apply Dirichlet boundary conditions
    u_next[0] = 0.0
    u_next[-1] = 0.0
    u_ftcs = u_next

# 2. Implicit Crank-Nicolson Solver
# System size for internal points (Nx - 2)
N_int = Nx - 2

# Left-hand side tridiagonal matrix A:
# Main diagonal = 1 + r, Off-diagonals = -r / 2
diag_A = (1 + r) * np.ones(N_int)
off_A = (-r / 2) * np.ones(N_int - 1)
A_sparse = sp.diags([off_A, diag_A, off_A], [-1, 0, 1], format="csr")

# Right-hand side tridiagonal matrix B:
diag_B = (1 - r) * np.ones(N_int)
off_B = (r / 2) * np.ones(N_int - 1)
B_sparse = sp.diags([off_B, diag_B, off_B], [-1, 0, 1], format="csr")

u_cn = u0.copy()
for n in range(Nt):
    # Construct right-hand side vector for internal points
    b = B_sparse @ u_cn[1:-1]
    
    # Solve linear system A * u_next = b
    u_internal_next = spla.spsolve(A_sparse, b)
    
    # Update state vector
    u_cn[1:-1] = u_internal_next
    u_cn[0] = 0.0
    u_cn[-1] = 0.0

# Analytical Solution for Comparison: u(x,t) = e^(-alpha * pi^2 * t / L^2) * sin(pi * x / L)
u_exact = np.exp(-alpha * (np.pi / L)**2 * t_max) * np.sin(np.pi * x / L)

print(f"\nResults at t = {t_max}s")
print(f"Max Absolute Error (FTCS)          : {np.max(np.abs(u_ftcs - u_exact)):.8e}")
print(f"Max Absolute Error (Crank-Nicolson) : {np.max(np.abs(u_cn - u_exact)):.8e}")
