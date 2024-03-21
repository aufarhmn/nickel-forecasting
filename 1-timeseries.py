import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Nickel-Price-Production.csv')

data.set_index('Year', inplace=True)

alpha = 0.2
data['Exponential_Smoothed'] = data['Price'].ewm(alpha=alpha, adjust=False).mean()

last_year = data.index[-1]
forecasted_price_2023 = data['Exponential_Smoothed'].iloc[-1]  

print("The forecasted nickel price for the year 2023 is: $", round(forecasted_price_2023, 2), sep="")

plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Price'], label='Original Data', color='blue')
plt.plot(data.index, data['Exponential_Smoothed'], label='Exponential Smoothed', color='red')
plt.scatter(last_year + 1, forecasted_price_2023, color='green', label='Forecast for 2023')
plt.title('Nickel Prices and Exponential Smoothing Forecasting')
plt.xlabel('Year')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
