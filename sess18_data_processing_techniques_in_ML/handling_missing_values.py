import pandas as pd
import numpy as np

# 1. Create a sample dataset with missing values
data = {
    'Name': ['Abigael', 'Mueni', 'Eve', 'David'],
    'Age': [25, np.nan, 30, 28],
    'Score': [85, 90, np.nan, 88]
}

df = pd.DataFrame(data)
print("Original DataFrame with missing values:\n", df)

# 2. Detect missing values
print("\nCheck for missing values:\n", df.isnull())

# 3. Drop rows with missing values
df_drop = df.dropna()
print("\nDataFrame after dropping missing values:\n", df_drop)

# 4. Fill missing values with a constant
df_fill_const = df.fillna(0)
print("\nDataFrame after filling missing values with 0:\n", df_fill_const)

# 5. Fill missing values with column mean (fixed assignment)
df_fill_mean = df.copy()
df_fill_mean['Age'] = df_fill_mean['Age'].fillna(df['Age'].mean())
df_fill_mean['Score'] = df_fill_mean['Score'].fillna(df['Score'].mean())
print("\nDataFrame after filling missing values with column mean:\n", df_fill_mean)

# 6. Forward fill (fixed)
df_ffill = df.ffill()
print("\nDataFrame after forward fill:\n", df_ffill)

# 7. Backward fill (fixed)
df_bfill = df.bfill()
print("\nDataFrame after backward fill:\n", df_bfill)
