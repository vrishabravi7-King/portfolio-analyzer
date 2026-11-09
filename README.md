# Portfolio Analyzer

A web app that analyzes a custom stock portfolio and benchmarks it against the S&P 500.

**Live app:** vrishabs-portfolio.streamlit.app

## What it does
Enter tickers, weights, and a start date. The app pulls historical prices and shows:

| Metric | What it means |
|---|---|
| Total return | How much $1 grew over the period |
| Annual volatility | How much returns swing in a year (daily standard deviation x √252) |
| Sharpe ratio | Annualized return per unit of risk (risk-free rate assumed 0%) |
| Max drawdown | Worst peak-to-trough drop in portfolio value |

It also plots the growth of $1 for your portfolio vs. SPY (S&P 500 ETF).

## Tech
Python, pandas, NumPy, yfinance, Streamlit

## Assumptions and limitations
- Weights are fixed and rebalanced daily
- Risk-free rate is 0% in the Sharpe calculation
- Uses adjusted closing prices from Yahoo Finance (no taxes, fees, or slippage)
- Past performance does not predict future results

## Run locally
```
pip install streamlit yfinance pandas numpy
streamlit run app.py
```

## Possible next steps
- Risk-free rate input
- Rebalancing options (monthly/quarterly)
- Additional metrics (Sortino ratio, beta)
