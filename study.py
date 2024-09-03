import tensorflow as tf
import numpy as np
x = np.ones(shape=(2, 2))
print(x)
x[0, 0] = 0
print(x)
y = tf.ones(shape=(2, 2))
print(y)