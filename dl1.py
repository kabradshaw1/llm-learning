import numpy as np

# example of scalars (rank-0 tensors)
a = np.array(12)

#example of a vector (rank-1 tensor)
b = np.array([12, 3, 6, 14, 7])

# example of a matrix (rank-2 tensor)
c = np.array([[5, 78, 2, 34, 0],
 [6, 79, 3, 35, 1],
 [7, 80, 4, 36, 2]])

# (rank-3 tensor)
d = np.array([[[5, 78, 2, 34, 0],
 [6, 79, 3, 35, 1],
 [7, 80, 4, 36, 2]],
 [[5, 78, 2, 34, 0],
 [6, 79, 3, 35, 1],
 [7, 80, 4, 36, 2]],
 [[5, 78, 2, 34, 0],
 [6, 79, 3, 35, 1],
 [7, 80, 4, 36, 2]]])

# this will give a tuple that discribes the shape of the tensor
a.shape