import tensorflow as tf
import numpy as np
x = np.ones(shape=(2, 2))
print(x)
x[0, 0] = 0
print(x)
y = tf.ones(shape=(2, 2))
print(y)

# a = tf.ones((2, 2))
# b = tf.square(a)
# c = tf.sqrt(a)
# d = b + c
# e = tf.matmul(a, b)

# This is what tenorflow does that numpy doesn't
input_var = tf.Variable(initial_value=3.)
with tf.GradientTape() as tape:
 result = tf.square(input_var)
gradient = tape.gradient(result, input_var)

# print(gradient)

time = tf.Variable(0.)
with tf.GradientTape() as outer_tape:
  with tf.GradientTape() as inner_tape:
    position = 4.9 * time ** 2
    print(position)
  speed = inner_tape.gradient(position, time)
  print(speed)
acceleration = outer_tape.gradient(speed, time) 
print(acceleration)