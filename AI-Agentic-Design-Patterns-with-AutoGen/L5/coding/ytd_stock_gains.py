# filename: ytd_stock_gains.py
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Define the tickers and the date range
tickers = ["NVDA", "TSLA"]
start_date = "2024-01-01"
end_date = "2024-08-02"

# Fetch the data
data = yf.download(tickers, start=start_date, end=end_date)

# Calculate YTD gains
ytd_gains = {}
for ticker in tickers:
    start_price = data['Adj Close'][ticker].iloc[0]
    end_price = data['Adj Close'][ticker].iloc[-1]
    gain = ((end_price - start_price) / start_price) * 100
    ytd_gains[ticker] = gain

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(ytd_gains.keys(), ytd_gains.values(), color=['blue', 'red'])
plt.title('Year-to-Date (YTD) Stock Gains (%)')
plt.ylabel('Percentage Gain (%)')
plt.xlabel('Stock')
plt.grid(True)

# Save the figure
plt.savefig('ytd_stock_gains.png')
plt.show()