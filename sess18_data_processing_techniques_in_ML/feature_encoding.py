# python script to demonstrate one-hot and encoding and label encoding on a single dataset

# Python script to demonstrate one-hot encoding and label encoding

# Import required modules
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# 1. Create sample dataset
data = pd.DataFrame({
    'colour': ['Red', 'Blue', 'Green', 'Red', 'Blue'],
    'size': ['Small', 'Medium', 'Large', 'Small', 'Large'],
    'city': ['London', 'Paris', 'London', 'New York', 'Paris']
})

# Display the original dataset
print("Original Dataset")
print("-" * 55)
print(data)
print("-" * 55)

# 2. Label Encoding (example: encode 'size')
label_encoder = LabelEncoder()
data['size_label'] = label_encoder.fit_transform(data['size'])

print("\nDataset after Label Encoding 'size'")
print("-" * 55)
print(data)
print("-" * 55)

# 3. One-Hot Encoding (example: encode 'colour' and 'city')
one_hot_encoder = OneHotEncoder(sparse_output=False)
encoded = one_hot_encoder.fit_transform(data[['colour', 'city']])

# Convert back to DataFrame with proper column names
encoded_df = pd.DataFrame(
    encoded,
    columns=one_hot_encoder.get_feature_names_out(['colour', 'city'])
)

# Concatenate with original dataset
data_encoded = pd.concat([data, encoded_df], axis=1)

print("\nDataset after One-Hot Encoding 'colour' and 'city'")
print("-" * 55)
print(data_encoded)
print("-" * 55)

#------visualizing encoded
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)