print("hello world")

import yfinance as yahooFinance

# Here We are getting Facebook financial information
# We need to pass FB as argument for that
GetAmazonInformation = yahooFinance.Ticker("AMZN")

# whole python dictionary is printed here
print(GetAmazonInformation.info)

# display Company Sector
print("Company Sector : ", GetAmazonInformation.info['sector'])

# display Price Earnings Ratio
print("Price Earnings Ratio : ", GetAmazonInformation.info['trailingPE'])

# display Company Beta
print("Company Beta : ", GetAmazonInformation.info['beta'])

amzn_historical = GetAmazonInformation.history(start="2023-05-23", end="2023-05-24", interval="1m")
print (amzn_historical)

