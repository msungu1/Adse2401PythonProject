# python script to demomnstrate feature scaling
# Python script to demonstrate feature scaling

# Python script to demonstrate feature scaling

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# 1. Create a sample dataset
data = pd.DataFrame({
    'height_cm': [150, 160, 170, 180, 190, 155, 162, 167, 132, 157, 174, 145],
    'weight_kg': [50, 60, 70, 80, 90, 67, 68, 89, 90, 76, 67, 56],
    'income': [50000, 60000, 70000, 80000, 90000, 67000, 68000, 89000, 90000, 76000, 67000, 56000]
})

print("Original Dataset")
print("-" * 55)
print(data)

# 2. Plot original data distribution
data.hist(bins=10, figsize=(10, 5))
plt.suptitle("Original Data Distribution", fontsize=14)
plt.show()

# 3. Standardize the features using StandardScaler
scaler = StandardScaler()
data_standardized = pd.DataFrame(
    scaler.fit_transform(data),
    columns=data.columns
)

print("\nDataset after Standardization (Z-score)")
print("-" * 55)
print(data_standardized)
# Plot the standard scaled data distributions
fig, ax = plt.subplots(2, 3, figsize=(18, 10))
# Standardised data
ax[0, 0].hist(data['height_standardised'], bins=5, color='lightblue', edgecolor='black')
ax[0, 0].set_title('Standardised Height')
ax[0, 1].hist(data['weight_standardised'], bins=5, color='salmon', edgecolor='black')
ax[0, 1].set_title('Standardised Weight')
ax[0, 2].hist(data['income_standardised'], bins=5, color='lightgreen', edgecolor='black')
ax[0, 2].set_title('Standardised Income')

# Min-Max scaled data
ax[1, 0].hist(data['height_minmax'], bins=5, color='lightblue', edgecolor='black')
ax[1, 0].set_title('Min-Max Height')
ax[1, 1].hist(data['weight_minmax'], bins=5, color='salmon', edgecolor='black')
ax[1, 1].set_title('Min-Max Weight')
ax[1, 2].hist(data['income_minmax'], bins=5, color='lightgreen', edgecolor='black')
ax[1, 2].set_title('Min-Max Income')

# Specify the layout and display
plt.tight_layout()
plt.show()
