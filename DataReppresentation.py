import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6])

# Reshape it to a 2x3 array
array_2d = array_1d.reshape(2, 3)

print("Original 1D Array:\n", array_1d)
print("Reshaped to 2D Array:\n", array_2d)

# Extract the first row
first_row = array_2d[0, :]
print("First Row:\n", first_row)

# Extract the second column
second_column = array_2d[:, 1]
print("Second Column:\n", second_column)

# Extract a 2x2 sub-array
sub_array = array_2d[0:2, 0:2]
print("2x2 Sub-array:\n", sub_array)
