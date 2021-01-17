import requests
import json
from tradeClass import Trade
from LinkedList_dsa import ListNode, LinkedList

TRADE_CLASS_24hr_URL = "https://www.binance.com/api/v3/ticker/24hr"

EXCHANGE_INFO_URL = "https://api.binance.com/api/v3/exchangeInfo"

TICKER_URL = "https://api.binance.com/api/v3/ticker/24hr"

# This needs an API key
ASSET_CLASS_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"


def get_data(url):
    raw_data = requests.get(url)
    if raw_data.status_code == 200:
        print_json(raw_data)
        #json_data = raw_data.json()
        #return json_data
    else:
        print("Error with request")

def recent_trades_to_list(trades):
    ll = LinkedList()
    for trade in trades:
        ll.insert_last(Trade(trade["symbol"]))
    return ll



def print_json(request_object):
    print(json.dumps(request_object.json(), indent=2))

print(get_data(TICKER_URL))

'''
1. iterate through a list of the trade symbols, requesting the latest trade weighted average price
2. Fill the current market with this data
3. Sort through in finding the best trade paths currently
'''

