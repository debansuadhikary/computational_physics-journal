import numpy as np


def function_to_integrate(x):
    """Integrand with a 1/sqrt(x) singularity at x=0."""
    return np.exp(-x) / np.sqrt(x)


def standard_monte_carlo(N: int):
    """Uniform Monte Carlo Integration over [0, 1]."""
    x_samples = np.random.uniform(0, 1, N)
    f_values = function_to_integrate(x_samples)

    integral_estimate = np.mean(f_values)
    # Variance of the estimator
    variance = np.var(f_values) / N
    error = np.sqrt(variance)
    return integral_estimate, error


def importance_sampling_monte_carlo(N: int):
    """Importance Sampling using weight function w(x) = 1/(2*sqrt(x)).

    Cumulative Distribution Function: C(x) = sqrt(x)
    Inverse CDF: x = U^2, where U ~ Uniform(0, 1)
    """
    u_samples = np.random.uniform(0, 1, N)
    x_samples = u_samples**2  # Transform samples to match w(x)

    # Function values divided by probability density p(x) = 1/(2*sqrt(x))
    # f(x) / p(x) = (e^-x / sqrt(x)) / (1 / (2*sqrt(x))) = 2 * e^-x
    ratio = 2.0 * np.exp(-x_samples)

    integral_estimate = np.mean(ratio)
    variance = np.var(ratio) / N
    error = np.sqrt(variance)
    return integral_estimate, error


if __name__ == "__main__":
    N = 100000
    exact_val = 1.493648265624854  # Analytical value: sqrt(pi) * erf(1)

    est_std, err_std = standard_monte_carlo(N)
    est_imp, err_imp = importance_sampling_monte_carlo(N)

    print(f"--- Monte Carlo Integration (N = {N}) ---")
    print(f"Exact Value                : {exact_val:.8f}")
    print(
        f"Standard Uniform Estimate  : {est_std:.8f} ± {err_std:.8f} (Error: {abs(est_std - exact_val):.2e})"
    )
    print(
        f"Importance Sampling Est.   : {est_imp:.8f} ± {err_imp:.8f} (Error: {abs(est_imp - exact_val):.2e})"
    )
