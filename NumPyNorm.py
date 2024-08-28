import numpy as np

# Image data processing
# Example image data: 8x8 grayscale image with pixel values ranging from 0 to 255
image = np.array([
    [0, 128, 255, 128, 0, 128, 255, 128],
    [255, 0, 128, 0, 255, 0, 128, 0],
    [128, 255, 0, 255, 128, 255, 0, 255],
    [0, 128, 255, 128, 0, 128, 255, 128],
    [255, 0, 128, 0, 255, 0, 128, 0],
    [128, 255, 0, 255, 128, 255, 0, 255],
    [0, 128, 255, 128, 0, 128, 255, 128],
    [255, 0, 128, 0, 255, 0, 128, 0]
])

# Normalize pixel values to [0, 1]
normalized_image = image / 255.0

print("Normalized Image:\n", normalized_image)

# Feature Scaling for machine learning models
# use cases: when traing models like k-nearest neighbors (KNN) or support vetor machines (SVM), normalization of feature s 
#ensures that all features have equal weight in the distance calculations.
# Example dataset: [height in cm, weight in kg]
data = np.array([
    [180, 80],
    [165, 60],
    [170, 75],
    [160, 50]
])

# Normalize each feature to the range [0, 1]
min_values = np.min(data, axis=0)
max_values = np.max(data, axis=0)
normalized_data = (data - min_values) / (max_values - min_values)

print("Normalized Data:\n", normalized_data)
