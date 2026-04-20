# Convert a multi-dimensional array into a 1D array
import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
flattened_array = array.flatten()
print(flattened_array)  # Output: [1 2 3 4 5 6 7 8 9]

# .ravel also flattens the array but returns a view instead of a copy
# This means that modifying the raveled array will affect the original array, while modifying the flattened array will not.
#.flattened_array_ravel = array.ravel()
#print(flattened_array_ravel)  # Output: [1 2 3 4 5 6 7 8 9]