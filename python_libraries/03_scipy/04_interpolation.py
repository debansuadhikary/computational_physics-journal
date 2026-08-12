import numpy as np
from scipy.interpolate import CubicSpline, interp1d

# Sparse physical measurements (e.g., potential at discrete nodes)
x_data = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y_data = np.array([0.0, 0.84, 0.91, 0.14, -0.75, -0.96])

# 1. 1D Linear and Nearest-Neighbor Interpolation
f_linear = interp1d(x_data, y_data, kind="linear")
f_nearest = interp1d(x_data, y_data, kind="nearest")

# 2. Smooth Cubic Spline Interpolation (Ensures continuous 1st & 2nd derivatives)
cs = CubicSpline(x_data, y_data, bc_type="natural")

# Query intermediate values at dense evaluation points
x_dense = np.linspace(0, 5, 11)

print("Interpolation Evaluation at Intermediates")
print(f"{'x':<6} | {'Linear':<10} | {'Cubic Spline':<12} | {'Spline Derivative':<16}")
print("-" * 52)

for x_val in x_dense[1::2]:  # Sample intermediate values
    y_lin = f_linear(x_val)
    y_cub = cs(x_val)
    dy_cub = cs(x_val, nu=1)  # nu=1 evaluates the first derivative
    print(f"{x_val:<6.2f} | {y_lin:<10.4f} | {y_cub:<12.4f} | {dy_cub:<16.4f}")
