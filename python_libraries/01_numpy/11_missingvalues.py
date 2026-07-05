# Handling missing values in NumPy arrays
# In this example, we will demonstrate how to handle missing values in NumPy arrays using NaN (Not a Number).
import numpy as np
# Create a NumPy array with some missing values represented by np.nan
data = np.array([1.0, 2.5, np.nan, 4.0, np.nan, 6.5])
print("Original data:", data)

# Check for missing values
missing_mask = np.isnan(data)
print("Missing values mask:", missing_mask)

# Count the number of missing values
num_missing = np.sum(missing_mask)
print("Number of missing values:", num_missing)

# Remove missing values
cleaned_data = data[~missing_mask]
print("Data after removing missing values:", cleaned_data)

# Replace missing values with the mean of the non-missing values
mean_value = np.nanmean(data)
filled_data = np.where(missing_mask, mean_value, data)
print("Data after replacing missing values with mean:", filled_data)

# Alternatively, replace missing values with a specific value (e.g., 0)
filled_data_with_zero = np.where(missing_mask, 0, data)
print("Data after replacing missing values with 0:", filled_data_with_zero)

# Infinity values can also be handled similarly using np.isinf() to check for infinite values and np.nan_to_num() to replace them with a specified value.
# Example of handling infinity values
data_with_inf = np.array([1.0, 2.5, np.inf, 4.0, -np.inf, 6.5])
print("Data with infinity values:", data_with_inf)
# Check for infinity values
inf_mask = np.isinf(data_with_inf)
print("Infinity values mask:", inf_mask)
# Replace infinity values with a specific value (e.g., 0)
filled_data_with_inf_replaced = np.where(inf_mask, 0, data_with_inf)
print("Data after replacing infinity values with 0:", filled_data_with_inf_replaced)
# Alternatively, replace infinity values with the maximum finite value in the array
max_finite_value = np.max(data_with_inf[~inf_mask])
filled_data_with_inf_replaced_max = np.where(inf_mask, max_finite_value, data_with_inf)
print("Data after replacing infinity values with max finite value:", filled_data_with_inf_replaced_max)
