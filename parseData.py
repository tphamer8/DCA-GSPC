from dotenv import load_dotenv
import os
import psycopg2
import yfinance as yf

# load environment variables from .env
load_dotenv

# Database connection variables from .env
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Connect to PostgresSQL
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

# Create a cursor object which allows us to execute SQL commands
cursor = conn.cursor()

# Get SPY stock data
ticker = 'SPY'
data_daily = yf.download(ticker, start="1993-01-22")
data_weekly = yf.download(ticker, start="1993-01-22", interval="1wk")
data_monthly = yf.download(ticker, start="1993-01-22", interval="1mo")

# Insert statements for stock_daily table
for index, row in data_daily.iterrows():
    cursor.execute("""
    INSERT INTO stock_daily (ticker, date, open, close, high, low, volume)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (ticker, date) DO NOTHING;
    """, (
        ticker,
        index.date(),
        row['Open'],
        row['Close'],
        row['High'],
        row['Low'],
        row['Volume']
    ))

# Insert statements for dividends table
dividends_data = yf.Ticker(ticker).dividends
for date, dividend in dividends_data.item():
    cursor.execute("""
    INSERT INTO dividends (ticker, date, dividend)
    VALUES (%s, %s, %s)
    ON CONFLICT (ticker, date) DO NOTZHING;
    """, (
        ticker,
        date.date(),
        dividend
    ))

# Commit and Close
conn.commit()
cursor.close()
conn.close()

print("Data insertion complete.")