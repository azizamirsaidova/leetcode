"""

PCA

1. pre-process data -> make sure data is balanced, no missing value, and all numerical 
2. standardize/normalize data 
3. create a feature vector -> covariance matrix -> how data correlated againts each other
4. create eigen value, vectors 
5. apply eigen values, vectors to covariance matrix
6. get number of principle component
7. show results in dataset/visually via plot

"""


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn
import seaborn as sns
import numpy

from numpy import array, mean, cov
from sklearn.preprocessing import StandardScaler
from numpy.linalg import eig

df = pd.read_csv("fraud_detection_bank_dataset.csv")
sns.displot(df, kde=True, bins=15)

scale = StandardScaler()
scaled_data = scale.fit_transform(df) 

# get the mean for reach column
mean_data = mean(scaled_data.T, axis = 1)

# center column by subtracting column means 
center = scaled_data - mean_data 


# calculate covariance matrix of centered matrix
covariance_matrix = cov(center.T)

#eigndecomposition of covariance matrix
value, vector = eig(covariance_matrix)

projection_original_data = vector.T.dot(covariance_matrix.T)

print(len(scaled_data), len(projection_original_data))