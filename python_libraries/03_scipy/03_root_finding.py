import numpy as np
from scipy.optimize import root, root_scalar

# 1. Scalar Root-Finding (Single Variable)
# Solve f(x) = x^3 - 2*x - 5 = 0
f_scalar = lambda x: x**3 - 2 * x - 5
f_prime = lambda x: 3 * x**2 - 2  # Analytical derivative for Newton method

# Method A: Newton-Raphson (Derivative required)
res_newton = root_scalar(f_scalar, fprime=f_prime, x0=2.0, method="newton")

# Method B: Secant Method (No derivative required, two initial guesses)
res_secant = root_scalar(f_scalar, x0=1.0, x1=3.0, method="secant")

print("Scalar Root Finding (scipy.optimize.root_scalar)")
print(f"Newton Method Root : {res_newton.root:.10f} (Iters: {res_newton.iterations})")
print(f"Secant Method Root : {res_secant.root:.10f} (Iters: {res_secant.iterations})\n")


# 2. System of Multi-Variable Non-linear Equations
# Solve:
#   1) x^2 + y^2 - 4 = 0   (Circle radius 2)
#   2) exp(x) + y - 1 = 0  (Exponential curve)
def system_equations(v):
    x, y = v
    f1 = x**2 + y**2 - 4.0
    f2 = np.exp(x) + y - 1.0
    return [f1, f2]


initial_guess_vec = [1.0, -1.0]
res_sys = root(system_equations, initial_guess_vec, method="hybr")

print("=== Multi-Variable System Root Finding (scipy.optimize.root) ===")
print(f"Solution Vector (x, y) : {res_sys.x}")
print(f"Residual Values        : {res_sys.fun}")
