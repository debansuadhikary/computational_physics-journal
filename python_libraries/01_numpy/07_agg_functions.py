# Aggregate functions are functions that operate on an array and return a single value.
# They are often used to summarize data or to compute statistics.
import numpy as np
# Create a 2D array
data = np.array([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]])

# Compute the sum of all elements in the array
total_sum = np.sum(data)
print("Total Sum:", total_sum)
# Compute the mean of all elements in the array
mean_value = np.mean(data)
print("Mean Value:", mean_value)
# Compute the standard deviation of all elements in the array
std_dev = np.std(data)
print("Standard Deviation:", std_dev)
# Compute the maximum value in the array
max_value = np.max(data)
print("Maximum Value:", max_value)
# Compute the minimum value in the array
min_value = np.min(data)
print("Minimum Value:", min_value)
# Compute the median of all elements in the array
median_value = np.median(data)
print("Median Value:", median_value)
# Compute the product of all elements in the array
product_value = np.prod(data)
print("Product Value:", product_value)
# Compute the cumulative sum of all elements in the array
cumulative_sum = np.cumsum(data)
print("Cumulative Sum:", cumulative_sum)
# Compute the cumulative product of all elements in the array
cumulative_product = np.cumprod(data)
print("Cumulative Product:", cumulative_product)

# These aggregate functions can also be applied along specific axes of the array. For example, to compute the sum along the columns (axis=0):
# Compute the sum along the columns (axis=0)
column_sum = np.sum(data, axis=0)
print("Column Sum:", column_sum)