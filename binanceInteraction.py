import config
# from binance.client import Client
import requests

'''
client = Client(config.API_KEY, config.API_SECRET)

tickers = client.get_ticker()

orderbook = client.get_orderbook_tickers()
print(orderbook)
'''

exchange_info = requests.get("https://www.binance.com/api/v3/exchangeInfo")
trades = requests.get("https://www.binance.com/api/v3/trades")
print(trades.json())