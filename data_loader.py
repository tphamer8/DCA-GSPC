import yfinance as yf

def downloadData(ticker):
    data_daily = yf.download(ticker, start="1993-01-22")
    data_weekly = yf.download(ticker, start="1993-01-22", interval="1wk")
    data_monthly = yf.download(ticker, start="1993-01-22", interval="1mo")
    print("")
    print("Daily:")
    print(data_daily.head())
    print("")
    print("Weekly:")
    print(data_weekly.head())
    print("")
    print("Monthly:")
    print(data_monthly.head())
    dividends = yf.Ticker(ticker).dividends
    print("")
    print(dividends)

def main():
    ticker = 'SPY'
    downloadData(ticker)

if __name__ == "__main__":
    main()