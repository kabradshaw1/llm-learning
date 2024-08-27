import numpy as np

# NumPy can be used in data processing. 
#  I can handle missing values.  NumPy provides function to identify, and and replace missing values within a dataset.
data = np.array([
    [2000, 3, 500000],
    [1500, 2, 350000],
    [np.nan, 3, 400000],
    [1800, np.nan, 420000],
    [1700, 2, np.nan]
])

print("Original Data:\n", data)

missing_data = np.isnan(data)
print("Missing Data (True indicates missing):\n", missing_data)

# Calculate the mean of each column, ignoring nan values
mean_values = np.nanmean(data, axis=0)

# Replace nan with the mean value of the corresponding column
data_imputed = np.where(np.isnan(data), mean_values, data)

print("Data after imputing missing values with column mean:\n", data_imputed)


# Feature Scaling.  Effectively, this is the process of normalizing the range of independent variables or features of data.