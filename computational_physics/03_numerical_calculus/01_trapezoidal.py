def trapezoidal_rule(vector_x, vector_y):
    """
    Performs numerical integration using the Trapezoidal Rule for a set of discrete data points.
    
    Parameters:
    vector_x (list/array): The x-coordinates of the data points (can be unequally spaced).
    vector_y (list/array): The y-coordinates (function values) corresponding to vector_x.
    
    Returns:
    float: The approximated definite integral (area under the curve).
    """
        
    n = len(vector_x) # Total number of data points
    
    if n < 2:
        raise ValueError("At least two data points are required for integration.")
        
    total_area = 0.0 # Initialise our running sum for the total integrated area
    
    # Loop through each sub-interval. If there are 'n' points, there are exactly 'n - 1' trapezoids trapped between them.
    for i in range(n - 1):
        # Calculate the width (base) of the current trapezoid. This handles both equally spaced and unequally spaced intervals perfectly.
        width = vector_x[i + 1] - vector_x[i]
        
        # Calculate the average height of the trapezoid. The two parallel vertical sides are vector_y[i] and vector_y[i + 1].
        average_height = (vector_y[i] + vector_y[i + 1]) / 2.0
        
        # Area of a single trapezoid = base * average height
        trapezoid_area = width * average_height
        
        # Add the area of this individual trapezoid to our total accumulated area.
        total_area += trapezoid_area
        
    return total_area


# example
if __name__ == "__main__":

    x_points = [0.0, 1.0, 2.0, 3.0]
    y_points = [0.0, 1.0, 4.0, 9.0] # corresponding y = x^2 values
    
    estimated_integral = trapezoidal_rule(x_points, y_points)
    
    print(f"Approximated Area: {estimated_integral}")
    print("Note: The approximation (9.5) is slightly higher than the exact value (9.0)")
    print("because a flat trapezoid ceiling overestimates a curve that bends upward (concave up).")
