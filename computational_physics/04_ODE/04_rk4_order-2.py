def rk4_second_order(f, x0, y0, v0, x_target, steps):
    """
    Solves a second-order ODE: d2y/dx2 = f(x, y, dy/dx) using RK4.
    
    Parameters:
    f        : Function returning the second derivative d2y/dx2 given (x, y, v)
    x0, y0   : Initial position conditions
    v0       : Initial velocity condition (dy/dx at x0)
    """
    h = (x_target - x0) / steps
    x = x0
    y = y0
    v = v0
    
    for _ in range(steps):
        # Stage 1
        k1 = v
        m1 = f(x, y, v)
        
        # Stage 2
        k2 = v + (h / 2.0) * m1
        m2 = f(x + h / 2.0, y + (h / 2.0) * k1, v + (h / 2.0) * m1)
        
        # Stage 3
        k3 = v + (h / 2.0) * m2
        m3 = f(x + h / 2.0, y + (h / 2.0) * k2, v + (h / 2.0) * m2)
        
        # Stage 4
        k4 = v + h * m3
        m4 = f(x + h, y + h * k3, v + h * m3)
        
        # Update both position (y) and velocity (v) simultaneously
        y = y + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        v = v + (h / 6.0) * (m1 + 2*m2 + 2*m3 + m4)
        x = x + h
        
    return y, v

# example
if __name__ == "__main__":
    # ODE: y'' = -y  -> standard spring equation. 
    # With y(0)=1, y'(0)=0, the analytical solution is exactly y = cos(x).
    def spring_system(x, y, v):
        return -y  # acceleration depends only on position
        
    # Let's find displacement (y) and velocity (v) at x = 3.14159 (pi)
    # Cos(pi) should be -1.0, and velocity should be 0.
    pos, vel = rk4_second_order(spring_system, x0=0.0, y0=1.0, v0=0.0, x_target=3.14159265, steps=20)
    
    print(f"At x = pi:")
    print(f"Approximated Position (y) : {pos:.5f} (Expected: -1.00000)")
    print(f"Approximated Velocity (y'): {vel:.5f} (Expected:  0.00000)")
