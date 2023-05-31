from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import os
from dotenv.main import load_dotenv


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
        # for property_name, value in market_order:
        #     print(f"\"{property_name}\": {value}")

    def sellStock(self, sym, quantity):
        # Setting parameters for our buy order
        market_order_data = MarketOrderRequest(
            symbol=sym,
            qty=quantity,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.GTC
        )

        market_order = self.trading_client.submit_order(market_order_data)
        # for property_name, value in market_order:
        #     print(f"\"{property_name}\": {value}")

    def getAccountInfo(self):
        account = self.trading_client.get_account()
        # for property_name, value in account:
        #     print(f"\"{property_name}\": {value}")
