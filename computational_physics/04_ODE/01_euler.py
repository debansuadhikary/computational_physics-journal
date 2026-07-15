def euler_method(f, x0, y0, x_target, steps):
    """
    Solves dy/dx = f(x, y) from x0 to x_target using Euler's method.
    """
    h = (x_target - x0) / steps
    x = x0
    y = y0
    
    for _ in range(steps):
        # Calculate slope at current point, then update y and x
        slope = f(x, y)
        y = y + h * slope
        x = x + h
        
    return y

# example
if __name__ == "__main__":
    # Solving dy/dx = x + y, where exact solution at x=1 for y(0)=1 is approx 3.4365
    import math
    
    def my_ode(x, y):
        return x + y
        
    result = euler_method(my_ode, x0=0, y0=1, x_target=1, steps=100)
    print(f"Approximated y at x=1: {result:.4f}")
