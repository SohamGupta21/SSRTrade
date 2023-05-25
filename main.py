print("hello world")

import yfinance as yahooFinance

import os
from dotenv import load_dotenv
load_dotenv()

endpoint = os.getenv("ENDPOINT")
apiKey = os.getenv("APIKEY")
secretKey = os.getenv("SECRETKEY")

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

