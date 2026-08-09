import numpy as np


def jacobi(A: np.ndarray, b: np.ndarray, tol: float = 1e-8, max_iter: int = 1000):
    """Solves Ax = b using the Jacobi Iterative Method."""
    n = len(b)
    x = np.zeros(n)
    x_new = np.zeros(n)
    diag = np.diag(A)
    R = A - np.diag(diag)  # Off-diagonal matrix (L + U)

    for k in range(1, max_iter + 1):
        x_new = (b - R @ x) / diag

        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k

        x = x_new.copy()

    return x, max_iter


def gauss_seidel(
    A: np.ndarray, b: np.ndarray, tol: float = 1e-8, max_iter: int = 1000
):
    """Solves Ax = b using the Gauss-Seidel Iterative Method."""
    n = len(b)
    x = np.zeros(n)

    for k in range(1, max_iter + 1):
        x_old = x.copy()

        for i in range(n):
            # Compute sum using latest values x[j] for j < i and old values for j > i
            sum_val = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1 :], x_old[i + 1 :])
            x[i] = (b[i] - sum_val) / A[i, i]

        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, k

    return x, max_iter


# Demonstration on a Discretized Poisson/Boundary Value System
if __name__ == "__main__":
    # Tridiagonal system: 2D/-1D finite difference matrix
    A = np.array(
        [
            [4.0, -1.0, 0.0, 0.0],
            [-1.0, 4.0, -1.0, 0.0],
            [0.0, -1.0, 4.0, -1.0],
            [0.0, 0.0, -1.0, 4.0],
        ]
    )

    b = np.array([15.0, 10.0, 10.0, 10.0])

    x_jacobi, iters_j = jacobi(A, b)
    x_gs, iters_gs = gauss_seidel(A, b)
    x_exact = np.linalg.solve(A, b)

    print("--- Iterative Solver Results ---")
    print(f"Exact Solution     : {x_exact}")
    print(f"Jacobi Solution    : {x_jacobi} (Iterations: {iters_j})")
    print(f"Gauss-Seidel Sol.  : {x_gs} (Iterations: {iters_gs})")
