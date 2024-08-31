import numpy as np

x = np.random.random((32, 10))
print('x:', x)
y = np.random.random((10,))
print('before expand', y.shape)
print('y:', y)
y = np.expand_dims(y, axis=0)
print('after expand', y.shape)
print('y after expand:', y)

y = np.concatenate([y] * 32, axis=0)
print('y after concatenate:', y)