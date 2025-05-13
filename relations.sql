CREATE TABLE stock_daily (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Generates unique number
    ticker varchar,
    date DATE NOT NULL,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    volume FLOAT
    UNIQUE(ticker, date)
)

CREATE TABLE stock_weekly (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Generates unique number
    ticker varchar,
    week_start_date DATE NOT NULL,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    volume FLOAT
    UNIQUE(ticker, week_start_date)
)

CREATE TABLE stock_monthly (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Generates unique number
    ticker varchar,
    month_start_date DATE NOT NULL,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    volume FLOAT
    UNIQUE(ticker, week_start_date)
)

CREATE TABLE dividends (
    ticker varchar,
    date DATE,
    dividend FLOAT,
    PRIMARY(ticker, date)
    FOREIGN KEY (ticker) REFERENCES stock_daily(ticker) 
)


