# Create a NumPy array with even numbers from 2 to 20.
import numpy as np

array = np.arange(2,20,2) # first arg = start pos. , 2. = stop pos. , 3. = increase amount per every step 
print(array.reshape(3,3)) 
print(array)

# As you awere when we use another reshape or other function our array doesn't affected 
# This because we just point 'array' just like C or Cpp
# If we want to change main array : array = array.reshape(3,3)