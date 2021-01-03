import config
import requests
import json

TRADE_CLASS_24hr_URL = "https://www.binance.com/api/v3/ticker/24hr"

# This needs an API key
ASSET_CLASS_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"


def get_data(url):
    raw_data = requests.get(url)
    if raw_data.status_code == 200:
        print_json(raw_data)
    else:
        print("Error with request")


def print_json(request_object):
    print(json.dumps(request_object.json(), indent=2))





