# Matrix Operations: Given a 2D NumPy array representing a set of coordinates, compute the distance between each pair of points and store the distances in a new 2D array.
import numpy as np

array = np.random.randint(0, 30, size=(3,3)) #2D array
print(array)
array = array.reshape(9) # Make it 1D for make process easy
distances = np.zeros(8)

counter = 0
while counter < 8:
    distances[counter] = array[counter + 1] - array[counter] 
    counter += 1
print(distances) # 1D distances array, but question wants 2D
distances = distances.reshape(4,2)
print(distances)