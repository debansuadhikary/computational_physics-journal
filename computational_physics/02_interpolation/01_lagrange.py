def lagrange_interpolation(x_points, y_points, target_x):
    """
    Performs Lagrange Interpolation to estimate the y-value at a given target_x.
    
    Parameters:
    x_points (list): The x-coordinates of the known data points.
    y_points (list): The y-coordinates of the known data points.
    target_x (float): The x-value where we want to estimate the y-value.
    
    Returns:
    float: The interpolated y-value at target_x.
    """
        
    n = len(x_points) # Total number of known data points
    interpolated_y = 0.0 # This will hold the final running sum P(x)
    
    # Outer Loop: Iterate through each given data point.
    for i in range(n):
        
        # 1 is the identity for multiplication
        basis_polynomial = 1.0
        
        # Inner Loop: Calculate the product term L_i(x) = Π (x - x_j) / (x_i - x_j)
        for j in range(n):
            if i != j:
                numerator = target_x - x_points[j]
                denominator = x_points[i] - x_points[j]
                basis_polynomial *= (numerator / denominator)
              
        interpolated_y += y_points[i] * basis_polynomial

    return interpolated_y


# example
if __name__ == "__main__":
    known_x = [1.0, 2.0, 3.0]
    known_y = [1.0, 4.0, 9.0]

    x_to_estimate = 2.5
    
    result = lagrange_interpolation(known_x, known_y, x_to_estimate)
    
    print(f"The estimated y-value at x = {x_to_estimate} is: {result}")
