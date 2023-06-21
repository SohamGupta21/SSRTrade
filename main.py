import schedule
from tradingAlgos import TradingAlgos


tradingAlgos = TradingAlgos("AMZN")

if __name__ == '__main__':
    # This code won't run if this file is imported.
    # schedule to run this function every 5 seconds

    schedule.every(1.5).seconds.do(tradingAlgos.tripleThreatTrader)



    while True:
        # Run any pending jobs
        schedule.run_pending()

