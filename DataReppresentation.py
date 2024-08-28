import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6])

# Reshape it to a 2x3 array
array_2d = array_1d.reshape(2, 3)

print("Original 1D Array:\n", array_1d)
print("Reshaped to 2D Array:\n", array_2d)