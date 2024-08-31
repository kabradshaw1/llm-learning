import numpy as np
import time

def naive_relu(x):
  assert len(x.shape) == 2
  x = x.copy()
  for i in range(x.shape[0]):
    for j in range(x.shape[1]):
      x[i, j] = max(x[i, j], 0)
  return x

def naive_add(x, y):
  assert len(x.shape) == 2
  assert x.shape == y.shape
  x = x.copy()
  for i in range(x.shape[0]):
    for j in range(x.shape[1]):
      x[i, j] += y[i, j]
  return x

x = np.array([[1, 10], [3, 6]])

y = np.array([[2, 3], [4, 5]])

z = x + y
z = np.maximum(z, 0.)

t0 = time.time()

