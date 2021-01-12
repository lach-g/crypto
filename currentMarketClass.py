from dataGrabClass import DataGrab
from assetClass import Asset
import numpy as np

class CurrentMarket:
    def __init__(self):
        self.asset_linked_list = None
        self.assets_hashed = None
        self.trade_linked_list = None
        self.trades_hashed = None
        self.assets_array = None
        self.trades_array = None
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
        if self.trade_list_has_data() and self.trades_hashed != None:
            return True
        else:
            return False

    def trade_list_has_data(self):
        if self.trade_linked_list.count != 0:
            return True
        else:
            return False

    def hidden_assets_overview(self):
        self.assets_ll_to_array()
        self.top_ten_by_market_cap()
        self.top_ten_by_circulating()
        self.top_ten_by_24_percent()
        print("\n\n---SCROLL TO TOP TO VIEW ALL INFO---\n\n")

    def hidden_trades_overview(self):
        self.trades_ll_to_array()
        self.top_ten_price_change_percent()
        self.top_ten_volume_traded()
        self.top_ten_high_price()
        print("\n\n---SCROLL TO TOP TO VIEW ALL INFO---\n\n")

    # It will auto load in case a new csv file has been loaded
    def __linked_list_to_array_assets(self, linked_list):
        num_assets = linked_list.count
        array = np.zeros(num_assets, dtype=object)
        
        index = 0
        for asset in self.asset_linked_list:
            array[index] = asset
            index += 1

        return array

    def __linked_list_to_array_trades(self, linked_list):
        num_trades = linked_list.count
        array = np.zeros(num_trades, dtype=object)

        # DEBUG
        print("Linked list count:", linked_list.count)
        actual = 0
        for i in linked_list:
            actual += 1
        print("Actual count:", actual)
        
        index = 0
        for trade in self.trade_linked_list:
            trade.high_price = self.standardize_price(trade.quote_asset, float(trade.high_price))
            print(trade.symbol)
            array[index] = trade
            index += 1

        return array

    def standardize_price(self, crypto_symbol, crypto_price):
        asset = self.assets_hashed.retrieve(crypto_symbol)
        usd_price = asset.price * crypto_price
        return usd_price

    def assets_ll_to_array(self):
        self.assets_array = self.__linked_list_to_array_assets(self.asset_linked_list)

    def trades_ll_to_array(self):
        self.trades_array = self.__linked_list_to_array_trades(self.trade_linked_list)

    def top_ten_by_market_cap(self):
        self.market_cap_sort()
        count = len(self.assets_array) - 1
        limit = count - 10
        rank = 1
        print("TOP 10 ASSETS BY MARKET CAP:")
        print("----------------------------")
        while count != limit:
            print(rank, ".\t", self.assets_array[count].symbol, "\t", self.assets_array[count].market_cap)
            rank += 1
            count -= 1

    def market_cap_sort(self):
        A = self.assets_array
        cantConvert = 0
        for i in range(1, len(A)):
            valueToSort = A[i]
            left_side = float(A[i - 1].market_cap)
            right_side = float(valueToSort.market_cap)
            while left_side > right_side and i > 0:
                A[i], A[i - 1] = A[i - 1], A[i]
                i = i - 1

    def top_ten_by_circulating(self):
        self.circulation_sort()
        count = len(self.assets_array) - 1
        limit = count - 10
        rank = 1
        print("\nTOP 10 ASSETS BY CIRCULATION:")
        print("-----------------------------")
        while count != limit:
            print(rank, ".\t", self.assets_array[count].symbol, "\t", self.assets_array[count].circulating_supply)
            rank += 1
            count -= 1

    def circulation_sort(self):
        A = self.assets_array
        for i in range(1, len(A)):
            key = A[i]
            j = i-1
            while j >=0 and float(key.circulating_supply) < float(A[j].circulating_supply) :
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key

    def top_ten_by_24_percent(self):
        self.percent_sort()
        count = len(self.assets_array) - 1
        limit = count - 10
        rank = 1
        print("\nTOP 10 ASSETS BY 24H PERCENT:")
        print("-----------------------------")
        while count != limit:
            amount = self.assets_array[count].percent_24_hours
            if amount == "9000":
                amount = ">9000"
            print(rank, ".\t", self.assets_array[count].symbol, "\t", amount)
            rank += 1
            count -= 1

    def percent_sort(self):
        A = self.assets_array
        count = 0
        for i in range(1, len(A)):
            key = A[i]
            j = i-1
            try:
                right = float(key.percent_24_hours)
                left = float(A[j].percent_24_hours)
                while j >=0 and right < left:
                    A[j+1] = A[j]
                    j -= 1
                A[j+1] = key
            except:
                print("left: ", key.percent_24_hours, "right: ", A[j].percent_24_hours)
                count += 1

    def top_ten_price_change_percent(self):
        self.price_percent_sort()
        count = len(self.trades_array) - 1
        limit = count - 10
        rank = 1
        print("\nTOP 10 TRADES BY PRICE CHANGE PERCENT:")
        print("---------------------------------------")
        while count != limit:
            print(rank, ".\t", self.trades_array[count].symbol, "\t", self.trades_array[count].price_change_percent)
            rank += 1
            count -= 1

    def price_percent_sort(self):
        A = self.trades_array
        for i in range(1, len(A)):
            key = A[i]
            j = i-1
            while j >=0 and float(key.price_change_percent) < float(A[j].price_change_percent) :
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key

    def top_ten_volume_traded(self):
        self.volume_sort()
        count = len(self.trades_array) - 1
        limit = count - 10
        rank = 1
        print("\nTOP 10 TRADES BY VOLUME:")
        print("---------------------------------------")
        while count != limit:
            print(rank, ".\t", self.trades_array[count].symbol, "\t", round(float(self.trades_array[count].volume), 1))
            rank += 1
            count -= 1

    def volume_sort(self):
        A = self.trades_array
        for i in range(1, len(A)):
            key = A[i]
            j = i-1
            while j >=0 and float(key.volume) < float(A[j].volume) :
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key

    def top_ten_high_price(self):
        self.weighted_avg_sort()
        count = len(self.trades_array) - 1
        limit = count - 10
        rank = 1
        print("\nTOP 10 TRADES BY HIGH PRICE:")
        print("------------------------------------------")
        while count != limit:
            print(rank, ".\t", self.trades_array[count].symbol, "\t", round(float(self.trades_array[count].high_price), 2))
            rank += 1
            count -= 1

    def weighted_avg_sort(self):
        A = self.trades_array
        for i in range(1, len(A)):
            key = A[i]
            j = i-1
            while j >=0 and float(key.high_price) < float(A[j].high_price):
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key

    def remove_from_asset_ll(self, to_remove):
        linked_list = self.asset_linked_list
        current_node = linked_list.head
        while current_node != None:
            if linked_list.count == 1:
                linked_list.head = None
                linked_list.tail = None
                linked_list.count -= 1
            if current_node.data.symbol == to_remove:
                next_node = current_node.next
                head_check = current_node.prev
                if head_check == None:
                    new_first_node = current_node.next
                    linked_list.head = new_first_node
                    new_first_node.prev = None
                elif next_node == None:
                    prev_node = current_node.prev
                    prev_node.next = None
                    linked_list.tail = prev_node
                else:
                    first_node = current_node.prev
                    third_node = current_node.next
                    first_node.next = third_node
                    third_node.prev = first_node
                linked_list.count -= 1
                print("Successfully filtered out", current_node.data.symbol)
                break
            else:
                current_node = current_node.next

    def remove_from_trades_ll(self, to_remove):
        linked_list = self.trade_linked_list
        current_node = linked_list.head
        while current_node != None:
            if linked_list.count == 1:
                linked_list.head = None
                linked_list.tail = None
                linked_list.count -= 1
            if linked_list.count < 1:
                    print("LIST HAS BEEN EMPTIED")
                    break

            if current_node.data.base_asset == to_remove or current_node.data.quote_asset == to_remove:
                next_node = current_node.next
                head_check = current_node.prev
                if head_check == None:
                    new_first_node = current_node.next
                    linked_list.head = new_first_node
                    new_first_node.prev = None
                elif next_node == None:
                    prev_node = current_node.prev
                    prev_node.next = None
                    linked_list.tail = prev_node
                else:
                    first_node = current_node.prev
                    third_node = current_node.next
                    first_node.next = third_node
                    third_node.prev = first_node
                linked_list.count -= 1
                current_node = current_node.next
            else:
                current_node = current_node.next

     


            
        



