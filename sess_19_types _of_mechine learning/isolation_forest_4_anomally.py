# python script to demonstarte anomally detection using isolation forest

#import the required modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from numpy.ma.core import anomalies

#generate a synthetic dataset for income and speding score
np.random.seed()


#create normal data point around income -(30k - 70k) and spending score (20 - 80)
income = np.random.normal(50_000, 10000, 300)
spending_score = np.random.normal(50, 15, 300)
X = np.column_stack((income, spending_score))

#introduce the anomalities with higher or lower income and spending
anomalies = np.array([[100_000,10],[20_000,90], [80_000, 75],[35000,5],[60000,95]])
x = np.vstack((X,anomalies))


#convert the data into data frame  for ease of use
df = pd.DataFrame(data=X, columns=['income', 'spending_score'])


print(f"First five rows:\n{df.head(5)}")

#Apply isolation forest
iso_forest =IsolationForest(contamination=.02, random_state=42)
df['Anomaly score'] = iso_forest.fit_predict(df[['income','spending_score']])

#separate the normal points and anomalies for visualisation
normal = df[df['Anomaly score']==1]
anomaly = df[df['Anomaly score']==-1]

#plot the result
plt.figure(figsize=(10,8))
plt.scatter(normal['income'],normal['spending_score'],color='blue',label='Normal',alpha=0.7)

plt.xlabel('income')
plt.ylabel('spending score')
plt.title('Normal vs anomaly score')
plt.grid(True)
plt.legend()
plt.show()
