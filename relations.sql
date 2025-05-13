DROP TABLE IF EXISTS stock_daily;
DROP TABLE IF EXISTS stock_weekly;
DROP TABLE IF EXISTS stock_monthly;
DROP TABLE IF EXISTS dividends;

CREATE TABLE stock_daily (
    id SERIAL PRIMARY KEY, -- Generates unique number
    ticker varchar,
    date DATE NOT NULL,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    volume FLOAT,
    UNIQUE(ticker, date)
);

CREATE TABLE stock_weekly (
    id SERIAL PRIMARY KEY, -- Generates unique number
    ticker varchar,
    week_start_date DATE NOT NULL,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    volume FLOAT,
    UNIQUE(ticker, week_start_date)
);

CREATE TABLE stock_monthly (
    id SERIAL PRIMARY KEY, -- Generates unique number
    ticker varchar,
    month_start_date DATE NOT NULL,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    volume FLOAT,
    UNIQUE(ticker, month_start_date)
);

CREATE TABLE dividends (
    ticker varchar,
    date DATE NOT NULL,
    dividend FLOAT,
    PRIMARY KEY (ticker, date)
);