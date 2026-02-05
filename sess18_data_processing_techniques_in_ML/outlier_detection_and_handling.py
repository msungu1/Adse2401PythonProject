#python script to demonstarte outlier detection and handling using IQR using IQR (interquartile range)


# import the required modules

# import the required modules
import pandas as pd
import numpy as np

# 1. Create sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Eve', 'Frank', 'Grace'],
    'Age': [25, 30, 35, 40, 120, 28],        # 120 is an outlier
    'Salary': [30000, 350900, 40500, 45600, 1005000, 38030]  # 100000 is an outlier
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 2. Function to detect and handle outliers using IQR
def handle_outliers(df, column):
    Q1 = df['Age'].quantile(0.25)
    Q3 = df['Age'].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    print(f"\nColumn: {column}")
    print("Q1:", Q1, "Q3:", Q3, "IQR:", IQR)
    print("Lower Bound:", lower_bound, "Upper Bound:", upper_bound)

    # Detect outliers
    outliers = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
    print("Detected Outliers:\n", outliers)

    # Option A: Remove outliers
    df_no_outliers = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]
    print("DataFrame after removing outliers:\n", df_no_outliers)


    # Option B: Cap outliers
    df_capped = df.copy()
    df_capped[column] = np.where(df_capped['Age'] > upper_bound, upper_bound,
                                 np.where(df_capped['Age'] < lower_bound, lower_bound, df_capped['Age']))
    print("DataFrame after capping outliers:\n", df_capped)

# 3. Apply outlier handling for Age
handle_outliers(df, 'Age')

# 4. Apply outlier handling for Salary
handle_outliers(df, 'Salary')
