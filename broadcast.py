import numpy as np

x = np.random.random((32, 10))
print('x:', x)
y = np.random.random((10,))
# print('before expand', y.shape)
# print('y:', y)
# y = np.expand_dims(y, axis=0)
# print('after expand', y.shape)
# print('y after expand:', y)

# y = np.concatenate([y] * 32, axis=0)
# print('y after concatenate:', y)

def naive_add_matrix_and_vector(x, y):
  assert len(x.shape) == 2
  assert len(y.shape) == 1
  assert x.shape[1] == y.shape[0]
  x = x.copy()
  for i in range(x.shape[0]):
    for j in range(x.shape[1]):
      x[i, j] += y[j]
  return x

print(naive_add_matrix_and_vector(x, y))