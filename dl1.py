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

t = 10
p = t
print(p)

my_list = [0, 1, 2, 3, 4, 5]

print(my_list[1:3])

# slice from start and everything prior to index 3
print(my_list[:3])

print(my_list[3:])

print(my_list[:])

# leaves off the last index
print(my_list[:-1])
print(my_list[:-3])

print(my_list[::-1])

array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array_1d[2:6])