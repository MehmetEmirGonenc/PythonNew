# Matrix operations: Perform matrix multiplication between two randomly generated 4x4 matrices.
import numpy as np

arr1 = np.random.randint(-100,100, size=(4,4))
arr2 = np.random.randint(-100,100, size=(4,4))
print(arr1 * arr2)