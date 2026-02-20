# Python file to demonstrate K-means clustering
# for customer segmentation based on income and spending score

# Import required modules
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate a synthetic dataset
X, y = make_blobs(n_samples=300, centers=3, cluster_std=0.5, random_state=42)

# Convert the data to a DataFrame for ease of use
df = pd.DataFrame(X, columns=["Income", "Spending Score"])

# Display the first 10 rows of the DataFrame
print(f"The first 10 rows of the income and spending data frame:\n{df.head(10)}")

# Visualize the dataset
plt.scatter(df["Income"], df["Spending Score"])
plt.title("Synthetic Dataset: Income vs Spending Score")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(df)

# Add cluster labels to the DataFrame
df['Cluster'] = kmeans.labels_

# Plot the clusters
plt.scatter(df["Income"], df["Spending Score"], c=df['Cluster'], cmap='viridis', marker='o')
plt.title("K-means Clusters")
plt.xlabel("Income")
plt.ylabel("Spending Score")

# Plot the cluster centers
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=200, alpha=0.75, label='Centroids')

plt.legend()
plt.show()

# Print inertia
print(f"\nInertia: {kmeans.inertia_}")

# Inertia is the sum of squared distances between each point and its assigned cluster center.
# Lower values indicate tighter clusters.
