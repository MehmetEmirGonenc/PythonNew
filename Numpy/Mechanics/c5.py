# Create a 1D array with random int 10 elements and replace every even number with 0.
import numpy as np

# Create random array and values between 0 and 200, size is 1D and have 10 elements
array = np.random.randint(0,200, size=10) # Arg 1 = start pos, 2 = end pos, size= (a,b..) a x b x ...
mask = array % 2 == 0
print(mask)
print(array)
# When we implement
array[mask] = 0
print(array)