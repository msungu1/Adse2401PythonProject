#python file to demonstarte heirachical clustering algorithim

#import the required module
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

#generate a synthetic customer dataset with income  and spending score

data = {
    'Income': np.random.randint(20000,100000, 50),
    'Spending score': np.random.randint(1, 50, 50)


}
#create a dataframe and display the first 10 rows
df = pd.DataFrame(data)
print(f"the first 10 rows of the customer income and spending score are: \n{df[:10]}")

#visualize the entire  dataset
plt.figure(figsize=(10,8))
plt.scatter(df['Income'], df['Spending score'])
plt.title('synthetic Dataset of Income and Spending Score')
plt.xlabel('Income')
plt.ylabel('Spending score')
plt.show()

#create a dendogram
plt.figure(figsize=(10,8))
dendrogram = sch.dendrogram(sch.linkage(df, method='ward'))
plt.title('Dendrogram of Income and Spending Score')
plt.xlabel('samples')
plt.ylabel('Euclidean Distance!')
plt.show()


# apply agglomerative clustering

hc = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
df['Cluster'] = hc.fit_predict(df)
# plot the cluster
plt.figure(figsize=(10,6))
plt.scatter(df['Income'], df['Cluster'],cmap='viridis')
plt.title('heirachcal_clustering:income vs Spending Score')
plt.xlabel('Income')
plt.xlabel('Spending Score')
plt.show()