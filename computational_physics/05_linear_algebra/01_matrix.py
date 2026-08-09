import numpy as np

# 1. Vector Setup (e.g., 3D positions or state vectors)
u = np.array([1.0, 2.0, 3.0])
v = np.array([4.0, 5.0, 6.0])

# Dot product & Norm
dot_product = np.dot(u, v)          # Or u @ v
norm_u = np.linalg.norm(u)          # ||u|| = sqrt(u . u)

print(f"Dot product: {dot_product}")
print(f"Norm of u  : {norm_u:.4f}\n")

# 2. Matrix-Vector Operations
# Operator A (e.g., transformation matrix)
A = np.array([
    [2.0, -1.0,  0.0],
    [-1.0, 2.0, -1.0],
    [0.0, -1.0,  2.0]
])

# Matrix-vector product: y = A * u
y = A @ u  # Equivalent to np.matmul(A, u)
print(f"Matrix-Vector Product (A @ u):\n{y}\n")

# 3. Vectorization Benchmark vs Python Loop
N = 1000000
vec_a = np.random.rand(N)
vec_b = np.random.rand(N)

# Vectorized dot product (Fast)
fast_dot = np.dot(vec_a, vec_b)
print(f"Vectorized Dot Product computed for N={N} elements.")
