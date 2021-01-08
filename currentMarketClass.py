from dataGrabClass import DataGrab
from assetClass import Asset

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

        def insertion_sort(arr):
            for i in range(1, arr.count):
                key = arr[i]
                # Move elements of arr[0..i-1], that are greaterthan key,
                # to one position ahead of their current position
                j = i-1
                while j >=0 and key.price < arr[j].price :
                    arr[j+1] = arr[j]
                    j -= 1
                arr[j+1] = key
            return arr

        sorted_list = insertion_sort(self.asset_linked_list)
        for i in sorted_list:
            print(i.price)