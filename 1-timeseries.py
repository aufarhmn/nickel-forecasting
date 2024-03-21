import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('Nickel-Price-Production.csv')

# Set 'Year' column as index
data.set_index('Year', inplace=True)

# Perform exponential smoothing
alpha = 0.2  # Smoothing parameter
data['Exponential_Smoothed'] = data['Price'].ewm(alpha=alpha, adjust=False).mean()

# Plot original data and exponential smoothed data
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Price'], label='Original Data', color='blue')
plt.plot(data.index, data['Exponential_Smoothed'], label='Exponential Smoothed', color='red')
plt.title('Nickel Prices and Exponential Smoothing Forecasting')
plt.xlabel('Year')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
