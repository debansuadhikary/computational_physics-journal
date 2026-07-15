def rk4_method(f, x0, y0, x_target, steps):
    """
    Solves dy/dx = f(x, y) using the Classical Runge-Kutta 4th Order method.
    """
    h = (x_target - x0) / steps
    x = x0
    y = y0
    
    for _ in range(steps):
        # Calculate the 4 trial slopes
        k1 = f(x, y)
        k2 = f(x + h/2.0, y + (h/2.0) * k1)
        k3 = f(x + h/2.0, y + (h/2.0) * k2)
        k4 = f(x + h, y + h * k3)
        
        # Take the step using the weighted average of the slopes
        y = y + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        
    return y

# example
if __name__ == "__main__":
    # Solving dy/dx = x + y, with y(0) = 1. Exact value at x=1 is approx 3.43656365
    def my_ode(x, y):
        return x + y

    result = rk4_method(my_ode, x0=0, y0=1, x_target=1, steps=5)
    print(f"RK4 approximated y at x=1 (only 5 steps): {result:.6f}")
