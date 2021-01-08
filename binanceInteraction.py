import config
import requests
import json
from tradeClass import Trade
from LinkedList_dsa import ListNode, LinkedList

TRADE_CLASS_24hr_URL = "https://www.binance.com/api/v3/ticker/24hr"

# This needs an API key
ASSET_CLASS_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"


def get_data(url):
    raw_data = requests.get(url)
    if raw_data.status_code == 200:
        json_data = raw_data.json()
        return json_data
    else:
        print("Error with request")

def recent_trades_to_list(trades):
    ll = LinkedList()
    for trade in trades:
        ll.insert_last(Trade(trade["symbol"]))
    return ll



def print_json(request_object):
    print(json.dumps(request_object.json(), indent=2))

get_data(TRADE_CLASS_24hr_URL)




