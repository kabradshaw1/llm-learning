import numpy as np

num_samples_per_class = 1000
negative_samples = np.random.multivariate_normal(
  mean=[0, 3], cov=[[1, 0.5], [0.5, 1]], size=num_samples_per_class)

positive_samples = np.random.multivariate_normal(
  mean=[3, 0], cov=[[1, 0.5], [0.5, 1]], size=num_samples_per_class)

print (negative_samples, positive_samples) 