import numpy as np
# So this library is used for scaling.
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Tensorflow will get used more in deep learning.
import tensorflow as tf

# NumPy can be used in data processing. 
#  I can handle missing values.  NumPy provides function to identify, and and replace missing values within a dataset.
# I expect most of the time I will be importing this data from a file, but for now I will create a numpy array with missing values.
data = np.array([
    [2000, 3, 500000],
    [1500, 2, 350000],
    [np.nan, 3, 400000],
    [1800, np.nan, 420000],
    [1700, 2, np.nan]
]) # I learned here that np has the array method to create a numpy array.  I also learned that np.nan is used to represent missing values.

print("Original Data:\n", data)

missing_data = np.isnan(data) # I leaned that np.isnan converts the data to a boolean array, where True indicates missing values.
print("Missing Data (True indicates missing):\n", missing_data)

# Calculate the mean of each column, ignoring nan values
mean_values = np.nanmean(data, axis=0)

# Replace nan with the mean value of the corresponding column
data_imputed = np.where(np.isnan(data), mean_values, data)

print("Data after imputing missing values with column mean:\n", data_imputed)

# Feature Scaling.  Effectively, this is the process of normalizing the range of independent variables or features of data.
data = np.array([[2000, 3], [1500, 2], [3000, 4], [1200, 2]])

scaler = StandardScaler()
data_normalized = scaler.fit_transform(data)

print("Normalized Data:\n", data_normalized)

# Example data: [age, income in thousands]
data = np.array([[25, 40000], [45, 80000], [35, 60000], [50, 90000]])

# Min-Max Scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

print("Scaled Data:\n", scaled_data)

# Example data: [height in cm, weight in kg]
data = np.array([[180, 80], [165, 60], [170, 75], [160, 50]])

# Standard Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Apply PCA
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

print("PCA Transformed Data:\n", pca_data)

# Tree-based Algorithms
# Algorithms: Decision Trees, Random Forests, Gradient Boosting Machines
# Why Scale?: Tree based algorithms are typcially less sensi
# Example data: [years of experience, income in thousands]
data = np.array([[2, 50], [5, 80], [7, 120], [10, 150]])
labels = np.array([0, 0, 1, 1])  # Binary classification labels

# Split data
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.25)

# Scaling (though not strictly necessary for trees)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train RandomForest
clf = RandomForestClassifier()
clf.fit(X_train_scaled, y_train)

print("Model Accuracy:", clf.score(X_test_scaled, y_test))

# Example data: [height in cm, weight in kg]
data = np.array([[180, 80], [165, 60], [170, 75], [160, 50]])
labels = np.array([1, 0, 1, 0])  # Binary classification labels

# Standard Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Define a simple neural network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile and train the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(scaled_data, labels, epochs=10, batch_size=1)

