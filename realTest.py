# imports
import schedule as schedule
import yfinance as yf
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

import os
from dotenv.main import load_dotenv
from alpacaTrader import AlpacaTrader

load_dotenv()


# alpaca code to manage the library
class AlpacaTrader:
    def __init__(self, endpoint, apiKey, secretKey):
        self.endpoint = endpoint
        self.apiKey = apiKey
        self.secretKey = secretKey
        self.trading_client = TradingClient(apiKey, secretKey, paper=True)

    def buyStock(self, sym, quantity):
        # Setting parameters for our buy order
        market_order_data = MarketOrderRequest(
            symbol=sym,
            qty=quantity,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.GTC
        )

        market_order = self.trading_client.submit_order(market_order_data)
        for property_name, value in market_order:
            print(f"\"{property_name}\": {value}")

    def sellStock(self, sym, quantity):
        # Setting parameters for our buy order
        market_order_data = MarketOrderRequest(
            symbol=sym,
            qty=quantity,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.GTC
        )

        market_order = self.trading_client.submit_order(market_order_data)
        for property_name, value in market_order:
            print(f"\"{property_name}\": {value}")

    def getAccountInfo(self):
        account = self.trading_client.get_account()
        for property_name, value in account:
            print(f"\"{property_name}\": {value}")


def get_current_price(tick):
    ticker_yahoo = yf.Ticker(tick)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    # print(tick, last_quote)
    return last_quote


# function that has an indicator and tells you whether to buy or sell
last_price = 0
current_price = 0

alpacaTrader = AlpacaTrader(os.getenv("ENDPOINT"), os.getenv("APIKEY"), os.getenv("SECRETKEY"))


def indicator():
    # get the current price
    global last_price, current_price
    last_price = current_price
    current_price = get_current_price("AMZN")

    if not last_price == 0:
        if current_price > last_price:
            # buy code
            print("buy")
            alpacaTrader.buyStock('AMZN' , 1)

        elif current_price < last_price:
            # sell code
            print("sell")
            alpacaTrader.sellStock('AMZN' , 1)


# use the indicator

# use the alpaca code to buy or sell


# schedule to run this function every 5 seconds
schedule.every(0.5).seconds.do(indicator)


def buyTest():
    alpacaTrader.sellStock("AMZN", 320)
    print("Amazon purchased")


while True:
    # Run any pending jobs
    schedule.run_pending()
    # buyTest()
