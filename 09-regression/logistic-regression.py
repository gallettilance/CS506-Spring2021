import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn import datasets
import statsmodels.api as sm

import seaborn as sns; sns.set()

df = pd.read_csv('ats-admissions.csv') 
print(df.head(10))

print()

print("DESCRIBE")
print(df.describe())

df.hist()
plt.show()

df['intercept'] = 1.0
train_cols = df.columns[1:]
train_cols
logit = sm.Logit(df['admit'], df[train_cols])
 
# fit the model
result = logit.fit()

print()
print("SUMMARY")
print(result.summary())
