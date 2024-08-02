# filename: get_stock_data.py
import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = 'YOUR_API_KEY'
symbol = 'NVDA'
function = 'TIME_SERIES_DAILY'
outputsize = 'compact'

url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={outputsize}&apikey={api_key}'
response = requests.get(url)
data = response.json()

# 提取过去一个月的数据
time_series = data['Time Series (Daily)']

# 将数据转换为DataFrame
df = pd.DataFrame(time_series).T
df.index = pd.to_datetime(df.index)
df = df.astype(float)
df = df.sort_index()

# 获取过去一个月的数据
start_date = '2024-07-02'
end_date = '2024-08-02'
last_month_data = df.loc[start_date:end_date]

# 计算基本统计数据
summary = last_month_data.describe()

# 绘制收盘价走势图
plt.figure(figsize=(14, 7))
plt.plot(last_month_data['4. close'], label='Close Price')
plt.title('NVIDIA Stock Price - Last Month')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.savefig('nvidia_stock_price.png')

# 打印摘要统计数据
print(summary)