# Import values from txt to array, manuplate them and write to txt again
import numpy as np

array = np.genfromtxt('c19.txt', delimiter=', ', dtype='int32') # delimiter which means seperate values by '...'
print(array)
array = array**2 # Take all values square
print(array)
np.savetxt('c19Output.txt', array, delimiter=';', fmt='%d') # fmt which means data format ; %d which menas integers