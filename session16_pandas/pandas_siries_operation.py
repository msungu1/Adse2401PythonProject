# Python script to demonstrate various operations on Pandas Series

# Import the required modules
import pandas as pd
import numpy as np

# 1. Create and display a sample series
print("-------------1. Create and display a sample series -------------")
sales = pd.Series([250, 320, 180, 450, 290, 510],
                  index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
print(sales)

# 2. Basic mathematical operations on the daily sales series
print("\n-------------2. Basic mathematical operations on the daily sales series -------------")
print("Original sales:\n", sales, "\n")

# Scalar operation: increase sales by 10%
print("Sales with a 10% increase:")
sales_increase = sales * 1.1
print(sales_increase, "\n")

# Element-wise operation: subtract 50 from each sale
print("Sales minus 50:")
sales_adjusted = sales - 50
print(sales_adjusted, "\n")

# Element-wise operation: square root of sales
print("Square root of sales:")
sales_sqrt = np.sqrt(sales)
print(sales_sqrt, "\n")


# 3. Combining two Series (Week 1 and Week 2 sales)
print("-------------3. Combining two Series (Week 1 and Week 2 sales) -------------")
week2_sales = pd.Series([260, 330, 200, 470, 310, 530],
                        index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
print("Week 2 sales:\n", week2_sales, "\n")

print("Total sales across two weeks:")
total_sales = sales + week2_sales
print(total_sales)



# 4. Series with Series operations
print("\n-------------4. Series with Series operations -------------")
# Create another series (Week 2 sales)
week2_sales = pd.Series([260, 330, 200, 470, 310, 530], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
print("Week 2 sales:\n", week2_sales, "\n")


# 5. Filtering and conditional operations
print("\n-------------5. Filtering and Conditional Operations -------------")

# Filter sales greater than 300
print("Sales greater than 300:")
print(sales[sales > 300], "\n")

# Filter sales less than or equal to 250
print("Sales less than or equal to 250:")
print(sales[sales <= 250], "\n")

# Multiple conditions: sales between 250 and 400
print("Sales between 250 and 400:")
print(sales[(sales >= 250) & (sales <= 400)], "\n")

# Multiple conditions: sales less than 200 OR greater than 500
print("Sales less than 200 OR greater than 500:")
print(sales[(sales < 200) | (sales > 500)], "\n")

# Using .where() to keep values that meet condition, others become NaN
print("Using .where() to filter sales greater than 300:")
print(sales.where(sales > 300), "\n")

# Using .mask() to replace values that meet condition with NaN
print("Using .mask() to hide sales greater than 300:")
print(sales.mask(sales > 300), "\n")

# Using .query() after converting to DataFrame
print("Using .query() for conditional filtering:")
df_sales = sales.reset_index()
df_sales.columns = ['Day', 'Sales']
print(df_sales.query("Sales > 300"))



# 6. Statistical operations on the Series
print("\n-------------6. Statistical Operations -------------")

# Basic statistics
print("Mean (average sales):", sales.mean())
print("Median sales:", sales.median())
print("Standard deviation of sales:", sales.std())
print("Variance of sales:", sales.var())
print("Minimum sales:", sales.min())
print("Maximum sales:", sales.max(), "\n")

# Describe method (summary statistics)
print("Summary statistics using .describe():")
print(sales.describe(), "\n")

# Value counts (frequency of values)
print("Frequency of sales values:")
print(sales.value_counts(), "\n")

# Correlation and covariance with another Series
week2_sales = pd.Series([260, 330, 200, 470, 310, 530],
                        index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
print("Correlation between Week 1 and Week 2 sales:")
print(sales.corr(week2_sales), "\n")

print("Covariance between Week 1 and Week 2 sales:")
print(sales.cov(week2_sales))

# 7. Applying functions on the Series
print("\n-------------7. Applying Functions on the Series -------------")

# Using built-in NumPy functions (vectorized)
print("Square root of sales using NumPy function:")
print(np.sqrt(sales), "\n")

# Using .apply() with a custom function
def convert_to_thousands(x):
    return x / 1000

print("Sales converted to thousands using .apply():")
print(sales.apply(convert_to_thousands), "\n")

# Using .apply() with a lambda function
print("Sales doubled using lambda in .apply():")
print(sales.apply(lambda x: x * 2), "\n")

# Using .map() for element-wise transformation
print("Sales labeled as 'High' or 'Low' using .map():")
print(sales.map(lambda x: 'High' if x > 300 else 'Low'), "\n")

# Using .apply() with string operations (after converting to string)
print("Appending ' units' to each sales value:")
print(sales.apply(lambda x: str(x) + " units"))



# 7. Missing data operations
print("-------------7. Missing Data Operations -------------")

# Create a Series with missing values
sales_with_na = pd.Series([250, None, 180, 450, None, 510, 380],
                          index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
print("Sales series with missing data:")
print(sales_with_na, "\n")

# Detect missing values
print("Detect missing values (True = missing):")
print(sales_with_na.isna(), "\n")

# Drop missing values
print("Drop missing values:")
print(sales_with_na.dropna(), "\n")

# Fill missing values with mean
print("Fill missing values with mean:")
filled_sales_series = sales_with_na.fillna(sales_with_na.mean())
print(filled_sales_series, "\n")

# Fill missing values with a fixed value
print("Fill missing values with 0:")
print(sales_with_na.fillna(0), "\n")

# Forward fill (propagate last valid value forward)
print("Forward fill missing values:")
print(sales_with_na.ffill(), "\n")

# Backward fill (propagate next valid value backward)
print("Backward fill missing values:")
print(sales_with_na.bfill())
