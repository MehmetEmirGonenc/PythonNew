# Array multiplication: Multiply two NumPy arrays of different shapes (e.g., a 2x3 array and a 3x2 array).
import numpy as np

arr1 = np.arange(0,6)
arr1 = arr1.reshape(2,3)
arr2 = np.arange(-6,0)
arr2 = arr2.reshape(3,2)
print(arr1 @ arr2) # Same as : np.dot(arr1, arr2)
