# Conditionals in NumPy
# The conditional functions in NumPy allow you to perform operations based on certain conditions. They are useful for filtering data, making decisions, and applying different operations to elements of an array based on specific criteria. Thwe most commonly used conditional functions in NumPy include `where`, `argwhere`, and logical operations like `logical_and` and `logical_or`, also known as boolean masking. These functions enable you to efficiently manipulate and analyze data based on conditions, making them essential tools for data analysis and scientific computing.
import numpy as np
# Create an array of random numbers
data = np.random.rand(10)
print("Data:", data)

# Create a boolean array where the condition is true with the help of a comparison operator "where"
result = np.where(data > 0.5, "High", "Low")
print("Result:", result)

# Finding the indices of elements that satisfy a condition using argwhere
rand = np.random.rand(3, 3)
print("Random Array:\n", rand)
print(f"The indices where the condition is satisfied: {np.argwhere(rand > 0.5)}")

# using np.take to extract elements based on indices
indices = np.argwhere(rand > 0.5)
extracted_elements = np.take(rand, indices)
print("Extracted Elements:\n", extracted_elements)

# using np.nonzero to find the indices of non-zero elements
non_zero_indices = np.nonzero(rand > 0.5)
print("Non-zero Indices:\n", non_zero_indices)

# Using logical operations to combine conditions
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])
print("Array:\n", arr)

# 1. Logical AND
and_result = np.logical_and(arr > 3, arr < 7)
print("Logical AND Result:\n", and_result, "\nElements that satisfy the condition:\n", arr[and_result])

# 2. Logical OR
or_result = np.logical_or(arr < 4, arr > 6)
print("Logical OR Result:\n", or_result, "\nElements that satisfy the condition:\n", arr[or_result])