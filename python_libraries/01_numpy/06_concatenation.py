# Concatenating arrays 
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# concatanating along the first axis 
c = np.concatenate((a, b), axis = 0)
print("Concatenated array:", c)
print("Shape of concatenated array:", c.shape)

# Concatenating along the second axis
d = np.array([[1, 2], [3, 4]])
e = np.array([[5, 6], [7, 8]])
f = np.concatenate((d, e), axis = 1)
print("Concatenated array along the second axis:\n", f)
print("Shape of concatenated array along the second axis:", f.shape)

# Concatenating via vstack and hstack
g = np.vstack((d, e))
h = np.hstack((d, e))
print("Concatenated array using vstack:\n", g)
print("Concatenated array using hstack:\n", h)

# we can also use np.stack to concatenate along a new axis, but here we have to specify the axis along which to stack.

# Spliting arrays {This always splits the array into equal parts}

i = np.array([[1, 2], 
              [3, 4], 
              [5, 6], 
              [7, 8]])
print(f"Spliting the array \n{i} into 2 parts: \n{np.split(i, 2)}")

# we can also specify the axis along which to split the array.
print(f"Spliting the array \n{i} into 2 parts along the second axis: \n{np.split(i, 2, axis = 1)}")

# we can also use np.hsplit and np.vsplit to split along the horizontal and vertical axes, respectively.
print(f"Spliting the array \n{i} into 2 parts along the horizontal axis: \n{np.hsplit(i, 2)}")
print(f"Spliting the array \n{i} into 2 parts along the vertical axis: \n{np.vsplit(i, 2)}")

# Using repeat and tile to multiply arrays
j = np.array([1, 2, 3])
print(f"Repeating the array {j} 3 times: \n{np.repeat(j, 3)}")
k = np.array([[1, 2], [3, 4]])
print(f"Repeating the array \n{k} 2 times along axis 0: \n{np.repeat(k, 2, axis = 0)}")
print(f"Repeating the array \n{k} 2 times along axis 1: \n{np.repeat(k, 2, axis = 1)}")

l = np.array([1, 2, 3])
m = np.tile(l, (2, 1)) # np.tile(array, (number of dimensions, number of repetitions))
print(f"Tile the array {l} to shape (2,3): \n{m}")
n = np.tile(l, (2, 3))
print(f"Tile the array {l} to shape (2,9): \n{n}")