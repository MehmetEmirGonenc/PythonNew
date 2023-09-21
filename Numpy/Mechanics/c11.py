# Finding Unique Values: Create a 1D NumPy array with repeated values and find the unique values in the array.
import numpy as np

arr = np.array([0,0,0,0,1,1,2,2,13,13,14,16,17,17,17,20,21,21,21,21]) 
print(np.unique(arr))