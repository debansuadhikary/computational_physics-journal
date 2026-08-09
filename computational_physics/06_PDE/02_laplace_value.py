import numpy as np


def solve_2d_laplace(Nx=50, Ny=50, tol=1e-5, max_iter=10000):
    """
    Solves 2D Laplace Equation on a rectangular grid using Gauss-Seidel Relaxation.
    Boundaries:
      - Top wall    : V = 100 V
      - Bottom wall : V = 0 V
      - Left wall   : V = 0 V
      - Right wall  : V = 0 V
    """
    V = np.zeros((Ny, Nx))

    # Apply Boundary Conditions
    V[-1, :] = 100.0  # Top boundary (last row in array)
    V[0, :] = 0.0  # Bottom boundary
    V[:, 0] = 0.0  # Left boundary
    V[:, -1] = 0.0  # Right boundary

    for iteration in range(1, max_iter + 1):
        V_old = V.copy()

        # Gauss-Seidel update over interior nodes only
        for i in range(1, Ny - 1):
            for j in range(1, Nx - 1):
                V[i, j] = 0.25 * (
                    V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1]
                )

        # Convergence check (Infinity norm of difference)
        diff = np.max(np.abs(V - V_old))
        if diff < tol:
            print(
                f"Gauss-Seidel converged in {iteration} iterations (Max Diff = {diff:.2e})."
            )
            return V

    print("Reached maximum iterations without full convergence.")
    return V


# Execute solver
grid_V = solve_2d_laplace(Nx=40, Ny=40, tol=1e-4)
print(f"Center Potential V(x=0.5, y=0.5): {grid_V[20, 20]:.2f} V")
