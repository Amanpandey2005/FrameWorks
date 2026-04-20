import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array)
# Insert a value at a specific index
new_array = np.insert(array, 2, 10, axis = None)  # Insert 10 at index 2
print(new_array)  # Output: [ 1  2 10  3  4  5]

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
# Insert a new row at index 1
new_matrix = np.insert(matrix, 1, [10, 11, 12], axis=0)
print(new_matrix)
# Insert a new column at index 2
new_matrix_col = np.insert(matrix, 2, [13, 14, 15], axis=1)
print(new_matrix_col)