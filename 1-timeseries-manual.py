import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Nickel-Price-Production.csv')

data.set_index('Year', inplace=True)

alpha = 0.2
smoothed_prices = [data['Price'].iloc[0]]
for i in range(1, len(data)):
    smoothed_price = alpha * data['Price'].iloc[i] + (1 - alpha) * smoothed_prices[-1]
    smoothed_prices.append(smoothed_price)

data['Exponential_Smoothed_Manual'] = smoothed_prices

forecasted_price_2023 = alpha * data['Price'].iloc[-1] + (1 - alpha) * data['Exponential_Smoothed_Manual'].iloc[-1]

print("The forecasted nickel price for the year 2023 is: $", round(forecasted_price_2023, 2), sep="")

plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Price'], label='Original Data', color='blue')
plt.plot(data.index, data['Exponential_Smoothed_Manual'], label='Exponential Smoothed (Manual)', color='red')
plt.scatter(data.index[-1] + 1, forecasted_price_2023, color='green', label='Forecast for 2023')
plt.title('Nickel Prices and Exponential Smoothing Forecasting (Manual)')
plt.xlabel('Year')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
