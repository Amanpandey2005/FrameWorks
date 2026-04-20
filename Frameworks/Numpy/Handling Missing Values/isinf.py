import numpy as np
array = np.array([1, 2,np.inf, 3, 4, np.inf])
print(np.isinf(array))  # Output: [False False  True False False  True]
# We cant Compare np.inf with anything, not even itself. So we use np.isinf() to check for inf values in the array.
cleaned_array = np.nan_to_num(array, posinf= 23, neginf= -23)
# Replace inf with 23 and -inf with -23
print(cleaned_array)  # Output: [  1.   2.  23.   3.   4.  23.]