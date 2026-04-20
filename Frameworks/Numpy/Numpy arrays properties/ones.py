import numpy as np
zerores = np.zeros((3, 3))

print("3x3 array of zeros:", zerores)

ones = np.ones((2, 4))
print("2x4 array of ones:", ones)

full_array = np.full((3, 3), 7)
print("3x3 array filled with 7:", full_array)

arrange = np.arange(0, 10, 2)
print("Array with values from 0 to 10 with step 2:", arrange)

identity_matrix = np.eye(4)
print( identity_matrix)