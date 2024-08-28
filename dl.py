import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

layers = tf.keras.layers

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

print(train_images.ndim)

print(train_images.shape)

model = keras.Sequential([
  layers.Dense(512, activation='relu'),
  layers.Dense(10, activation='softmax')
])
