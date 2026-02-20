#import the required modules
import pandas as pd
import numpy as np

#1. Create a Pandas series from a list
print("__________1. Create a Pandas series from a list -------")
temperatures = [72, 68, 75, 79, 83, 77, 70]
temp_series = pd.Series(temperatures, name="Temperature")
print(f"Series name: {temp_series.name}")
print(f"Series type: {type(temp_series)}")
print(f"Series data type (dtype): {temp_series.dtype}")
print(temp_series)

#2. Create a series with a custom index
print("\n-----------------2. Create a Pandas series with a custom index ---------")
days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
temp_series_index = pd.Series(temperatures, index=days, name="Temperature by Day")
print(temp_series_index)

#3. Access data by index label
print("\n-----------------3. Access data by index label ---------")
print("Temperature on Monday:", temp_series_index['Mon'])
print("Temperature on Friday:", temp_series_index['Fri'])

#4. Access data by position
print("\n-----------------4. Access data by position ---------")
print("First element:", temp_series_index.iloc[0])
print("Last element:", temp_series_index.iloc[-1])

#5. Perform operations on the series
print("\n-----------------5. Perform operations on the series ---------")
print("Average temperature:", temp_series_index.mean())
print("Maximum temperature:", temp_series_index.max())
print("Minimum temperature:", temp_series_index.min())

#6. Create a series from a NumPy array
print("\n-----------------6. Create a Pandas series from a NumPy array ---------")
np_array = np.array([10, 20, 30, 40, 50])
num_series = pd.Series(np_array, name="Numbers")
print(num_series)

# acess series data

print("\n-----------------6. access sires data ---------")
print(f"using the index location 'iloc':", temp_series_index.iloc[0])
print(f"first temprature: {temp_series_index.iloc[0]} degrees Fahrenheit")
print(f"second temprature: {temp_series_index.iloc[1]} degrees Celsius")
print()

print(f"using the lable index 'loc()' function")
print(f"Monday's temprature: {temp_series_index.iloc[0]} degrees Fahrenheit")
print(f"friday's temprature: {temp_series_index.iloc[1]} degrees Celsius")

print("-" *50)


# siries attributes
print("\n----5. series Attribute-------------")
print(f"shape: {temp_series_index.shape}")
print(f"size: {temp_series_index.size}")
print(f"values: {temp_series_index.values}")
print(f"index: {temp_series_index.index}")
print("_"*50)
#7. Boolean indexing
print("\n-----------------7. Boolean indexing ---------")
print("Days with temperature above 75:")
print(temp_series_index[temp_series_index > 75])

#8. Access multiple elements by index labels
print("\n-----------------8. Access multiple elements by index labels ---------")
print(temp_series_index[['Mon', 'Wed', 'Fri']])

#9. Access a range of elements by position
print("\n-----------------9. Access a range of elements by position ---------")
print(temp_series_index.iloc[1:4])  # Tue to Thur

#10. Conditional selection with multiple conditions
print("\n-----------------10. Conditional selection with multiple conditions ---------")
print("Days with temperature between 70 and 80:")
print(temp_series_index[(temp_series_index >= 70) & (temp_series_index <= 80)])

#11. Using .loc and .iloc explicitly
print("\n-----------------11. Using .loc and .iloc ---------")
print("Access with .loc (label-based):", temp_series_index.loc['Sun'])
print("Access with .iloc (position-based):", temp_series_index.iloc[6])

#12. Access first few and last few elements
print("\n-----------------12. Access first few and last few elements ---------")
print("First 3 days:\n", temp_series_index.head(3))
print("Last 2 days:\n", temp_series_index.tail(2))
