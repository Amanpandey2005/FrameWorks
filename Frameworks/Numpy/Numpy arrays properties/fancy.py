import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array[[0,2,4]])  # Output: [1 3 5]
print(array[array > 2])  # Output: [3 4 5]