from alpacaTrader import AlpacaTrader
from indicators import indicators

class TradingAlgos():
    def __init__(self):
        self.last_price = 0
        self.current_price = 0
        self.alpacaTrader = AlpacaTrader("https://paper-api.alpaca.markets", "PKCZKBUQHLTN83I82B4U", "0VuY0Fe9dUHffs1kKPUZMDsEJqouKCoocgztgglZ")
        self.indicators = indicators()

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

    def rsiTrader(self):
        gains = []
        losses = []



