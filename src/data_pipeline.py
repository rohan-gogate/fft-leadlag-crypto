import os
import pandas as pd
import yfinance as yf

def load_asset_data(ticker, interval = '1h', period = "100d"):
    data = yf.download(ticker, interval=interval, period=period)
    return data.dropna()

def save_to_csv(data, ticker, directory='data/raw'):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist. Creating it.")
        os.makedirs(directory)
    file_path = os.path.join(directory, f"{ticker}.csv")
    data.to_csv(file_path)
    print(f"Data for {ticker} saved to {file_path}")
    return file_path

def load_from_csv(ticker, directory='data/raw'):
    filepath = os.path.join(directory, f"{ticker}.csv")
    return pd.read_csv(filepath, index_col=0, parse_dates=True)
