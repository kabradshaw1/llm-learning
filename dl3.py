import numpy as np
import tensorflow as tf

# This will work, where it wouldn't work with tensforflow.
x = np.ones(shape=(2, 2))
x[0, 0] = 0
print(x)


x = tf.ones(shape=(2, 1))
print(x)