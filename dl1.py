import numpy as np

# example of scalars (rank-0 tensors)
x = np.array(12)
print(x)
print(x.ndim)

#example of a vector (rank-1 tensor)
x = np.array([12, 3, 6, 14, 7])
print(x)
print(x.ndim)

# example of a matrix (rank-2 tensor)
x = np.array([[5, 78, 2, 34, 0],
 [6, 79, 3, 35, 1],
 [7, 80, 4, 36, 2]])

# (rank-3 tensor)
x = np.array([[[5, 78, 2, 34, 0],
 [6, 79, 3, 35, 1],
 [7, 80, 4, 36, 2]],
 [[5, 78, 2, 34, 0],
 [6, 79, 3, 35, 1],
 [7, 80, 4, 36, 2]],
 [[5, 78, 2, 34, 0],
 [6, 79, 3, 35, 1],
 [7, 80, 4, 36, 2]]])