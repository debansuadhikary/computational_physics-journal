# Array Reshaping with NumPy
import numpy as np
# Array reshaping is a common operation in data manipulation and analysis. Here, we change the size of an array without changing its data.

arr = np.array([1, 2, 3, 4, 5, 6])
# Reshape the array to 2 rows and 3 columns
reshaped_arr = arr.reshape(2, 3)
print("Original array:")
print(arr)
print("Reshaped array (2x3):")
print(reshaped_arr)

# Ravel is used to flatten an array into a 1D array
raveled_arr = reshaped_arr.ravel()
print("Raveled array:")
print(raveled_arr)

# Flat is another method to flatten an array, returning a 1D iterator. Here we have the original array as it is, but we can iterate over it in a flattened manner.
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
flattened_arr = arr_2d.flatten()
print("Original 2D array:")
print(arr_2d)
print("Flattened array using flat:")
print(flattened_arr)

flattened_arr[0] = 99
print("Modified flattened array:")
print(flattened_arr)
print("Original 2D array after modifying flattened array (remains unchanged):")
print(arr_2d)

# Transpose of a matrix means to interchange the rows and columns of the matrix. In NumPy, you can easily compute the transpose of a matrix using the `T` attribute or the `transpose()` method.
import numpy as np

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print("Original Matrix:", matrix)

# Compute the transpose of the matrix using transpose() method
transpose_matrix = matrix.transpose()
print("Transpose of the Matrix:", transpose_matrix)

# We can also swap any two axes using the swapaxes() method. 
arr = np.array([[1, 2, 4],
                [3, 4, 5],])
print("Original Array:\n", arr)
print("Original Array's shape: ", arr.shape)

# Swaping the axes of the 2 * 3 array with the help of swapaxes() method
swapped_arr = np.swapaxes(arr, 0, 1)
# swapped_arr = arr.swapaxes(0, 1) # another way to swap axes
print(f"Swapped Array:\n {swapped_arr}")
print("Swapped Array's shape: ", swapped_arr.shape)
# Here we are changing the shape of the array from (2, 3) to (3, 2) by swapping the axes. The first axis (0) becomes the second axis (1) and the second axis (1) becomes the first axis (0). The first axis corresponds to the rows and the second axis corresponds to the columns. So, after swapping, the rows become columns and the columns become rows.