import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read data from CSV file
data = pd.read_csv('nickelproduction.csv')

# Set 'Year' column as index
data.set_index('Year', inplace=True)

# Perform linear regression to model the relationship between prices and production
X = data[['Production']]
y = data['Price']
model = LinearRegression()
model.fit(X, y)

# Forecast production for the upcoming year (assuming production data is available)
last_year = data.index[-1]
next_year = last_year + 1
forecasted_production = model.predict([[data.loc[last_year, 'Production']]])[0]

# Forecast nickel price for the upcoming year based on the forecasted production
forecasted_price = model.predict([[forecasted_production]])[0]

# Plot original data, regression line, and forecasted price
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Price'], label='Original Data', color='blue')
plt.scatter(next_year, forecasted_price, color='red', label='Forecast for ' + str(next_year))
plt.plot(data.index, model.predict(X), label='Regression Line', color='green')  # Plot regression line
plt.title('Nickel Prices and Causal Quantitative Forecasting')
plt.xlabel('Year')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
