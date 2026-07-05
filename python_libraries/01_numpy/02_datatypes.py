# Data Types in NumPy
import numpy as np
# NumPy provides a variety of data types to accommodate different kinds of numerical data. Some common data types include:
# 1. int: Integer data type (e.g., int8, int16, int32, int64)
# int8: 8-bit signed integer (-128 to 127)
# int16: 16-bit signed integer (-32,768 to 32,767)
# int32: 32-bit signed integer (-2,147,483,648 to 2,147,483,647)
# int64: 64-bit signed integer (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)

# 2. float: Floating-point data type (e.g., float16, float32, float64)
# float16: 16-bit half-precision floating-point
# float32: 32-bit single-precision floating-point
# float64: 64-bit double-precision floating-point

# 3. bool: Boolean data type (True or False)

# 4. complex: Complex number data type (e.g., complex64, complex128)
# complex64: Complex number represented by two 32-bit floats (real and imaginary parts)
# complex128: Complex number represented by two 64-bit floats (real and imaginary parts)

# 5. string: String data type for text data

# NOTE: In the modern version of NumPy, we have to specify data types using 'np.int32', 'np.float64', etc. or simply 'int', 'float', etc.
 
arr = np.array([1, 2, 3, 4, 5])
print("Data type of arr:", arr.dtype) # Output = int64 (or int32 depending on the system)

arr = np.array([1, 2, 3.1, 4, 5])
print("Data type of arr:", arr.dtype) # Output = float64 (upgraded to float due to presence of a float element)

# Specifying data type during array creation:
arr = np.array([1, 2, 3, 4, 5], dtype = float)
print("Data type of arr:", arr.dtype) # Output = float64

# Type casting: Converting one data type to another uding astype() method
arr = np.array([1, 2, 3, 4, 5], dtype = int)
print("Original data type of arr:", arr.dtype) # Output = int64

arr_float = arr.astype(float)
print("Converted data type of arr_float:", arr_float.dtype) # Output = float64

# Type Casting errors:
arr = np.array(["1", "2", "hello"])
# arr_2 = arr.astype(int) This will raise an error because "hello" cannot be converted to an integer
# To avoid such errors, ensure that all elements in the array can be converted to the desired data type.
arr_2 = np.array(["1", "2", "3"])
print("Converted data type of arr_2:", arr_2.dtype) # Output = int64
# ValueError: invalid literal for int() with base 10: np.str_('hello')