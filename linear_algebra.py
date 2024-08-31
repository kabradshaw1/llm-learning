import numpy as np

def naive_relu(x):
  assert len(x.shape) == 2
  x = x.copy()
  for i in range(x.shape[0]):
    for j in range(x.shape[1]):
      x[i, j] = max(x[i, j], 0)
  return x

x = np.array([[1, -1], [-1, 1]])

print(naive_relu(x))