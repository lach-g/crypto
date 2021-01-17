from dataGrabClass import DataGrab
from assetClass import Asset
from Graph_dsa import Graph, Edge
from DoubleLinkedList_dsa import DoubleLinkedList, ListNode
import numpy as np


class CurrentMarket:
    def __init__(self):
        self.asset_linked_list = None
        self.assets_hashed = None
        self.trade_linked_list = None
        self.trades_hashed = None
        self.assets_array = None
        self.trades_array = None
        self.trades_graph = None
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

    def collected_assets_overview(self):
        self.assets_ll_to_array()
        self.top_ten_by_market_cap()
        self.top_ten_by_circulating()
        self.top_ten_by_24_percent()
        print("\n\n---SCROLL TO TOP TO VIEW ALL INFO---\n\n")

    def collected_trades_overview(self):
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
        
        index = 0
        for trade in self.trade_linked_list:
            trade.high_price = self.standardize_price(trade.quote_asset, float(trade.high_price))
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
        sorting = self.assets_array
        cantConvert = 0
        for i in range(1, len(sorting)):
            valueToSort = sorting[i]
            left_side = float(sorting[i - 1].market_cap)
            right_side = float(valueToSort.market_cap)
            while left_side > right_side and i > 0:
                sorting[i], sorting[i - 1] = sorting[i - 1], sorting[i]
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
        sorting = self.assets_array
        for i in range(1, len(sorting)):
            key = sorting[i]
            j = i-1
            while j >=0 and float(key.circulating_supply) < float(sorting[j].circulating_supply):
                sorting[j+1] = sorting[j]
                j -= 1
            sorting[j+1] = key

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
        sorting = self.assets_array
        count = 0
        for i in range(1, len(sorting)):
            key = sorting[i]
            j = i-1
            try:
                right = float(key.percent_24_hours)
                left = float(sorting[j].percent_24_hours)
                while j >=0 and right < left:
                    sorting[j+1] = sorting[j]
                    j -= 1
                sorting[j+1] = key
            except:
                print("left: ", key.percent_24_hours, "right: ", sorting[j].percent_24_hours)
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
        sorting = self.trades_array
        for i in range(1, len(sorting)):
            key = sorting[i]
            j = i-1
            while j >=0 and float(key.price_change_percent) < float(sorting[j].price_change_percent) :
                sorting[j+1] = sorting[j]
                j -= 1
            sorting[j+1] = key

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
        sorting = self.trades_array
        for i in range(1, len(sorting)):
            key = sorting[i]
            j = i-1
            while j >=0 and float(key.volume) < float(sorting[j].volume) :
                sorting[j+1] = sorting[j]
                j -= 1
            sorting[j+1] = key

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
        sorting = self.trades_array
        for i in range(1, len(sorting)):
            key = sorting[i]
            j = i-1
            while j >=0 and float(key.high_price) < float(sorting[j].high_price):
                sorting[j+1] = sorting[j]
                j -= 1
            sorting[j+1] = key

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

    def remove_from_asset_hash(self, to_remove):
        self.assets_hashed.remove(to_remove)

    def remove_from_trade_hash(self, to_remove):
        data_grab = DataGrab()
        data_grab.set_trades_linked_list(self.trade_linked_list)
        self.trades_hashed = data_grab.read_trades_to_hash()

    def graphing(self):
        trades = self.trade_linked_list
        assets = self.assets_hashed
        trades_graph = Graph()
        for trade in trades:
            asset_selling = assets.retrieve(trade.base_asset)
            asset_buying = assets.retrieve(trade.quote_asset)
            if asset_selling != None and asset_buying != None:
                if trades_graph.has_vertex(asset_selling.symbol) == False:
                    trades_graph.add_vertex(asset_selling.symbol, asset_selling)
                if trades_graph.has_vertex(asset_buying.symbol) == False:
                    trades_graph.add_vertex(asset_buying.symbol, asset_buying)
                trades_graph.add_edge(asset_selling.symbol, asset_buying.symbol, trade.price_change_percent)

        self.trades_graph = trades_graph

    def find_direct_paths(self, base, quote):
        print("\nBreadth first search for the shortest trade path:")
        breadth_path = self.trades_graph.bfs_shortest_path(base, quote)
        if breadth_path != None:
            for vertex_name in breadth_path:
                print(vertex_name)
        print()

        print("\nDepth first search for the trade path optimizing for weighted average price:")
        depth_path = self.trades_graph.dfs_shortest_path(base, quote)
        if depth_path != None:
            for vertex_name in depth_path:
                print(vertex_name)



            
        



