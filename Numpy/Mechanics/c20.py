#  Reshaping with Missing Elements :Given a flattened 1D NumPy array and its shape (number of rows and columns), write a Python function to reshape the array while accommodating missing elements. If the number of elements in the flattened array does not match the required shape, insert zeros to fill in the missing elements.
import numpy as np

def resapeWithMissing(array, rows, columns): 
    # elms means elements
    requiredelms = rows * columns
    missingelms = requiredelms - len(array)
    
    if missingelms > 0:
        array = np.append(array, np.zeros(missingelms, dtype= array.dtype)) # Which means we complete array with zeros until reach the number of requiredelms
    elif missingelms < 0:
        array = array[:requiredelms] # Which means from start to requiredelms number and ignore other values after that number
    # If requiredelms and missingelms are equal we do not need to make any extra process like above
    array = array.reshape((rows, columns))
    return array
def main():
    # Create 1D array
    arr = np.array([1,2,6,8,3,5,56,34,432,7,53], dtype='int32')
    # We can't reshape 4x4 array with this array because we need 16 elements but we only have 11 
    # So we use our function
    arr = resapeWithMissing(arr, 4, 4)
    print(arr)
main()