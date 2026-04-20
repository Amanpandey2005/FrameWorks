import numpy as np 
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10,11,12]])
reshaped_array = array.reshape(12, 1)
print(reshaped_array)

reshaped_array1 = array.reshape(3,4)
print(reshaped_array1)