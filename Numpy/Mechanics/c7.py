# NumPy slicing: Given a 2D NumPy array, extract the second column.
import numpy as np

array = np.arange(0, 12) # Create a matrix include 12 elements
array = array.reshape(2,6) # elements need to fit multiply of two arg.
print(array)
# Now we seperate them
arr1 = array[0, :]
arr2 = array[1, :]
print(arr1)
print(arr2)