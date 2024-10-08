import tensorflow as tf
x = tf.Variable(tf.random.uniform((2, 2)))
with tf.GradientTape() as tape:
 y = 2 * x + 3
grad_of_y_wrt_x = tape.gradient(y, x) 
print(grad_of_y_wrt_x)