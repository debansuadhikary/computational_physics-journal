# Indexing in NumPy allows you to access and manipulate specific elements, rows, or columns of an array.
import numpy as np

# Create a sample 2D array
array = np.array([10, 20, 30])
print("Original array:", array)

# syntax for indexing => array[index] or array[start:stop:step]

# Using positive indexing
first_element = array[0]  # Accessing the first element
sliced_array = array[0:2]  # Slicing to get the first two elements
print("First element (positive indexing):", first_element)
print("Sliced array (positive indexing):", sliced_array)

# Using negative indexing
last_element = array[-1]  # Accessing the last element
slices_array_neg = array[-2:]  # Slicing to get the last two elements
conventional_slices_array_neg = array[-1:-4:-1]  # Slicing to get the last two elements in reverse order
print("Last element (negative indexing):", last_element)    
print("Sliced array (negative indexing):", slices_array_neg)
print("Sliced array (negative indexing in reverse order):", conventional_slices_array_neg)

# Multi-dimensional indexing
matrix = np.array([[1, 2, 3],
                   [4, 5, 6], 
                   [7, 8, 9]])
element = matrix[1, 2]  # Accessing the element in the second row and third column
print("Element at (1, 2):", element)
print(matrix[1:, 1:]) # Slicing to get the last two rows and columns


# Advanced indexing with np.take
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]  # Indices of the elements to take
taken_elements = np.take(arr, indices) # Using np.take to get the specified elements
print(f"Taken elements: {taken_elements}")

# printing sliced values using loops 
ar = np.array([10, 20, 30, 40, 50])
# 1. using for loop and np.nditer
for x in np.nditer(ar): # it will give us the individual elements of the array one by one
    print(x, end=" ")
print()

# 2. using for loop and np.ndenumerate (it returns both index and value)
for i, x in np.ndenumerate(ar):
    print(f"index: {i}, value: {x}")

# View vs Copy
# When you slice an array, it creates a view of the original array, meaning that changes to the view will affect the original array.
original_array = np.array([1, 2, 3, 4, 5])
view_array = original_array[1:4]  # This creates a view of the original array
print("Original array before modification:", original_array)
print("View array before modification:", view_array)
view_array[0] = 99 # Modifying the view array
print("Original array after modification:", original_array)  # The original array is modified

# To create a copy of the array, you can use the copy() method, which creates a new array that is independent of the original array.
original_array = np.array([1, 2, 3, 4, 5])
copy_array = original_array[1:4].copy()  # This creates a copy of the sliced array
print("Original array before modification:", original_array)
print("Copy array before modification:", copy_array)
copy_array[0] = 99 # Modifying the copy array
print("Original array after modification:", original_array)  # The original array remains unchanged
