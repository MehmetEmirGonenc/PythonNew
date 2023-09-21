# Calculate the mean and standard deviation: Calculate the mean and standard deviation of a NumPy array with random numbers.
import numpy as np

arr = np.random.randint(-10, 10, size=(3,3))
print(arr)
print("Mean: ", np.mean(arr))
print("Deviation: ", np.std(arr)) # standard deviation