import numpy as np

# Problem 1: Create a 1D array of numbers 1 to 10
arr = np.arange(1, 11)
print("Problem 1:", arr)

# Problem 2: Create a 3x3 array of all zeros
arr = np.zeros((3,3), dtype='int32')
print("Problem 2:\n", arr)

# Problem 3: Create a 4x4 array of all ones
arr = np.ones((4,4), dtype='int32')
print("Problem 3:\n", arr)

# Problem 4: Create an array of 10 evenly spaced numbers between 0 and 5
arr = np.linspace(0, 5, 10)
print("Problem 4:", arr)

# Problem 5: Create a 3x3 identity matrix
arr = np.identity(3, dtype='int32')
print("Problem 5:\n", arr)

# Problem 6: Create a 4x4 array of random numbers between 0 and 1
arr = np.random.rand(4, 4)
print("Problem 6:\n", arr)

# Problem 7: Find the shape, size and dtype of an array
print("Problem 7:")
print("Shape:", arr.shape)
print("Ndim:", arr.ndim)
print("Size:", arr.size)
print("Dtype:", arr.dtype)

# Problem 8: Get the 3rd element from a 1D array
arr = np.arange(1, 11)
print("Problem 8:", arr[2])

# Problem 9: Get the last row of a 2D array
arr = np.arange(1, 17).reshape((4,4))
print("Problem 9:", arr[-1, :])

# Problem 10: Get the first 3 elements of a 1D array
arr = np.arange(1, 11)
print("Problem 10:", arr[:3])

# Problem 11: Get the middle 3x3 from a 5x5 array
arr = np.arange(1, 26).reshape((5,5))
print("Problem 11:\n", arr[1:4, 1:4])

# Problem 12: Get every other element from a 1D array
arr = np.arange(1, 11)
print("Problem 12:", arr[::2])

# Problem 13: Add two arrays together
arr = np.arange(1, 11)
brr = np.arange(12, 22)
print("Problem 13:", arr + brr)

# Problem 14: Multiply every element by 3
print("Problem 14:", arr * 3)

# Problem 15: Find the sum of all elements
arr = np.arange(1, 11)
print("Problem 15:", arr.sum())

# Problem 16: Find the mean of each row
arr = np.arange(1, 26).reshape((5,5))
print("Problem 16:", arr.mean(axis=1))

# Problem 17: Reshape a 1D array of 12 numbers into 3x4
arr = np.arange(1, 13).reshape((3,4))
print("Problem 17:\n", arr)

# Problem 18: Flatten a 2D array into 1D
arr = np.arange(1, 26).reshape((5,5))
print("Problem 18:", arr.flatten())

# Problem 19: Transpose a 3x4 array
arr = np.arange(1, 13).reshape((3,4))
print("Problem 19:\n", arr.transpose())

# Problem 20: Stack two arrays vertically
arr = np.arange(1, 17).reshape((4,4))
arr1 = np.arange(11, 27).reshape((4,4))
print("Problem 20:\n", np.vstack((arr, arr1)))