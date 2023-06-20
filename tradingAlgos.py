from alpacaTrader import AlpacaTrader
from indicators import indicators
import os

class TradingAlgos():
    def __init__(self):
        self.last_price = 0
        self.current_price = 0
        self.alpacaTrader = AlpacaTrader("https://paper-api.alpaca.markets", "PKI5BEQA5IIUNH6YV9K5", "sACQ8jXfOdEjJ90ZtC70XJjl25hmQs82vQSzZ3BN")
        self.indicators = indicators()
        self.shares = 0




    def simpleMomentumTrader(self):
        self.last_price = self.current_price
        self.current_price = indicators.get_current_price(indicators, "AMZN")

        if not self.last_price == 0:
            if self.current_price > self.last_price:
                # buy code
                print("buy")
                self.alpacaTrader.buyStock('AMZN' , 1)

            elif self.current_price < self.last_price:
                # sell code
                print("sell")
                self.alpacaTrader.sellStock('AMZN' , 1)

    def simpleMomentumTraderWithStopLoss(self):
        self.last_price = self.current_price
        self.current_price = indicators.get_current_price(indicators, "AMZN")

        if not self.last_price == 0:
            if self.current_price > self.last_price:
                # buy code
                print("buy")
                self.alpacaTrader.buyStock('AMZN' , 1)
                self.shares +=1

            elif self.current_price < self.last_price and self.shares > 0:
                # sell code
                print("sell")
                self.alpacaTrader.sellStock('AMZN' , self.shares)
                self.shares = 0

    def rsiTrader(self):
        gains = []
        losses = []



