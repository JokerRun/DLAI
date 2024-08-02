# filename: stock_prices_YTD.py
from functions import get_stock_prices, plot_stock_prices

# Define the stock symbols, start date, and end date
stock_symbols = ['NVDA', 'TSLA']
start_date = '2024-01-01'
end_date = '2024-08-02'

# Get the stock prices
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Plot the stock prices and save the figure to a file
plot_stock_prices(stock_prices, 'stock_prices_YTD_plot.png')