import numpy as np
array = np.array([1, 2, np.nan, 4, 5,np.nan])
print(np.isnan(array))  # Output: [False False  True False False  True]
# We cant Compare np.nan with anything, not even itself. So we use np.isnan() to check for nan values in the array.

cleaned_array = np.nan_to_num(array, nan= 23)
# Replace NaN with 23
print(cleaned_array)  # Output: [ 1.  2. 23.  4.  5. 23.]