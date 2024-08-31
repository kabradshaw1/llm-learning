import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

layers = keras.layers

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
print(train_labels)

model = keras.Sequential([
  layers.Dense(512, activation='relu'),
  layers.Dense(10, activation='softmax')
])

model.compile(optimizer="rmsprop", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
# train_images = train_images.reshape((60000, 28 * 28))
# train_images = train_images.astype("float32") / 255
# test_images = test_images.reshape((10000, 28 * 28))
# test_images = test_images.astype("float32") / 255

# print(train_images.ndim)

# print(train_images.shape)





# model.fit(train_images, train_labels, epochs=5, batch_size=128)

# test_digits = test_images[0:10]
# predictions = model.predict(test_digits)
# print(predictions[0])

# # Why are they using the pyshell?