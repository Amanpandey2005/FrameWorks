import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array[0])  # Output: 1
print(array[1])  # Output: 2

# Negative indexing
print(array[-1])  # Output: 5
print(array[-2])  # Output: 4

# Slicing
print(array[1:4])  # Output: [2 3 4]
print(array[:3])  # Output: [1 2 3]
print(array[2:])  # Output: [3 4 5]

# Step size
print(array[::2])  # Output: [1 3 5]
print(array[1::2])  # Output: [2 4]

# Multidimensional indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[0, 0])  # Output: 1
print(matrix[1, 2])  # Output: 6

# Slicing in multidimensional arrays
print(matrix[0:2, 1:3])  # Output: [[2 3] # [5 6]]
                            
print(matrix[:, 1])  # Output: [2 5 8]
print(matrix[1, :])  # Output: [4 5 6]
print(array[: : -1])  # Output: [5 4 3 2 1] (reverses the array)