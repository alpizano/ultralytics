import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import explained_variance_score, \
    mean_absolute_error, \
    median_absolute_error
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# read in .csv
df = pd.read_csv('pred_data.csv')
print(df)

# turn data frame into array
dataset = df.values

# first ten columns
X = dataset[:,0:9]

# pocket column
Y = dataset[:,9]
