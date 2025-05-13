import yfinance as yf

def downloadData(ticker):
    data_daily = yf.download(ticker, start="1957-03-04", end="2025-05-12")
    data_weekly = yf.download(ticker, start="1957-03-04", end="2025-05-12", interval="1wk")
    data_monthly = yf.download(ticker, start="1957-03-04", end="2025-05-12", interval="1mo")
    print(data_daily.head())
    print(data_weekly.head())
    print(data_monthly.head())

def main():
    ticker = '^GSPC'
    downloadData(ticker)

if __name__ == "__main__":
    main()