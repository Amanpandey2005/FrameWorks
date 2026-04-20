# np.split is used to split an array into multiple sub-arrays. It takes the array to be split and the indices at which to split as 
# arguments.
# The resulting sub-arrays are returned as a list.
# hsplit is used to split an array horizontally (column-wise). It takes the array to be split and the indices at which to split as 
# arguments. 
# The resulting sub-arrays are returned as a list.
# vsplit is used to split an array vertically (row-wise). It takes the array to
#be split and the np.indices at which to split as arguments. The resulting sub-arrays are returned as a list.
import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Split the array into 3 sub-arrays along the rows (vertical split)
v_split = np.vsplit(array, 3)
print("Vertical split:")
for sub_array in v_split:
    print(sub_array)
    
# Split the array into 3 sub-arrays along the columns (horizontal split)
h_split = np.hsplit(array, 3)
print("\nHorizontal split:")
for sub_array in h_split:
    print(sub_array)
print("\nUsing np.split to split the array into 3 sub-arrays along the rows:")

split_array = np.split(array, 3, axis=0)
for sub_array in split_array:
    print(sub_array)
