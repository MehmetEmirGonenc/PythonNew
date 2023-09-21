# Advanced slicing: Given a 2D NumPy array, extract all even rows and odd columns and create a new array with the extracted elements.
import numpy as np

array = np.arange(0,100)
array = array.reshape((10,10))
print(array)
print(array[::2,:])  # For rows: form start to end, increase amount two ;for columns: any args
print(array[:,1::2]) # For rows: any args ;for columns: from 1 to end, increase amont two
print(array[::2, 1::2]) # Now combine two of them

