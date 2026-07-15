def newton_forward_interpolation(x_points, y_points, target_x):
    """
    Performs Newton-Forward Interpolation to estimate the y-value at target_x.
    
    Parameters:
    x_points (list): The x-coordinates of the data points (must be equally spaced).
    y_points (list): The y-coordinates corresponding to x_points.
    target_x (float): The x-value where we want to estimate the y-value.
    
    Returns:
    float: The interpolated y-value at target_x.
    """
    n = len(x_points)
    
    # Constructing the Forward Difference Table
    diff_table = [[0.0 for _ in range(n)] for _ in range(n)]
    
    # The 0th column of the difference table is original y-values.
    for i in range(n):
        diff_table[i][0] = y_points[i]
        
    # Dynamically calculate forward differences column by column.
    for j in range(1, n):
        for i in range(n - j):
            # The forward difference is calculated as the next value minus the current value
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    # Calculate the interpolation parameter 'u'
    # h is the spacing between consecutive x-values (assumed uniform).
    h = x_points[1] - x_points[0]
    
    # u measures how many steps target_x is away from the initial point x_0
    u = (target_x - x_points[0]) / h
    
    # Computing the Interpolated Value
    interpolated_y = diff_table[0][0]

    u_term = 1.0
    factorial = 1
    
    # Loop through the remaining terms of the formula
    for i in range(1, n):
        u_term *= (u - (i - 1))
        factorial *= i
        
        interpolated_y += (u_term * diff_table[0][i]) / factorial
        
    return interpolated_y


# example
if __name__ == "__main__":
    known_x = [10.0, 20.0, 30.0, 40.0]
    known_y = [1010.0, 8020.0, 27030.0, 64040.0]
  
    x_to_estimate = 15.0
    
    result = newton_forward_interpolation(known_x, known_y, x_to_estimate)
    
    print(f"The estimated y-value at x = {x_to_estimate} is: {result:.2f}")
