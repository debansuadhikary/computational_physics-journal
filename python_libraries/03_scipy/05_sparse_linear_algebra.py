import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
import scipy.sparse.linalg as spla

# Physical Problem: 1D Discrete Quantum Particle in a Box Hamiltonian
N = 1000  # Grid size
diag = 2.0 * np.ones(N)
off_diag = -1.0 * np.ones(N - 1)

# 1. Dense Eigenvalue Solver (Full matrix decomposition)
H_dense = np.diag(diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
evals_dense, evecs_dense = la.eigh(H_dense)

print("=== Dense Eigenvalue Solver (scipy.linalg.eigh) ===")
print(f"Lowest 3 Eigenvalues (Ground & Excited States):")
print(evals_dense[:3])
print(f"Matrix Size: {H_dense.shape}\n")

# 2. Sparse Tridiagonal Matrix Solver (Lanczos ARPACK)
# Stores non-zero diagonals only (conserves memory for large quantum grids)
H_sparse = sp.diags([off_diag, diag, off_diag], [-1, 0, 1], format="csr")

# Solve for ONLY the k=3 lowest eigenvalues ('SA' = Smallest Algebraic)
evals_sparse, evecs_sparse = spla.eigsh(H_sparse, k=3, which="SA")

print("Sparse Eigenvalue Solver (scipy.sparse.linalg.eigsh)")
print(f"Lowest 3 Eigenvalues (Sparse Lanczos):")
print(evals_sparse)
print(
    f"Max Difference vs Dense Solver: {np.max(np.abs(evals_dense[:3] - evals_sparse)):.2e}"
)
