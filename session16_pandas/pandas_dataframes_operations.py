import pandas as pd

# 1. Create employees dataframe
print("---------1. Create employees dataframe")

employees = pd.DataFrame({
    'EmployeeId': [2000, 2001, 2002, 2003, 2004],
    'Name': ['Abigail', 'Kamau', 'Sharlene', 'Diana', 'Mueni'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['Nakuru', 'Limuru', 'Kisumu', 'Homabay', 'Makueni'],
    'Salary': [55000, 65000, 72000, 48000, 60000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'Finance']
})

# 2. Create sales dataframe
print("---------2. Create sales dataframe")

sales = pd.DataFrame({
    'EmployeeId': [2000, 2001, 2002, 2003, 2004],
    'Q1_sales': [18000, 24000, 21000, 12000, 1600],
    'Q2_sales': [15000, 25000, 28000, 30000, 5600],
    'Q3_sales': [16000, 24000, 34000, 13600, 16500],
})

print(employees)
print(sales)

# 3. Filtering
print("---------3. Filtering employees with Salary > 60000")
print(employees[employees['Salary'] > 60000])

# 4. Grouping
print("---------4. Grouping employees by Department and calculating average salary")
print(employees.groupby('Department')['Salary'].mean())


# 5. Merging
print("---------5. Merging employees with sales data")
combined = pd.merge(employees, sales, on='EmployeeId')
merged = pd.merge(employees, sales, on='EmployeeId')
print("merged employess and sales dataframe ".center(55, '-'))
print(combined)

# 6. Adding new column (Total Sales)
print("---------6. Adding Total Sales column")
merged['Total_sales'] = merged[['Q1_sales', 'Q2_sales', 'Q3_sales']].sum(axis=1)
print(merged[['Name', 'Department', 'Total_sales']])

# 7. Sorting
print("---------7. Sorting employees by Total Sales descending")
print(merged.sort_values(by='Total_sales', ascending=False))

# 8. Aggregation
print("---------8. Aggregating sales by Department")
print(merged.groupby('Department')['Total_sales'].sum())

# 9. Selecting specific columns
print("---------9. Selecting Name and City columns")
print(employees[['Name', 'City']])
