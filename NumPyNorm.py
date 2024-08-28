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

# Example time series data: daily temperatures over a week
temperatures = np.array([30, 32, 34, 31, 29, 35, 33])

# Normalize temperatures to [0, 1]
normalized_temperatures = (temperatures - np.min(temperatures)) / (np.max(temperatures) - np.min(temperatures))

print("Normalized Temperatures:\n", normalized_temperatures)

# Example term frequency (TF) counts for words in a document
tf = np.array([3, 5, 2, 7])

# Example inverse document frequency (IDF) values
idf = np.array([0.3, 0.7, 0.5, 0.4])

# Calculate TF-IDF
tf_idf = tf * idf

# Normalize TF-IDF to unit length (L2 normalization)
tf_idf_normalized = tf_idf / np.linalg.norm(tf_idf)

print("Normalized TF-IDF:\n", tf_idf_normalized)

# Example input data: features in a dataset
data = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
    [5.0, 6.0]
])

# Normalize data to range [-1, 1] (assuming features are originally [0, 1])
normalized_data = 2 * (data - np.min(data)) / (np.max(data) - np.min(data)) - 1

print("Normalized Data:\n", normalized_data)