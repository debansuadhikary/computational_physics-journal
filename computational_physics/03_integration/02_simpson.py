def simpsons_one_third(vector_x, vector_y):
    """
    Performs numerical integration using Simpson's 1/3 Rule.
    
    Parameters:
    vector_x (list): Equally spaced x-coordinates of the data points.
    vector_y (list): The y-coordinates (function values) corresponding to vector_x.
    
    Returns:
    float: The approximated definite integral.
    """
    n = len(vector_x) - 1  # Number of intervals
    
    # Rule Requirement 1: We need at least 3 points (2 intervals) to fit a parabola.
    if n < 2:
        raise ValueError("Simpson's 1/3 rule requires at least 3 data points.")
        
    # Rule Requirement 2: The number of segments/intervals must be EVEN.
    if n % 2 != 0:
        raise ValueError("Simpson's 1/3 rule requires an EVEN number of intervals (odd number of points).")
        
    # Calculate the step size 'h' (assumes uniform spacing)
    h = vector_x[1] - vector_x[0]
    
    # Start our running sum with the first and last y-values (coefficients are both 1)
    integral_sum = vector_y[0] + vector_y[n]
    
    # Loop through all the inner points to apply the alternating 4 and 2 weights
    for i in range(1, n):
        if i % 2 == 1:
            # Odd index -> weight of 4
            integral_sum += 4 * vector_y[i]
        else:
            # Even index -> weight of 2
            integral_sum += 2 * vector_y[i]
            
    # Multiply the entire accumulated sum by h/3
    total_area = (h / 3.0) * integral_sum
    
    return total_area


# example
if __name__ == "__main__":

    x_points = [0.0, 0.5, 1.0, 1.5, 2.0]
    y_points = [0.0**3, 0.5**3, 1.0**3, 1.5**3, 2.0**3] # [0.0, 0.125, 1.0, 3.375, 8.0]
    
    estimated_integral = simpsons_one_third(x_points, y_points)
    
    print(f"Approximated Area: {estimated_integral:.4f}")
    print("Notice that for cubic functions or lower, Simpson's 1/3 rule yields the exact mathematical answer!")
