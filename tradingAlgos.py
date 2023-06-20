from alpacaTrader import AlpacaTrader
from indicators import indicators
import os
import numpy as np

class TradingAlgos():
    def __init__(self):
        self.last_price = 0
        self.current_price = 0
        self.alpacaTrader = AlpacaTrader("https://paper-api.alpaca.markets", "PKI5BEQA5IIUNH6YV9K5", "sACQ8jXfOdEjJ90ZtC70XJjl25hmQs82vQSzZ3BN")
        self.indicators = indicators()
        self.shares = 0

        self.rsiData = []
        self.macdData = []
        self.stochasticData = []




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
        self.current_price = indicators.get_current_price(indicators, "AMZN")
        self.rsiData.append(self.current_price)
        
        if(len(self.rsiData) == 15):
            gains = []
            losses = []
            # calculate the differences
            for i in range(0, len(self.rsiData) - 1):
                diff = self.rsiData[i + 1] - self.rsiData[i]
                # add these differences to the gains and losses array  
                if diff > 0:
                    gains.append(diff)
                elif diff < 0:
                    losses.append(-(diff)) 
            # calculate the RSI

            if len(gains) == 0:
                RSI = 0
            elif len(losses) == 0:
                RSI = 100
            else:
                RS = (sum(gains) / len(gains)) / (sum(losses) / len(losses))
                RSI = 100 - (100 / (1 + RS))
            print(RSI)
            # remove the first element from data
            self.rsiData.pop(0)
        else:
            pass

        print(len(self.rsiData))


    def macdTrader(self):
        self.current_price = indicators.get_current_price(indicators, "AMZN")
        self.macdData.append(self.current_price)

        if len(self.macdData) == 26:
            twenty_six_ema = self.calculateEMA(self.macdData, 26, 25)
            twelve_ema = self.calculateEMA(self.macdData, 12, 11)

            MACD = twelve_ema - twenty_six_ema

            print(MACD)

        
            self.macdData.pop(0)
        else:
            pass
        print(len(self.macdData))

    def calculateEMA(self, data, period, index):

        smoothing = float(2 / (period + 1))

        if index == 0:
            return float(data[0])
        else:
            return (float(data[index]) * smoothing)+ (self.calculateEMA(data, period, index - 1) * (1-smoothing))
        
    def stochastic(self):


        self.current_price = indicators.get_current_price(indicators, "AMZN")
        self.stochasticData.append(self.current_price)
            
        if(len(self.stochasticData) == 14):
            L14 = min(self.stochasticData)
            H14 = max(self.stochasticData)
            K = 100 * ((self.current_price - L14)/(H14 - L14))
            print(K)
            # remove the first element from data
            self.stochasticData.pop(0)
        else:
            pass   
        print(len(self.stochasticData))

 



            
            
            

        





