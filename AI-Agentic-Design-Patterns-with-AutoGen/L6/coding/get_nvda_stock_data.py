# filename: get_nvda_stock_data.py
import yfinance as yf
import pandas as pd

# 获取英伟达的股票数据
nvda = yf.Ticker("NVDA")

# 获取过去一个月的历史数据
hist = nvda.history(period="1mo")

# 打印数据
print(hist)