# Python script to analyze and predict unemployment rate based on GDP
# using Polynomial Regression

# import required modules
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# get the path to the CSV file
file_path = os.path.abspath(
    os.path.join(os.getcwd(), "..", "files", "gdp_unemployment.csv")
)

# load the dataset
data = pd.read_csv(file_path)

# 🔹 clean column names (IMPORTANT FIX)
data.columns = data.columns.str.strip()

# 🔹 optional: see column names (for debugging)
print("Columns found:", data.columns.tolist())

# extract GDP (independent variable) and Unemployment Rate (dependent variable)
gdp = data.iloc[:, 0].values.reshape(-1, 1)
unemployment_rate = data.iloc[:, 1].values.reshape(-1, 1)

# create polynomial features (degree 2)
poly = PolynomialFeatures(degree=2)
gdp_poly = poly.fit_transform(gdp)

# train the model
model = LinearRegression()
model.fit(gdp_poly, unemployment_rate)

# predict unemployment rate for 2020 given GDP = 620 billion
gdp_2020 = np.array([[620]])
gdp_2020_poly = poly.transform(gdp_2020)
predicted_unemployment = model.predict(gdp_2020_poly)

# display prediction
print(
    f"Predicted unemployment rate for GDP of 620B is "
    f"{predicted_unemployment[0][0]:.2f}%"
)

# plot the results
plt.scatter(gdp, unemployment_rate, color="blue", label="Actual Data")

gdp_range = np.linspace(gdp.min(), gdp.max(), 100).reshape(-1, 1)
gdp_range_poly = poly.transform(gdp_range)
predicted_rates = model.predict(gdp_range_poly)

plt.plot(gdp_range, predicted_rates, color="red", label="Polynomial Regression Curve")

plt.xlabel("GDP (Billion USD)")
plt.ylabel("Unemployment Rate (%)")
plt.title("GDP vs Unemployment Rate (Polynomial Regression)")
plt.legend()
plt.grid(True)
plt.show()
