import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

# Stiffness matrix K
K = np.array([
    [ 2.0, -1.0,  0.0],
    [-1.0,  2.0, -1.0],
    [ 0.0, -1.0,  2.0]
])

# External force vector (e.g., constant downward force on mass 2)
F_ext = np.array([0.0, 5.0, 0.0])

# Method 1: Direct Solve (Preferred for single right-hand side)
x_displacements = np.linalg.solve(K, F_ext)

print("--- Direct Solver ---")
print(f"Equilibrium Displacements: {x_displacements}\n")

# Method 2: LU Factorization (Preferred when solving for multiple force vectors)
lu_piv = lu_factor(K)  # LU decomposition with pivoting
x_lu = lu_solve(lu_piv, F_ext)

print("--- LU Decomposition Solver ---")
print(f"Equilibrium Displacements: {x_lu}")
