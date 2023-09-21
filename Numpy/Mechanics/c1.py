# Create a NumPy array with values from 0 to 9.
import numpy as np

array = np.arange(0,10, dtype = 'int8') # same as: array = np.array([0,1,2,3,4,5,6,7,8,9], dtype='int16')
print(array.dtype)
print(array)