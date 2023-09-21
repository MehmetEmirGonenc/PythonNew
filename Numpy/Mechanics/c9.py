# Array reshaping: Create a 1D NumPy array with 12 elements. Reshape it into a 2D array with 3 rows and 4 columns.
import numpy as np

array = np.arange(0,12) # 1D array with 12 elements
print(array)
array = array.reshape(3,4) # 2D array with 12 elemets 
print(array)