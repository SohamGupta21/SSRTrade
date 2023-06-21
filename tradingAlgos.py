from alpacaTrader import AlpacaTrader
from indicators import indicators
import os
import numpy as np

class TradingAlgos():
    def __init__(self, tick):
        self.ticker = tick
        self.last_price = 0
        self.current_price = 0
        self.alpacaTrader = AlpacaTrader("https://paper-api.alpaca.markets", "PK1VFVS6OA1V6DJ7BB6Z", "crQXqJpBrHdiSwDXxK9hLiv2eZTDi239JdRJ6Hrb")
        self.indicators = indicators()
        self.shares = 0

        self.rsiData = []
        self.macdData = []
        self.stochasticData = []
        self.macdHistory = []

        self.macdSignalLine = 0
        self.macd = 0
        self.rsi = 0
        self.stochasticK = 0

        self.tripleThreatCounter = 0






    def simpleMomentumTrader(self):
        self.last_price = self.current_price
        self.current_price = indicators.get_current_price(indicators, self.ticker)

        if not self.last_price == 0:
            if self.current_price > self.last_price:
                # buy code
                print("buy")
                self.alpacaTrader.buyStock(self.ticker , 1)

            elif self.current_price < self.last_price:
                # sell code
                print("sell")
                self.alpacaTrader.sellStock(self.ticker , 1)

    def simpleMomentumTraderWithStopLoss(self):
        self.last_price = self.current_price
        self.current_price = indicators.get_current_price(indicators, self.ticker)

        if not self.last_price == 0:
            if self.current_price > self.last_price:
                # buy code
                print("buy")
                self.alpacaTrader.buyStock(self.ticker , 1)
                self.shares +=1

            elif self.current_price < self.last_price and self.shares > 0:
                # sell code
                print("sell")
                self.alpacaTrader.sellStock(self.ticker , self.shares)
                self.shares = 0

    def rsiTrader(self):
        self.current_price = indicators.get_current_price(indicators, self.ticker)
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
                self.rsi = 0
            elif len(losses) == 0:
                self.rsi = 100
            else:
                RS = (sum(gains) / len(gains)) / (sum(losses) / len(losses))
                self.rsi = 100 - (100 / (1 + RS))
            print(f"RSI: {self.rsi}")
            # remove the first element from data
            self.rsiData.pop(0)
        else:
            pass



    def macdTrader(self):
        self.current_price = indicators.get_current_price(indicators, self.ticker)
        self.macdData.append(self.current_price)

        if len(self.macdData) == 26:
            twenty_six_ema = self.calculateEMA(self.macdData, 26, 25)
            twelve_ema = self.calculateEMA(self.macdData, 12, 11)

            self.macd = twelve_ema - twenty_six_ema

            self.macdHistory.append(self.macd)
            if len(self.macdHistory) > 8:
                self.macdSignalLine = self.calculateEMA(self.macdHistory[-9:], 9, 8)


            print(f"MACD value: {self.macd}")
            print(f"MACD signal: {self.macdSignalLine}")




            self.macdData.pop(0)
        else:
            pass

    def calculateEMA(self, data, period, index):

        smoothing = float(2 / (period + 1))

        if index == 0:
            return float(data[0])
        else:
            return (float(data[index]) * smoothing)+ (self.calculateEMA(data, period, index - 1) * (1-smoothing))
        
    def stoTrader(self):


        self.current_price = indicators.get_current_price(indicators, self.ticker)
        self.stochasticData.append(self.current_price)
            
        if(len(self.stochasticData) == 14):
            L14 = min(self.stochasticData)
            H14 = max(self.stochasticData)
            self.stochasticK = 100 * ((self.current_price - L14)/(H14 - L14))
            print(f"StochasticK: {self.stochasticK}")
            # remove the first element from data
            self.stochasticData.pop(0)
        else:
            pass   


    def tripleThreatTrader(self):
        self.tripleThreatCounter += 1
        self.macdTrader()
        self.rsiTrader()
        self.stoTrader()
        print(self.tripleThreatCounter)

        if(self.tripleThreatCounter > 35 and self.stochasticK < 20 and self.rsi > 50 and self.macd > self.macdSignalLine):
            print("BUY")
            self.alpacaTrader.buyStock(self.ticker, 1)


        if (self.tripleThreatCounter > 35 and self.stochasticK > 80 and self.rsi < 50 and self.macd < self.macdSignalLine):
            print("SELL")
            self.alpacaTrader.sellStock(self.ticker, 1)




 



            
            
            

        





