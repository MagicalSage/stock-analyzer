import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

# Title and user input
st.title("Stock Trend Analyzer")
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", "AAPL")

# Fetch stock data
stock = yf.Ticker(ticker)
data = stock.history(period="1y") # 1 year of data

# Create a Plotly chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data["Close"], mode="lines", name="Close Price"))
fig.update_layout(title=f"{ticker} Stock Price", xaxis_title="Date", yaxis_title="Price (USD)")

# Display the chart
st.plotly_chart(fig)
# This app lets users enter a stock ticker (like “AAPL” for Apple) and see a year-long price chart.

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import yfinance as yf
# import plotly.graph_objs as go
# 
# st.title("Stock Trend Analyzer")
# ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", "AAPL")
# stock = yf.Ticker(ticker)
# data = stock.history(period="1y")
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=data.index, y=data["Close"], mode="lines", name="Close Price"))
# fig.update_layout(title=f"{ticker} Stock Price", xaxis_title="Date", yaxis_title="Price (USD)")
# st.plotly_chart(fig)
#
