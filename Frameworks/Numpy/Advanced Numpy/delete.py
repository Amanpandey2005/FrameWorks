import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array)
new_array = np.delete(array,2, axis = None)
print(new_array)  # Output: [1 2 4 5]

array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array2d)
new_array2d = np.delete(array2d, 1, axis=0)  # Delete the second row
print(new_array2d)