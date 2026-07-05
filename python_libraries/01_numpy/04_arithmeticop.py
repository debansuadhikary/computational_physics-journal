# NumPy allows for direct arithmetic operations on arrays, enabling element-wise computations without the need for explicit loops.
import numpy as np

# creating two 1D arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

# Element-wise addition
print("Addition:", arr1 + arr2)  # Output = [11 22 33 44 55]
# Element-wise subtraction
print("Subtraction:", arr1 - arr2)  # Output = [9 18 27 36 45]
# Element-wise multiplication
print("Multiplication:", arr1 * arr2)  # Output = [ 10  40  90 160 250]
# Element-wise division
print("Division:", arr1 / arr2)  # Output = [10. 10. 10. 10. 10.]
# Element-wise exponentiation
print("Exponentiation:", arr1 ** 2)  # Output = [ 100  400  900 1600 2500]
# Element-wise modulus
print("Modulus:", arr1 % arr2)  # Output = [0 0 0 0 0]
# Element-wise floor division
print("Floor Division:", arr1 // arr2)  # Output = [10 10 10 10 10]
# Note: All operations are performed element-wise, meaning each operation is applied to corresponding elements from the input arrays.


# Universal Functions (ufuncs): NumPy provides a variety of built-in mathematical functions that operate element-wise on arrays.
# Example: Applying the square root function to each element in an array
arr = np.array([1, 4, 9, 16, 25])

# square root
sqrt_arr = np.sqrt(arr)
print("Square roots:", sqrt_arr)  # Output = [1. 2. 3. 4. 5.]

# exponential
exp_arr = np.exp(arr)
print("Exponentials:", exp_arr)  # Output = [2.71828183e+00 5.45981500e+01 8.10308393e+03 8.88611052e+06 7.20048993e+10]

# logarithm
log_arr = np.log(arr)
print("Logarithms:", log_arr)  # Output = [0.         1.38629436 2.19722458 2.77258872 3.21887582]

# trigonometric functions
sin_arr = np.sin(arr)
print("Sine values:", sin_arr)  # Output = [ 0.84147098  -0.7568025   0.41211849 -0.28790332 -0.13235175]
cos_arr = np.cos(arr)
print("Cosine values:", cos_arr)  # Output = [0.54030231 -0.65364362 -0.91113026 -0.95892427 0.99120281]
tan_arr = np.tan(arr)
print("Tangent values:", tan_arr)  # Output = [1.55740772 1.15782128 -0.45231566 0.30060461 -0.13352639]    