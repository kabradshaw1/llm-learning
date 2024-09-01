import numpy as np

x = np.random.random((3, 2))
y = np.random.random((2, 3))
print(x)
print(y)
print(x.shape[1])
print(y.shape[0])
# z = np.dot(x, y)

# def naive_vector_dot(x, y):
#   assert len(x.shape) == 1
#   assert len(y.shape) == 1
#   assert x.shape[0] == y.shape[0]
#   z = 0.
#   for i in range(x.shape[0]):
#     z += x[i] * y[i]
#   return z

# print(naive_vector_dot(x[0], y))
# print(z)

# def naive_matrix_vector_dot(x, y):
#   z = np.zeros(x.shape[0])
#   for i in range(x.shape[0]):
#     z[i] = naive_vector_dot(x[i, :], y)
#   return z

# print(naive_matrix_vector_dot(x, y))
