import numpy as np
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_1d = np.array([10, 20, 30])
result = array_2d + array_1d
print("Result of broadcasting 1D array to 2D array:")
print(result)