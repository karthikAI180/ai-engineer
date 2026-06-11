# Day 12 - Linear Algebra in NumPy (3Blue1Brown eps 1-8)
# 180-Day AI Engineer Roadmap | github.com/karthikAI180/ai-engineer

import numpy as np

# Task 1: Dot product - manual vs np.dot
a = np.array([2, 7, 1])
b = np.array([8, 2, 8])
result = 0
for i in range(len(a)):
    result += a[i] * b[i]
print("Task 1:", result, np.dot(a, b))          # 38 38

# Task 2: Scalar multiplication + vector addition
print("Task 2:", 3*a + 2*b)                     # [22 25 19]

# Task 3: Linear combination of basis vectors
v1 = np.array([1, 0])
v2 = np.array([0, 1])
print("Task 3:", 5*v1 + 3*v2)                   # [5 3]

# Task 4: Matrix x vector (column picture: columns = where i-hat, j-hat land)
M = np.array([[1, 2], [3, 4]])
v = np.array([3, 4])
manual = v[0]*M[:, 0] + v[1]*M[:, 1]
print("Task 4:", manual, M @ v)                 # [11 25] [11 25]

# Task 5: Matrix x matrix - nested loops (the definition)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.zeros((A.shape[0], B.shape[1]))
for i in range(A.shape[0]):          # each row of A
    for j in range(B.shape[1]):      # each column of B
        for k in range(A.shape[1]):
            result[i, j] += A[i, k] * B[k, j]
print("Task 5 (loops):")
print(result)                                   # [[19. 22.] [43. 50.]]

# Task 5: column picture - each result column = A applied to a column of B
result2 = np.zeros((2, 2))
result2[:, 0] = B[0, 0]*A[:, 0] + B[1, 0]*A[:, 1]
result2[:, 1] = B[0, 1]*A[:, 0] + B[1, 1]*A[:, 1]
print("Task 5 (columns):")
print(result2)
print("Task 5 (built-in):")
print(A @ B)

# Task 6: Composition - S @ R is one transformation: "do R, then do S"
R = np.array([[0, -1], [1, 0]])      # rotate 90 deg counterclockwise
S = np.array([[1, 1], [0, 1]])       # shear
p = np.array([1, 1])
print("Task 6:", S @ (R @ p), (S @ R) @ p)      # [0 1] [0 1] - associative
print("Task 6 swapped:", R @ S @ p)             # [-1 2] - order matters!

# Task 7: Determinant = factor by which the transformation scales AREA
# det = 0 -> space squished flat (no inverse). det < 0 -> orientation flips.
M = np.array([[3, 1], [1, 2]])
print("Task 7:", M[0][0]*M[1][1] - M[0][1]*M[1][0], np.linalg.det(M))   # 5 5.0