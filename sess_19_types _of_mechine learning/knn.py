from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Example dataset: 19 samples per fruit
# Features: [weight, size_ratio]
# Labels: 0 = Apple, 1 = Orange, 2 = Banana

apples = [
    [150, 0.65], [160, 0.70], [155, 0.68], [145, 0.60], [170, 0.72],
    [165, 0.66], [158, 0.64], [152, 0.62], [148, 0.61], [172, 0.75],
    [168, 0.67], [162, 0.69], [157, 0.63], [149, 0.59], [151, 0.60],
    [159, 0.65], [161, 0.71], [166, 0.73], [153, 0.62]
]

oranges = [
    [130, 0.60], [120, 0.58], [135, 0.62], [140, 0.63], [125, 0.57],
    [138, 0.61], [132, 0.59], [128, 0.56], [136, 0.64], [134, 0.60],
    [129, 0.58], [137, 0.62], [133, 0.59], [126, 0.57], [131, 0.61],
    [127, 0.55], [139, 0.63], [124, 0.56], [122, 0.57]
]

bananas = [
    [200, 0.30], [210, 0.32], [190, 0.28], [205, 0.31], [195, 0.29],
    [215, 0.33], [198, 0.30], [202, 0.31], [207, 0.32], [193, 0.29],
    [212, 0.34], [196, 0.28], [199, 0.30], [203, 0.31], [208, 0.32],
    [194, 0.29], [201, 0.30], [206, 0.31], [211, 0.33]
]

# Combine dataset
X = np.array(apples + oranges + bananas)
y = np.array([0]*19 + [1]*19 + [2]*19)  # 57 labels total

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train KNN classifier
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(x_train, y_train)

# Evaluate the model
y_pred = knn.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Model accuracy on test set:", accuracy)
print("Confusion Matrix:\n", conf_matrix)

# Map labels back to fruit names
fruit_map = {0: "Apple", 1: "Orange", 2: "Banana"}

# Example predictions
test_samples = [[150, 0.66], [125, 0.59], [205, 0.31]]
predictions = knn.predict(test_samples)

for sample, pred in zip(test_samples, predictions):
    print(f"Fruit with features {sample} is classified as: {fruit_map[pred]}")

# --- Visualization of decision boundaries ---
x_min, x_max = X[:, 0].min() - 10, X[:, 0].max() + 10
y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 1),
                     np.arange(y_min, y_max, 0.01))

# Train again on full dataset for visualization
knn_plot = KNeighborsClassifier(n_neighbors=k)
knn_plot.fit(X, y)

# Predict on the mesh grid
Z = knn_plot.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10, 6))
cmap_light = ListedColormap(['#ffaaaa', '#aaffaa', '#aaaaff'])
cmap_bold = ListedColormap(['#ff0000', '#00ff00', '#0000ff'])

plt.contourf(xx, yy, Z, alpha=0.3, cmap=cmap_light)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolors='k', s=50)

plt.xlabel('Weight (grams)')
plt.ylabel('Size Ratio')
plt.title(f"KNN Decision Boundary with K={k}")
plt.show()
