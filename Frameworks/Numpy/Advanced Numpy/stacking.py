#vstack = row wise stacking
#hstack = column wise stacking
import numpy as np
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
vstacked_array = np.vstack([array1, array2])
print("Vstacked array:\n", vstacked_array)
hstacked_array = np.hstack([array1, array2])
print("Hstacked array:\n", hstacked_array)
