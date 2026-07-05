# Vectorisation is the process of converting an algorithm from operating on a single value at a time to operating on a set of values at once. This is often done using NumPy, which allows for efficient operations on arrays.

import numpy as np

# We can create a vectorised function using the np.vectorize decorator. This allows us to apply a function to each element of an array without having to write a loop.
@np.vectorize
def my_function(x):
    return x**2 + 2*x + 1
# Now we can apply this function to an array of values.
x = np.array([1, 2, 3, 4, 5])
result = my_function(x)
print(result)  # Output: [ 4  9 16 25 36]

# We can also use NumPy's built-in functions, which are already vectorised. For example, we can use np.sin to apply the sine function to each element of an array.

# Disadvantages of vectorisation:
# 1. Memory Usage: Vectorised operations can consume more memory than their non-vectorised counterparts, especially when working with large arrays. This is because intermediate results may need to be stored in memory.
# 2. Performance: While vectorisation can significantly speed up computations, it may not always be the most efficient approach for small arrays or simple operations. In some cases, the overhead of setting up the vectorised operation may outweigh the performance benefits.