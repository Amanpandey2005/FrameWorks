import numpy as np
array = np.array([10, 20, 30, 40, 50])
discount = 10
# Broadcasting allows us to perform operations on arrays of different shapes and sizes without explicitly reshaping them.
# In this example, we can subtract the discount from each element in the array without needing to
# reshape the discount value to match the shape of the array.
discounted_prices = array - (discount / 100) * array
print(discounted_prices)  # Output: [ 9. 18. 27 36. 45.]