from alpacaTrader import AlpacaTrader
import yfinance as yf
import os



class indicators():
    def __init__(self):
        pass
        # function that has an indicator and tells you whether to buy or sell

    def get_current_price(self, tick):
        ticker_yahoo = yf.Ticker(tick)
        data = ticker_yahoo.history()
        last_quote = data['Close'].iloc[-1]
        # print(tick, last_quote)
        return last_quote