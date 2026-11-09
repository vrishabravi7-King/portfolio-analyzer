import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

st.title("Portfolio Analyzer")

tickers_in = st.text_input("Tickers (comma separated)", "AAPL, MSFT, JPM")
weights_in = st.text_input("Weights (must sum to 1)", "0.4, 0.3, 0.3")
start = st.date_input("Start date", pd.to_datetime("2021-01-01"))

if st.button("Analyze"):
    tickers = [t.strip().upper() for t in tickers_in.split(",")]
    weights = np.array([float(w) for w in weights_in.split(",")])

    if len(tickers) != len(weights) or not np.isclose(weights.sum(), 1):
        st.error("Need one weight per ticker, and they must sum to 1.")
        st.stop()

    prices = yf.download(tickers + ["SPY"], start=start)["Close"].dropna()
    returns = prices.pct_change().dropna()

    port = (returns[tickers] * weights).sum(axis=1)
    spy = returns["SPY"]

    def metrics(r):
        cum = (1 + r).cumprod()
        vol = r.std() * np.sqrt(252)
        return {
            "Total return": f"{cum.iloc[-1] - 1:.1%}",
            "Annual volatility": f"{vol:.1%}",
            "Sharpe (rf=0)": f"{(r.mean() * 252) / vol:.2f}",
            "Max drawdown": f"{(cum / cum.cummax() - 1).min():.1%}",
        }

    st.subheader("Metrics")
    st.table(pd.DataFrame({"Portfolio": metrics(port), "S&P 500": metrics(spy)}))

    st.subheader("Growth of $1")
    st.line_chart(pd.DataFrame({"Portfolio": (1 + port).cumprod(),
                                "S&P 500": (1 + spy).cumprod()}))