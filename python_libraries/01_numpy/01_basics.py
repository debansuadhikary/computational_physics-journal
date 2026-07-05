# It stands for numerical python which makes it easier to work with arrays and matrices. NumPy provides a high-performance multidimensional array object and tools for working with these arrays.

# Why do we need NumPy?
# Here are some reasons why we need NumPy:
# 1. Fast Computational Speed: NumPy is implemented in C and optimized for performance, making it much faster than traditional Python lists for numerical computations.
# 2. Efficient Memory Usage: NumPy arrays use less memory compared to Python lists, which is crucial when working with large datasets.
# 3. Direct (Vectorized) Operations: NumPy allows for vectorized operations, enabling element-wise operations on entire arrays without the need for explicit loops.

import numpy as np
# creating a 1D array
arr = np.array([1, 2, 3, 4, 5])

ls = [1, 2, 3, 4, 5] # creating a list
arr = np.array(ls) # converting list to numpy array

# Dimensions and shapes of an array:
# Dimension: The number of indices needed to specify an element in the array. A 1D array has one dimension, a 2D array has two dimensions, and so on.
# 0D Array => Scalar values arranged in a single line, e.g., 32
# 1D Array => A single row or column of values, e.g., [1, 2, 3, 4, 5]
# 2D Array => A table or matrix of values, e.g., [[1, 2, 3], [4, 5, 6]]
# NOTE: The number of dimensions is also referred to as the rank of the array, and is directly proportional to the number of [].
print("Dimension of arr:", arr.ndim) # Output = 1

# Shapes: The shape of an array is a tuple that indicates the size of the array along each dimension. It represents the number of elements in each dimension.
print("Shape of arr:", arr.shape) # Output = (5,) => 5 elements in 1D array

# Creating arrays using arange:
ar = np.arange(0, 10, 2) # start, stop, step
print("Array using arange:", ar) # Output = [0 2 4 6 8]

# Creating arrays using linspace:
ls = np.linspace(0,1,5) # start, stop, number of elements
print("Array using linspace:", ls) # Output = [0.   0.25 0.5  0.75 1.  ]
# The linspace function generates 'number of elements evenly spaced values between 'start' and 'stop', inclusive.

# Creating arrays using logspace: (logarithmic scale array)
lg = np.logspace(1, 3, 4) # start exponent [10^1], stop exponent [10^3], number of elements
print("Array using logspace:", lg) # Output = [  10.          46.41588834 215.443469    1000.        ]
# The logspace function generates 'number of elements' values between 10^start and 10^stop, spaced evenly on a logarithmic scale.

# Creating arrays using zeros and ones:
z = np.zeros([3,4]) # 3 rows and 4 columns
o = np.ones([2,5])  # 2 rows and 5 columns
print("Array of zeros:\n", z)
print("Array of ones:\n", o)

# NOTE: We may introduce data type in the arrays using dtype parameter like np.zeros([3,4], dtype=int), by default it is float.

# Creating array full of any value:
arr = np.full((2,3), 7) # 2 rows and 3 columns filled with 7
print("Array full of 7s:\n", arr)

# Creating an uninitialized array:
uninit = np.empty([2,3]) # 2 rows and 3 columns
print("Uninitialized array:\n", uninit)

# Creating random arrays:
rand_arr = np.random.rand(2,3) # 2 rows and 3 columns with random values between 0 and 1
print("Random array:\n", rand_arr)

# Creating random floats: (random numbers having a normal distribution)
rand_floats = np.random.randn(2,3) # 2 rows and 3 columns with random values from a normal distribution
print("Random floats:\n", rand_floats)
# NOTE: The randn function generates samples from the "standard normal" distribution (mean = 0, standard deviation = 1).

# Creating random integers:
rand_ints = np.random.randint(1, 10, size=(2,3)) # 2 rows and 3 columns with random integers between 1 and 10
print("Random integers:\n", rand_ints)
# NOTE: The randint function generates random integers from the "discrete uniform" distribution in the specified range [low, high).

# Creating a multidimensional array: <manually>
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("Multidimensional array:\n", arr)
print("Dimension of arr:", arr.ndim) # Output = 2
print("Shape of arr:", arr.shape) # Output = (3, 3) => 3 rows and 3 columns
print("Size of arr:", arr.size) # Output = 9 => total number of elements in the array
print("Item size of arr:", arr.itemsize) # Output = 8 => size of each element in bytes (default is float64)
# NOTE: The above functions (ndim, shape, size, itemsize) can be used for any numpy array to get its properties, and are called attributes of the array object.
