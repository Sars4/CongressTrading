import pandas as pd
import yfinance as yf
from datetime import timedelta

# Load the CSV file
df = pd.read_excel('C:\\Users\\logan\\Downloads\\U.S Senators Trades - Master.xlsx')

# Create new columns for the closing price, price after 1 week, 1 month, 3 months, and 1 year, and the percentage change
df['Industry'] = None  # New column for the industry of the stock


for index, row in df.iterrows():
    print(index)
    stock = yf.Ticker(row['ticker'])
    start_date = pd.to_datetime(row['transaction_date'])
    end_date = start_date + timedelta(days=365)
    hist = stock.history(start=start_date, end=start_date + timedelta(days=365))

    if 'industry' in stock.info:
        df.loc[index, 'Industry'] = stock.info['industry']

df.to_excel('C:\\Users\\logan\\Downloads\\U.S Senators Trades - Master.xlsx', index=False)
