# Python ML script to use logistic regression model
# to determine whether a person/customer buys or not

# Import the required modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Example dataset (replace with your own or load from CSV)
data = {
    'Age': [22, 25, 47, 52, 46, 56, 55, 60, 62, 61],
    'EstimatedSalary': [20000, 25000, 50000, 52000, 48000, 60000, 58000, 62000, 65000, 64000],
    'Purchased': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# 1. Display the dataset
print("Dataset:\n", df)

# 2. Separate features (X) and target (y)
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']
print("\nFeatures (X):\n", X)
print("\nTarget (y):\n", y)

# 3. Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("\nTraining Features:\n", X_train)
print("\nTesting Features:\n", X_test)
print("\nTraining Target:\n", y_train)
print("\nTesting Target:\n", y_test)

# 4. Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)


#initialize the logistic regression model
log_reg = LogisticRegression()
# 6. Predictions
y_pred = model.predict(X_test)

# 7. Evaluation
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
