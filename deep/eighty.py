import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Generate two classes of random points in a 2d plane
num_samples_per_class = 1000
# This will be the firset set of points with a, so the cluster of points
# will look similar for these two classes, but with different mean
negative_samples = np.random.multivariate_normal(
  mean=[0, 3], cov=[[1, 0.5], [0.5, 1]], size=num_samples_per_class)

positive_samples = np.random.multivariate_normal(
  mean=[3, 0], cov=[[1, 0.5], [0.5, 1]], size=num_samples_per_class)

# make the 2 arrays into a single array
inputs = np.vstack((negative_samples, positive_samples)).astype(np.float32)

# Create the target labels for the two classes
targets = np.vstack((np.zeros((num_samples_per_class, 1), dtype="float32"),
  np.ones((num_samples_per_class, 1), dtype="float32")))

plt.scatter(inputs[:, 0], inputs[:, 1], c=targets[:, 0])
plt.show()

# input_dim = 2
# output_dim = 1
# W = tf.Variable(initial_value=tf.random.normal(shape=(input_dim, output_dim)))
# b = tf.Variable(initial_value=tf.zeros(shape=(output_dim,)))

# def model(inputs):
#   return tf.matmul(inputs, W) + b

# def square_loss(targets, predictions):
#   per_sample_losses = tf.square(targets - predictions)
#   return tf.reduce_mean(per_sample_losses)

# learning_rate = 0.1
# def training_step(inputs, targets):
#   with tf.GradientTape() as tape:
#     predictions = model(inputs)
#     loss = square_loss(targets, predictions)
#   grad_W, grad_b = tape.gradient(loss, [W, b])
#   W.assign_sub(grad_W * learning_rate)
#   b.assign_sub(grad_b * learning_rate)
#   return loss

# for step in range(40):
#   loss = training_step(inputs, targets)
#   print("Loss at step {:03d}: {:.3f}".format(step, loss))

# predictions = model(inputs)
# plt.scatter(inputs[:, 0], inputs[:, 1], c=predictions[:, 0] > 0.5)
# plt.show()
