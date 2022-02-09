import requests
import json

class cmc_Data:
    '''Class to return current cmc index data'''
    
    def __init__(self, symbol, price, HR,):
        self.symbol = symbol
        self.price = price
        self.HR = HR
       
        
    def get_data():
        url = 'https://api.blockchain.com/v3/exchange/tickers/'
        r = requests.get(url)
        data = r.json()
        symbols = data

        for symbol in symbols:
            print(f"name: {symbol['symbol']}")
            print(f"price: {symbol['last_trade_price']}")
            print(f"24HR: {symbol['volume_24h']}")
            print("\n")
        
print(f"{cmc_Data.get_data()}")
