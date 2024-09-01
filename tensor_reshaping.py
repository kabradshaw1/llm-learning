import tensorflow as tf
from tensorflow import keras

layers = keras.layers

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_images = train_images.reshape((60000, 28 * 28))