# Broadcasting is a powerful mechanism in NumPy that allows operations to be performed on arrays of different shapes and sizes without the need for explicit loops. It works by automatically expanding the smaller array to match the shape of the larger array during arithmetic operations.
# The rules for broadcasting are as follows:
# 1. If the arrays have different numbers of dimensions, the shape of the smaller array is padded with ones on its leading (left) side until both shapes have the same number of dimensions.
# 2. If the shapes of the arrays do not match in any dimension, the array with a shape of 1 in that dimension is stretched to match the other shape.
# 3. If the shapes of the arrays do not match and neither has a shape of 1 in that dimension, an error is raised.
import numpy as np

# 1. Adding a scalar to an array
# When we add a scalar value (like 50) to an array, NumPy automatically broadcasts the scalar to match the shape of the array. In this case, the scalar is added to each element of the array, resulting in a new array where each pixel value is increased by 50.
image = np.array([[200, 150], [100, 250]])
print(f"image: {image}")
brightness = image + 50
print(f"brightened image: {brightness}")

# 2. Adding two arrays of different shapes
# When we add two arrays of different shapes, NumPy applies the broadcasting rules to determine how to perform the operation. In this example, we have a 2D array (image) and a 1D array (filter). The filter is broadcasted across the rows of the image, allowing us to add the filter values to each corresponding element in the image.
filter = np.array([10, 20])
print(f"filter: {filter}")
filtered_image = image + filter
print(f"filtered image: {filtered_image}")

# 3. Multiplying arrays of different shapes
# Similar to addition, when we multiply two arrays of different shapes, NumPy applies the broadcasting rules to perform the operation. In this case, we have a 2D array (image) and a 1D array (scaling factor). The scaling factor is broadcasted across the rows of the image, allowing us to multiply each element in the image by the corresponding scaling factor.
scaling_factor = np.array([0.5, 1.5])
print(f"scaling factor: {scaling_factor}")
scaled_image = image * scaling_factor
print(f"scaled image: {scaled_image}")

# 4. Combining multiple operations with broadcasting
# We can also combine multiple operations that involve broadcasting. In this example, we first add a scalar value to the image and then multiply the result by a scaling factor. Both operations utilize broadcasting to ensure that the shapes of the arrays are compatible for the arithmetic operations.
combined_image = (image + 50) * scaling_factor
print(f"combined image: {combined_image}")