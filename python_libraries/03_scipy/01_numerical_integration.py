import numpy as np
from scipy import integrate

# 1. 1D Continuous Integration (quad)
# Example: Integrating Gaussian function f(x) = exp(-x^2) from 0 to infinity
# Exact answer: sqrt(pi) / 2 approx 0.886226925
gaussian = lambda x: np.exp(-(x**2))

result_quad, error_estimate = integrate.quad(gaussian, 0, np.inf)

print("1D Integration (scipy.integrate.quad)")
print(f"Integral of exp(-x^2) [0, inf] : {result_quad:.10f}")
print(f"Estimated Absolute Error       : {error_estimate:.2e}\n")

# 2. 2D Double Integration (dblquad)
# Example: Integrating f(x, y) = x * y over x in [0, 2], y in [0, 1]
# Exact answer: (2^2 / 2) * (1^2 / 2) = 1.0
f_2d = lambda y, x: x * y  # Note order: f(y, x)

result_2d, error_2d = integrate.dblquad(
    f_2d,
    a=0,
    b=2,  # x bounds [0, 2]
    gfun=lambda x: 0,
    hfun=lambda x: 1,  # y bounds [0, 1]
)

print("2D Integration (scipy.integrate.dblquad)")
print(f"Double Integral of x*y         : {result_2d:.10f}\n")

# 3. Discrete Sample Integration (simpson)
# When you only have sampled data points (x, y) rather than a continuous function
x_samples = np.linspace(0, np.pi, 101)
y_samples = np.sin(x_samples)  # Exact integral [0, pi] of sin(x) = 2.0

result_simpson = integrate.simpson(y=y_samples, x=x_samples)

print("=== Discrete Sample Integration (scipy.integrate.simpson) ===")
print(f"Simpson's Rule on sin(x) samples : {result_simpson:.10f}")
