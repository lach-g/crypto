from dataGrabClass import DataGrab
from assetClass import Asset
import numpy as np

class CurrentMarket:
    def __init__(self):
        self.asset_linked_list = None
        self.assets_hashed = None
        self.trade_linked_list = None
        self.trades_hashed = None
        self.empty = True

    def set_asset_data(self, linked_list, hash_table):
        self.asset_linked_list = linked_list
        self.assets_hashed = hash_table

    def set_trade_data(self, linked_list, hash_table):
        self.trade_linked_list = linked_list
        self.trades_hashed = hash_table

    def is_empty(self):
        if self.empty == True:
            return True
        else:
            return False

    def find_asset_details(self, key):
        return self.assets_hashed.retrieve(key)

    def find_trade_details(self, key):
        return self.trades_hashed.retrieve(key)

    def has_asset_data(self):
        if self.asset_linked_list != None and self.assets_hashed != None:
            return True
        else:
            return False

    def has_trades_data(self):
        if self.trade_linked_list != None and self.trades_hashed != None:
            return True
        else:
            return False

    def top_ten_price(self):
        self.__top_ten_price()

    def __top_ten_price(self):
        num_assets = self.asset_linked_list.count
        array = np.zeros(num_assets, dtype=object)
        
        for i in range(num_assets):
            asset = self.asset_linked_list.remove_first()
            array[i] = asset

        sorted_market_cap = self.market_cap_sort(array)
        count = len(sorted_market_cap) - 1
        limit = count - 10
        rank = 1
        print("TOP 10 Assets by Market Cap:")
        print("----------------------------")
        while count != limit:
            print(rank, ". ", array[count].symbol, " - ", array[count].market_cap)
            rank += 1
            count -= 1

    def market_cap_sort(self, A):
        # Index 0 is considered sorted
        cantConvert = 0
        for i in range(1, len(A)):
            # Grabs the second value to look at sorting
            valueToSort = A[i]
            '''Compares the left sorted side with the current value
            needing to be sorted'''
            try:
                left_side = float(A[i - 1].market_cap)
                right_side = float(valueToSort.market_cap)
                while left_side > right_side and i > 0:
                    A[i], A[i - 1] = A[i - 1], A[i]
                    # Stepping down the rest of the array
                    i = i - 1
            except:
                print("Cant convert to int", A[i - 1].market_cap, " ", valueToSort.market_cap)
                cantConvert += 1
        print("Cant convert: ", cantConvert)
            
        return A
        



