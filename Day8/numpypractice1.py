import numpy as np
arr = np.ones((5,5), dtype='int32')
b = np.zeros((3,3), dtype='int32')
b[1,1] = 9
arr[1:4, 1:4] = b
print(arr)