def rk2_method(f, x0, y0, x_target, steps):
    """
    Solves dy/dx = f(x, y) using the Runge-Kutta 2nd Order (Heun's) method.
    """
    h = (x_target - x0) / steps
    x = x0
    y = y0
    
    for _ in range(steps):
        # Step 1: Slope at the start of the interval
        k1 = f(x, y)
        
        # Step 2: Estimated slope at the end of the interval
        k2 = f(x + h, y + h * k1)
        
        # Step 3: Update y using the average of both slopes
        y = y + (h / 2.0) * (k1 + k2)
        x = x + h
        
    return y

# example
if __name__ == "__main__":
    # Solving dy/dx = x + y, with y(0) = 1. Exact value at x=1 is approx 3.43656
    def my_ode(x, y):
        return x + y
        
    # Let's use only 10 steps to see how accurate RK2 is compared to Euler
    result = rk2_method(my_ode, x0=0, y0=1, x_target=1, steps=10)
    print(f"RK2 approximated y at x=1 (10 steps): {result:.5f}")
