# Filter a NumPy array: Given an array, filter out all values greater than 5.
import numpy as np

arr = np.arange(-20,20)
arr = arr[arr > 5]
print(arr)