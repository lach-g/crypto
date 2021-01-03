'''
something to capture the loaded market values for the user to mess around with in the program
'''
from dataGrabClass import DataGrab


class CurrentMarket:
    def __init__(self, market_obj=None):
        self.market = market_obj

    def is_empty(self):
        if self.market == None:
            return True
        else:
            return False

    def add_market(self, market_obj):
        self.market = market_obj

    def find_asset_details(self, key):
        return self.market.assets.retrieve(key)
