import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Microsoft stock data
stock_symbol = "MSFT"
start_date = "2025-02-01"
end_date = "2025-02-28"

stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
stock_data.to_excel(f"{stock_symbol}_stock_data.xlsx")
print(f"{stock_symbol} data saved.")

plt.plot(stock_data['Close'], color='green', label='MSFT Closing Price')
plt.title('Microsoft Stock Price Movements')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()