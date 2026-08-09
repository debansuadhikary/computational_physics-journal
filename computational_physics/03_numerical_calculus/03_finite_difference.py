import numpy as np
import matplotlib.pyplot as plt

def finite_difference_1d(f, x, h, method="central"):
    """
    Computes the 1D first derivative of f at points x using finite differences.
    
    Parameters:
        f      : callable, function f(x)
        x      : float or np.ndarray, evaluation points
        h      : float, grid step size
        method : str, 'forward', 'backward', or 'central'
        
    Returns:
        df : float or np.ndarray, numerical derivative approximation
    """
    if method == "forward":
        return (f(x + h) - f(x)) / h
    elif method == "backward":
        return (f(x) - f(x - h)) / h
    elif method == "central":
        return (f(x + h) - f(x - h)) / (2 * h)
    else:
        raise ValueError("Method must be 'forward', 'backward', or 'central'.")

def second_derivative_central(f, x, h):
    """Computes second derivative f''(x) using central difference."""
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)

if __name__ == "__main__":
    # Test function: f(x) = sin(x) -> f'(x) = cos(x)
    f = np.sin
    exact_df = np.cos
    
    x = np.linspace(0, 2 * np.pi, 100)
    h = 0.1
    
    # Numerical computations
    df_forward = finite_difference_1d(f, x, h, method="forward")
    df_central = finite_difference_1d(f, x, h, method="central")
    df_exact = exact_df(x)
    
    # Print max absolute errors
    err_forward = np.max(np.abs(df_forward - df_exact))
    err_central = np.max(np.abs(df_central - df_exact))
    
    print(f"Grid spacing h = {h}")
    print(f"Max Error (Forward Difference - O(h))   : {err_forward:.6f}")
    print(f"Max Error (Central Difference - O(h^2)) : {err_central:.6f}")
