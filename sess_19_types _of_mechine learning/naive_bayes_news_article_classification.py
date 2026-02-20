# Python file to demonstrate Naive Bayes algorithm for News article classification
# (20 newsgroups). It demonstrates Multinomial Naive Bayes

# Import the required modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, ConfusionMatrixDisplay
from sklearn.pipeline import Pipeline

# 1. Load data (subset of categories for faster demo)
categories = [
    'rec.sport.hockey',
    'rec.sport.baseball',
    'sci.space',
    'sci.med',
    'talk.politics.guns',
    'comp.graphics',
    'comp.os.ms-windows.misc',
]

print("Loading data...")
data = fetch_20newsgroups(subset='all', categories=categories, remove=('headers', 'footers', 'quotes'), random_state=42)

X = data.data
y = data.target

target_names = data.target_names

print(f"Number of documents: {len(y)}")
print(f"Number of classes: {len(target_names)}")
print()

# 2. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
print(f"Training set size: {len(X_train):,} documents\ntest set size: {len(X_test):,} documents\n")


#create pipleine
pipeline = Pipeline([
    (
        'tfidf',TfidfVectorizer(
        max_df=0.95,
        min_df=5,
        stop_words='english',
        ngram_range=(1, 2),
    )
    ),
    ('clf', MultinomialNB(alpha=.05)),
])

# 4train model
print("Training the Naive Bayes clssification/model...")
pipeline.fit(X_train, y_train)

#5. make the predictions and evaluate them
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, target_names=target_names,digits=3)

#display the evalaution metrics
print(f"naive bayes accuracy: {accuracy:.2f}")
print(f"confusion matrix:\n{cm}")
print(f"classification report:\n{class_report}")

#visualize  the result
plt.figure(figsize = (10,8))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
disp.plot(
    cmap='Blues',
    values_format='d',
    xticklabels=target_names,
    yticklabels=target_names,
    cbar_kws ={'label': 'propotion'}
)
plt.figure(figsize=(10, 8))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
disp.plot(cmap='Blues', values_format='d')
plt.title("Confusion Matrix - Multinomial Naive Bayes\n(20 Newsgroups subset)", fontsize=14, pad=20)
plt.tight_layout()
plt.show()
