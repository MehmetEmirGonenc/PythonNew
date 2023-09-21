# Repeating arrays: Create an array and and make 10 lines array with same values
import numpy as np

arr = np.array([[1,3,5,7,9,11]])
arr = np.repeat(arr, 10, axis=0)
print(arr)