import matplotlib.pyplot as plt
from tensorflow import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.ndim)
