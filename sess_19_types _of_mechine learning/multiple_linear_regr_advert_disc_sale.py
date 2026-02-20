# Import required modules
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create the dataset
data = {
    'Year': [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,
             2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020],
    'Advertising Budget ($)': [
        150,200,180,220,170,250,210,230,190,280,
        240,180,370,190,380,190,390,190,400,190,250
    ],
    'Discount ($)': [
        5,10,7,12,17,11,12,14,6,12,
        3,4,12,11,3,9,8,7,9,3,12
    ],
    'Sales ($)': [
        1050,1200,1400,1550,1800,1700,1600,1850,1450,1300,
        1200,1700,1600,1500,1400,1800,1700,1600,1850,1450,1300
    ]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Split independent (X) and dependent (y) variables
X = df[['Advertising Budget ($)', 'Discount ($)']]  # independent variables
y = df['Sales ($)']  # dependent variable

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict sales for 2024 with given budget and discount
budget_2024 = 250
discount_2024 = 12
sales_2024 = model.predict([[budget_2024, discount_2024]])

# Display the prediction
print(f"Predicted sales for 2024 with an advertising budget of ${budget_2024} "
      f"and discount of ${discount_2024} is: {sales_2024[0]:.2f}")

# Visualize the data
plt.figure(figsize=(10, 6))

# Plot actual sales
plt.scatter(df['Year'], df['Sales ($)'], color='blue', label='Actual Sales', marker='o')

# Plot predicted sales for historical data
y_pred = model.predict(X)
plt.plot(df['Year'], y_pred, color='green', label='Predicted Sales')

# Highlight 2024 prediction
plt.scatter(2024, sales_2024, color='red', label='2024 Prediction', marker='x', s=100)

plt.xlabel('Year')
plt.ylabel('Sales ($)')
plt.title('Sales Prediction using Multiple Linear Regression')
plt.legend()
plt.show()
