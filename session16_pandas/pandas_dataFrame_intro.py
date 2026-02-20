# Python script to introduce Pandas by demonstrating how to create, display, and explore a DataFrame

# Import the required modules
import pandas as pd
import numpy as np

# 1. Create a DataFrame from a dictionary
print("-------------1. Create and display a DataFrame -------------")
data = {
    'Name': ['Abigail', 'Kamau', 'Sharlene', 'Diana', 'Mueni'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['Nakuru', 'Limuru', 'Kisumu', 'Homabay', 'Makueni'],
    'Salary': [55000, 65000, 72000, 48000, 60000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'Finance']
}

employees = pd.DataFrame(data)
print(employees)

# 2. Explore DataFrame attributes
print("\n-------------2. Explore DataFrame attributes -------------")
print("Shape:", employees.shape)
print("Columns:", employees.columns)
print("Index:", employees.index)
print("Data types:\n", employees.dtypes)

# 3. Accessing data
print("\n-------------3. Accessing data -------------")
print("First 2 rows:\n", employees.head(2))
print("Last 2 rows:\n", employees.tail(2))
print("Access a single column (Name):\n", employees['Name'])
print("Access multiple columns (Name and Salary):\n", employees[['Name', 'Salary']])
print("Access a row by index (iloc):\n", employees.iloc[2])
print("Access a row by label (loc):\n", employees.loc[3])

# 4. Filtering and conditional selection
print("\n-------------4. Filtering and conditional selection -------------")
print("Employees with Salary > 60000:\n", employees[employees['Salary'] > 60000])
print("Employees in IT department:\n", employees[employees['Department'] == 'IT'])
print("Employees younger than 30 with Salary > 50000:\n",
      employees[(employees['Age'] < 30) & (employees['Salary'] > 50000)])

# 5. Basic statistical operations
print("\n-------------5. Statistical operations -------------")
print("Average Age:", employees['Age'].mean())
print("Maximum Salary:", employees['Salary'].max())
print("Minimum Salary:", employees['Salary'].min())
print("\nSummary statistics:\n", employees.describe())

# 6. Applying functions
print("\n-------------6. Applying functions -------------")
print("Salary after 10% increase:\n", employees['Salary'].apply(lambda x: round(x * 1.1, 2)))
print("Categorize Salary as High/Low:\n", employees['Salary'].map(lambda x: 'High' if x > 60000 else 'Low'))

# 7. Handling missing data (example)
print("\n-------------7. Handling missing data -------------")
employees_with_na = employees.copy()
employees_with_na.loc[2, 'Salary'] = None  # introduce a missing value
print("DataFrame with missing value:\n", employees_with_na)
print("Fill missing Salary with mean:\n", employees_with_na['Salary'].fillna(employees_with_na['Salary'].mean()))




