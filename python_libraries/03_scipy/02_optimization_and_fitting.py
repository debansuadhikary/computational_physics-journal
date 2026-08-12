import numpy as np
from scipy.optimize import curve_fit, minimize

# 1. Non-linear Curve Fitting (curve_fit)
# Physical Model: Damped Exponential Decay f(t) = A * exp(-gamma * t)
def decay_model(t, A, gamma):
    return A * np.exp(-gamma * t)


# Generate synthetic noisy experimental data
np.random.seed(42)
t_data = np.linspace(0, 5, 50)
true_A, true_gamma = 10.0, 0.8
y_exact = decay_model(t_data, true_A, true_gamma)
y_noisy = y_exact + np.random.normal(0, 0.5, size=t_data.size)

# Perform non-linear fit
popt, pcov = curve_fit(decay_model, t_data, y_noisy, p0=[1.0, 1.0])
p_errors = np.sqrt(np.diag(pcov))  # Standard deviation errors of parameters

print("Curve Fitting (scipy.optimize.curve_fit)")
print(
    f"Fitted Amplitude (A)   : {popt[0]:.4f} ± {p_errors[0]:.4f} (True: {true_A})"
)
print(
    f"Fitted Decay Rate (γ)  : {popt[1]:.4f} ± {p_errors[1]:.4f} (True: {true_gamma})\n"
)


# 2. Multidimensional Function Minimization (minimize)
# Potential Energy Surface: Rosenbrock Function f(x, y) = (1-x)^2 + 100*(y-x^2)^2
def potential_energy(coords):
    x, y = coords
    return (1 - x) ** 2 + 100 * (y - x**2) ** 2


initial_guess = [-1.2, 1.0]
res = minimize(
    potential_energy, initial_guess, method="Nelder-Mead", options={"tol": 1e-8}
)

print("Function Minimization (scipy.optimize.minimize)")
print(f"Minimum Found at (x, y) : {res.x}")
print(f"Minimum Potential Value  : {res.fun:.2e}")
print(f"Optimization Success     : {res.success}")
