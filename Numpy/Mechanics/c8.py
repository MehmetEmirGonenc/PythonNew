# Array manipulation: Create a NumPy array and reverse its elements in-place (i.e., without creating a new array).
import numpy as np

array = np.arange(0,10)
print(array)
array = np.flip(array)
print(array) # Reversed array