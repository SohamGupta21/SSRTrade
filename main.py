import yfinance as yahooFinance

import os
from dotenv.main import load_dotenv
load_dotenv()

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

endpoint = os.getenv("ENDPOINT")
apiKey = os.getenv("APIKEY")
secretKey = os.getenv("SECRETKEY")

trading_client = TradingClient(apiKey, secretKey, paper=True)

# Setting parameters for our buy order
market_order_data = MarketOrderRequest(
                      symbol="AMZN",
                      qty=1,
                      side=OrderSide.SELL,
                      time_in_force=TimeInForce.GTC
                  )

market_order = trading_client.submit_order(market_order_data)
for property_name, value in market_order:
  print(f"\"{property_name}\": {value}")



account = trading_client.get_account()
for property_name, value in account:
  print(f"\"{property_name}\": {value}")


print(f"The endpoint is {endpoint}, the api key is {apiKey}, the secret key is {secretKey}")

# Here We are getting Amazon financial information
# We need to pass AMZN as argument for that
GetAmazonInformation = yahooFinance.Ticker("AMZN")

# whole python dictionary is printed here
print(GetAmazonInformation.info)

# display Company Sector
print("Company Sector : ", GetAmazonInformation.info['sector'])

# display Price Earnings Ratio
print("Price Earnings Ratio : ", GetAmazonInformation.info['trailingPE'])

# display Company Beta
print("Company Beta : ", GetAmazonInformation.info['beta'])

amzn_historical = GetAmazonInformation.history(start="2023-05-24", end="2023-05-25", interval="1m")
print(amzn_historical)

