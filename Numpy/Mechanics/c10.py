# Stacking arrays: Create two NumPy arrays, one with integers from 1 to 5 and another with integers from 6 to 10. Stack them horizontally to form a single 1D array.
import numpy as np

arr1 = np.arange(1,6)
arr2 = np.arange(6,11)
print(arr1,arr2)
print(np.hstack((arr1, arr2))) # Horizantally stacking
print(np.vstack((arr1,arr2))) # Vertically stacking
