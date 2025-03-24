import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Define the stock symbol and date range
stock_symbol = 'AAPL'
start_date = '2025-02-01'
end_date = '2025-03-01'

# Step 2: Download the stock data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Step 3: Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(stock_data['Close'], label='Closing Price')
plt.title(f'{stock_symbol} Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Step 4: Calculate daily percentage change
stock_data['Daily Change %'] = stock_data['Close'].pct_change() * 100

# Step 5: Identify significant movements (e.g., changes greater than 2%)
significant_movements = stock_data[abs(stock_data['Daily Change %']) > 2]

# Step 6: Display significant movements
print(significant_movements)

# Step 7: Plot the closing prices with significant movements highlighted
plt.figure(figsize=(10, 5))
plt.plot(stock_data['Close'], label='Closing Price', linestyle='--', color='blue')
plt.scatter(significant_movements.index, significant_movements['Close'], color='red', label='Significant Movement')
plt.title(f'{stock_symbol} Closing Prices with Significant Movements', fontsize=14 , color='darkred')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Step 8: Save significant movements to a CSV file
significant_movements.to_csv('significant_movements.csv')
