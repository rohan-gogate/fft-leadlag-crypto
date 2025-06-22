import os
import pandas as pd
import yfinance as yf

def load_asset_data(ticker, interval = '1h', period = "100d"):
    data = yf.download(ticker, interval=interval, period=period)
    return data.dropna()

def save_to_csv(data: pd.DataFrame, ticker: str, directory: str = "data/raw") -> str:
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, f"{ticker}.csv")
    data.to_csv(filepath)  # Don't set index=False
    return filepath

def load_from_csv(ticker: str, directory: str = "data/raw") -> pd.DataFrame:
    filepath = os.path.join(directory, f"{ticker}.csv")
    return pd.read_csv(filepath, index_col=0, parse_dates=True)
