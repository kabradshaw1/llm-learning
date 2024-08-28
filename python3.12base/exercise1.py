import numpy as np

array = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

revserse_array = array[::-1]

reshape_array = array.reshape(2, 5)

sum = array.sum()

mean = array.std()

print("Original Array:\n", array)
print("Reverse Array:\n", revserse_array)
print("Reshaped Array:\n", reshape_array)
print("Sum of Array:\n", sum)
print("Mean of Array:\n", mean)
