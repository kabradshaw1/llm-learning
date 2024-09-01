import numpy as np

x = np.random.random((3, 2))
y = np.random.random((2, 3))
print(np.zeros((x.shape[0], y.shape[1])))
print(y)
print(x.shape[1])
print(y.shape[1])

def defnaive_matrix_vector_dot(x, y):
  assert len(x.shape) == 2
  assert len(y.shape) == 2
  assert x.shape[1] == y.shape[0]
  z = np.zeros((x.shape[0], y.shape[1]))
  for i in range(x.shape[0]):
    for j in range(y.shape[1]):
      row_x = x[i, :]
      column_y = y[:, j]
      z[i, j] = np.dot(row_x, column_y)
  return z