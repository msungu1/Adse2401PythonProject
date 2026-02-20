# Python script to predict sales for a given year (2019)
# based on advertisement and sales data using simple linear regression

# Import the required modules
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression

# Sample dataset
years = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020])
advertisement = np.array([90, 120, 150, 100, 130, 140, 146])
sales = np.array([1000, 1300, 1800, 1200, 1380, 1600, 1790])

# Reshape advertisement data to 2D for sklearn
advertisement_2d = advertisement.reshape(-1, 1)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(advertisement_2d, sales)

# Predict the sales for 2019 given an advertising budget of 200
sales_2019 = model.predict([[200]])
print(f"Sales prediction for the year 2019 with advertising budget of $200: {sales_2019[0]:.2f}")

# Regression line using scipy (requires 1D arrays)
slope, intercept, r_value, p_value, std_err = stats.linregress(advertisement, sales)

def simple_regression(advertisement, sales):
    return slope * advertisement + intercept

# Plot data and regression line
plt.scatter(advertisement, sales, color='blue', label='Data points')
plt.plot(advertisement, intercept + slope*advertisement, color='red', label='Regression line')
plt.xlabel("Advertisement Budget ($)")
plt.ylabel("Sales")
plt.title("Sales vs Advertisement Budget")
plt.legend()
plt.show()
