import yfinance as yf
import streamlit as st

st.write("""
## Ziremi - Stock Price Tracker App

Here are stock closing **price** and **volume** of Microsoft  
""")

tickerSymbol = 'msft'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='max')
# tickerDf = tickerData.history(period='1d', start='2015-4-11', end='2020-4-11')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
