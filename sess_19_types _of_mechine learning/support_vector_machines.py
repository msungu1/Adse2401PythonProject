# Import required modules
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# For reproducibility
np.random.seed(42)

# -----------------------------
# Create synthetic dataset
# -----------------------------

# Apples (lighter, smaller)
weight_apples = np.random.normal(loc=150, scale=15, size=50)
size_apples = np.random.normal(loc=7, scale=1, size=50)
label_apples = np.zeros(50)   # 0 = Apple

# Oranges (heavier, larger)
weight_oranges = np.random.normal(loc=180, scale=15, size=50)
size_oranges = np.random.normal(loc=9, scale=1, size=50)
label_oranges = np.ones(50)   # 1 = Orange

# Combine data
X = np.column_stack((
    np.concatenate((weight_apples, weight_oranges)),
    np.concatenate((size_apples, size_oranges))
))
y = np.concatenate((label_apples, label_oranges))

# -----------------------------
# Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Train SVM model
# -----------------------------
svm_clf = SVC(kernel='linear', C=1.0)
svm_clf.fit(X_train, y_train)

# -----------------------------
# Predictions & Evaluation
# -----------------------------
y_pred = svm_clf.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["Apple", "Orange"]))

# -----------------------------
# Plot decision boundary
# -----------------------------
def plot_decision_boundary(X, y, model):
    plt.figure(figsize=(8, 6))

    # Scatter data points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors='k')

    # Create grid
    x_min, x_max = X[:, 0].min() - 5, X[:, 0].max() + 5
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 300),
        np.linspace(y_min, y_max, 300)
    )

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot boundary
    plt.contourf(xx, yy, Z, alpha=0.2, cmap=plt.cm.Paired)

    # Support vectors
    plt.scatter(
        model.support_vectors_[:, 0],
        model.support_vectors_[:, 1],
        s=100,
        facecolors='none',
        edgecolors='k'
    )

    plt.xlabel("Weight (grams)")
    plt.ylabel("Size (cm)")
    plt.title("SVM Decision Boundary (Apple vs Orange)")
    plt.show()

plot_decision_boundary(X, y, svm_clf)
