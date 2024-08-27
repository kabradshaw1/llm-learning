import numpy as np
from sklearn.preprocessing import StandardScaler

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

# Normalization: Normalize your data to make sure all features contribute equally to the model.