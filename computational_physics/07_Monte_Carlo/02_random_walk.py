import numpy as np
import matplotlib.pyplot as plt

def simulate_1d_random_walk(n_walkers: int = 1000, n_steps: int = 500):
    """
    Simulates 1D discrete random walks for multiple walkers.
    Step size dx = +/- 1 with equal probability.
    
    Returns:
        positions: ndarray of shape (n_walkers, n_steps + 1)
    """
    # Random steps: +1 or -1
    steps = np.random.choice([-1, 1], size=(n_walkers, n_steps))
    
    # Prepend starting position at x = 0
    positions = np.zeros((n_walkers, n_steps + 1))
    positions[:, 1:] = np.cumsum(steps, axis=1)
    
    return positions

def simulate_2d_random_walk(n_walkers: int = 1000, n_steps: int = 500):
    """
    Simulates 2D random walks with continuous random angles.
    Step size step_len = 1.0 in arbitrary direction theta in [0, 2pi).
    
    Returns:
        x_pos, y_pos: tuple of ndarrays of shape (n_walkers, n_steps + 1)
    """
    # Uniform random angles
    theta = np.random.uniform(0, 2 * np.pi, size=(n_walkers, n_steps))
    
    dx = np.cos(theta)
    dy = np.sin(theta)
    
    x_pos = np.zeros((n_walkers, n_steps + 1))
    y_pos = np.zeros((n_walkers, n_steps + 1))
    
    x_pos[:, 1:] = np.cumsum(dx, axis=1)
    y_pos[:, 1:] = np.cumsum(dy, axis=1)
    
    return x_pos, y_pos


if __name__ == "__main__":
    n_walkers = 5000
    n_steps = 500
    steps_arr = np.arange(n_steps + 1)
    

    # 1D Random Walk MSD Calculation

    pos_1d = simulate_1d_random_walk(n_walkers, n_steps)
    
    # MSD = <x^2(t)>
    msd_1d = np.mean(pos_1d**2, axis=0)
    
    # Linear regression fit: MSD = slope * t + intercept
    slope_1d, intercept_1d = np.polyfit(steps_arr, msd_1d, 1)
    
    print("--- 1D Random Walk Verification ---")
    print(f"Theoretical Slope (<x^2>/t) : 1.0000")
    print(f"Simulated Slope             : {slope_1d:.4f}")
    print(f"Fit Intercept               : {intercept_1d:.4f}\n")

  
    # 2D Random Walk MSD Calculation

    x_2d, y_2d = simulate_2d_random_walk(n_walkers, n_steps)
    
    # Squared displacement r^2 = x^2 + y^2
    r_squared = x_2d**2 + y_2d**2
    msd_2d = np.mean(r_squared, axis=0)
    
    slope_2d, intercept_2d = np.polyfit(steps_arr, msd_2d, 1)
    
    print("--- 2D Random Walk Verification ---")
    print(f"Theoretical Slope (<r^2>/t) : 1.0000  (step_length^2 = 1)")
    print(f"Simulated Slope             : {slope_2d:.4f}")
    print(f"Fit Intercept               : {intercept_2d:.4f}")
