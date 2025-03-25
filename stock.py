import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

st.title("Stock Trend Analyzer")
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", "AAPL")

# Password for premium feature
password = st.text_input("Enter Password for Premium Features (leave blank for free version)", type="password")
show_premium = password == "premium123"  # Set your password here

# Fetch stock data
stock = yf.Ticker(ticker)
data = stock.history(period="1y")

# Create the price chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data["Close"], mode="lines", name="Close Price"))

# Add premium feature: 50-day moving average
if show_premium:
    fig.add_trace(go.Scatter(x=data.index, y=data["Close"].rolling(50).mean(), mode="lines", name="50-Day MA", line=dict(color="orange")))

fig.update_layout(title=f"{ticker} Stock Price", xaxis_title="Date", yaxis_title="Price (USD)")
st.plotly_chart(fig)

# Show a message if premium features are not unlocked
if not show_premium:
    st.write("Enter the password to unlock premium features like the 50-day moving average! Get access at [savadoctor.gumroad.com/l/stockpremium](https://savadoctor.gumroad.com/l/stockpremium).")
