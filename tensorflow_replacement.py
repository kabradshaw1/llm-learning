import tensorflow as tf

class NaiveDense:
  def __init__(self, input_size, output_size, activation):
    self.activation = activation

    self.weights = tf.Variable(tf.random.uniform((input_size, output_size)))
    self.biases = tf.Variable(tf.zeros(output_size))

  def __call__(self, inputs):
    return self.activation(tf.matmul(inputs, self.weights) + self.biases)