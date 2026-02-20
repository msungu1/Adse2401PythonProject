# Python script to demonstrate the use of Decision Tree for classification
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Sample dataset of fruits
# Features: [weight in grams, colour score]
# Labels: 0 -> Apple, 1 -> Orange, 2 -> Banana
X = np.array([
    # Apples
    [150, 0.80], [170, 0.75], [140, 0.85],
    [160, 0.82], [180, 0.78], [145, 0.88], [155, 0.76], [190, 0.80], [135, 0.87], [175, 0.79],

    # Oranges
    [130, 0.60], [120, 0.58], [115, 0.65],
    [140, 0.55], [125, 0.66], [110, 0.62], [100, 0.50], [135, 0.59], [145, 0.68], [105, 0.53],

    # Bananas
    [180, 0.55], [200, 0.50], [220, 0.48],
    [140, 0.42], [135, 0.45], [150, 0.46], [125, 0.51], [110, 0.43], [95, 0.57], [100, 0.49],
])

y = np.array([
    # Apples
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    # Oranges
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    # Bananas
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2
])

# Split dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize Decision Tree Classifier
clf = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=42)

# Train the model
clf.fit(x_train, y_train)

# Make predictions
y_pred = clf.predict(x_test)

# Define feature and target names
feature_names = ["Weight", "Colour Score"]
target_names = ["Apple", "Orange", "Banana"]

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classf_report = classification_report(y_test, y_pred, target_names=target_names)

print("Model accuracy on test set:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", classf_report)

# Example predictions
test_samples = [[150, 0.82], [120, 0.59], [200, 0.49]]
predictions = clf.predict(test_samples)

fruit_map = {0: "Apple", 1: "Orange", 2: "Banana"}
for sample, pred in zip(test_samples, predictions):
    print(f"Fruit with features {sample} is classified as: {fruit_map[pred]}")

# Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=feature_names, class_names=target_names, filled=True)
plt.show()

