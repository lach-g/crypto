import sys
sys.path.append("../assignment")

import unittest
import numpy as np
from currentMarketClass import CurrentMarket
from DoubleLinkedList_dsa import DoubleLinkedList, ListNode
from HashTable_dsa import HashTable, HashEntry
from Graph_dsa import Graph, Vertex, Edge
from tradeClass import Trade
from assetClass import Asset


class TestCurrentMarketClass(unittest.TestCase):

    def test_init(self):
        graph = Graph()
        array = np.zeros(10)

        market = CurrentMarket()
        self.assertTrue(market.asset_linked_list == None,
            "When first initialised the assets linked list should equal None.")

    def test_set_asset_data(self):
        link_list = DoubleLinkedList()
        hash_table = HashTable(10)
        market = CurrentMarket()
        market.set_asset_data(link_list, hash_table)
        self.assertTrue(market.asset_linked_list != None,
            "The linked list should be set")

    def test_set_trade_data(self):
        link_list = DoubleLinkedList()
        hash_table = HashTable(10)
        market = CurrentMarket()
        market.set_trade_data(link_list, hash_table)
        self.assertTrue(market.trade_linked_list != None,
            "The linked list should be set")

    def test_is_empty(self):
        market = CurrentMarket()
        self.assertEqual(market.is_empty(), True,
            "On initialisation the current market should be empty")

    def test_find_asset_details(self):
        ll = DoubleLinkedList()
        hash_table = HashTable(10)
        hash_table.insert("A", 1)
        market = CurrentMarket()
        market.set_asset_data(ll, hash_table)
        self.assertEqual(market.find_asset_details("A"), 1,
                "Function should perform a hash retrieve.")

    def test_find_trade_details(self):
        ll = DoubleLinkedList()
        hash_table = HashTable(10)
        hash_table.insert("A", 1)
        market = CurrentMarket()
        market.set_trade_data(ll, hash_table)
        self.assertEqual(market.find_trade_details("A"), 1,
                "Function should perform a hash retrieve.")

    def test_has_asset_data(self):
        market = CurrentMarket()
        self.assertEqual(market.has_asset_data(), False,
                    "No market data has been added.")

    def test_has_trades_data(self):
        market = CurrentMarket()
        self.assertEqual(market.has_trades_data(), False,
                    "No market data has been added.")

    def test_trade_list_has_data(self):
        market = CurrentMarket()
        self.assertEqual(market.trade_list_has_data(), False,
                "No trade linked list has been added.")

    def test_linked_list_to_array_assets(self):
        trade = Trade("BTCETH", "BTC", "ETH", 2, 5, 1, 3,
                4, 3, 5, 3, 5, 2, 2, 4, 5, 3, 2, 2, 2,1 ,3, 2)
        asset = Asset(1, "Bitcoin", "BTC", 23421, 12431, 1434,
                        363, 35636, 23452, 25)
        ll_assets = DoubleLinkedList()
        ll_trades = DoubleLinkedList()
        ll_trades.insert_first(trade)
        ll_assets.insert_first(asset)


        hash_table_trades = HashTable(10)
        hash_table_assets = HashTable(10)
        hash_table_assets.insert(asset.symbol, asset)
        hash_table_trades.insert(trade.symbol, trade)

        market = CurrentMarket()
        market.set_trade_data(ll_trades, hash_table_trades)
        market.set_asset_data(ll_assets, hash_table_assets)

        array = market.linked_list_to_array_assets(ll_assets)
        self.assertEqual(array[0], asset,
                        "Array should return only asset at index 0")

    def test_standardize_price(self):
        asset = Asset(1, "Bitcoin", "BTC", 23421, 12431, 1434,
                        363, 35636, 23452, 25)
        ll_assets = DoubleLinkedList()
        ll_assets.insert_first(asset)


        hash_table_assets = HashTable(10)
        hash_table_assets.insert(asset.symbol, asset)

        market = CurrentMarket()
        market.set_asset_data(ll_assets, hash_table_assets)
        usd = market.standardize_price("BTC", 10)
        self.assertEqual(usd, 124310,
            "Price returned must be converted to usd from Bitcoin value")

    def test_market_cap_sort(self):
        asset1 = Asset(1, "Bitcoin", "BTC", 23421, 12431, 1434,
                        363, 35636, 23452, 25)
        asset2 = Asset(2, "Ethereum", "ETH", 234, 14, 134, 365, 476,
                        41, 3412)

        ll_assets = DoubleLinkedList()

        ll_assets.insert_first(asset1)
        ll_assets.insert_first(asset2)


        hash_table_assets = HashTable(10)
        hash_table_assets.insert(asset1.symbol, asset1)
        hash_table_assets.insert(asset2.symbol, asset2)

        market = CurrentMarket()
        market.set_asset_data(ll_assets, hash_table_assets)

        array = market.linked_list_to_array_assets(ll_assets)
        market.set_assets_array(array)

        market.market_cap_sort()
        self.assertEqual(market.assets_array[0].symbol, "ETH",
                "The sort should be done from least to greatest.")

    def test_circulation_sort(self):
        asset1 = Asset(1, "Bitcoin", "BTC", 23421, 12431, 1434,
                        363, 35636, 23452, 25)
        asset2 = Asset(2, "Ethereum", "ETH", 234, 14, 134, 365, 476,
                        41, 3412)

        ll_assets = DoubleLinkedList()

        ll_assets.insert_first(asset1)
        ll_assets.insert_first(asset2)


        hash_table_assets = HashTable(10)
        hash_table_assets.insert(asset1.symbol, asset1)
        hash_table_assets.insert(asset2.symbol, asset2)

        market = CurrentMarket()
        market.set_asset_data(ll_assets, hash_table_assets)

        array = market.linked_list_to_array_assets(ll_assets)
        market.set_assets_array(array)

        market.circulation_sort()
        self.assertEqual(market.assets_array[0].symbol, "ETH",
                "The sort should be done from least to greatest.")

    
    def test_percent_sort(self):
        asset1 = Asset(1, "Bitcoin", "BTC", 23421, 12431, 1434,
                        363, 35636, 23452, 25)
        asset2 = Asset(2, "Ethereum", "ETH", 234, 14, 134, 365, 476,
                        41, 3412)

        ll_assets = DoubleLinkedList()

        ll_assets.insert_first(asset1)
        ll_assets.insert_first(asset2)


        hash_table_assets = HashTable(10)
        hash_table_assets.insert(asset1.symbol, asset1)
        hash_table_assets.insert(asset2.symbol, asset2)

        market = CurrentMarket()
        market.set_asset_data(ll_assets, hash_table_assets)

        array = market.linked_list_to_array_assets(ll_assets)
        market.set_assets_array(array)

        market.percent_sort()
        self.assertEqual(market.assets_array[0].symbol, "ETH",
                "The sort should be done from least to greatest.")
    
    def test_price_percent_sort(self):
        trade1 = Trade("BTCETH", "BTC", "ETH", 2, 5, 1, 3,
                4, 3, 5, 3, 5, 2, 2, 4, 5, 3, 2, 2, 2,1 ,3, 2)
        trade2 = Trade("OMGCHEESE", "OMG", "CHEESE", 20, 50, 10, 30,
                40, 30, 50, 30, 50, 20, 20, 40, 50, 30, 20, 20, 20, 10 ,30, 20)

        array = np.zeros(2, dtype=object)
        array[0] = trade2
        array[1] = trade1

        market = CurrentMarket()
        market.set_trades_array(array)
        market.price_percent_sort()

        self.assertEqual(market.trades_array[0].symbol, "BTCETH",
                    "Sort returns items by specific variable order smallest first")

    def test_volume_sort(self):
        trade1 = Trade("BTCETH", "BTC", "ETH", 2, 5, 1, 3,
                4, 3, 5, 3, 5, 2, 2, 4, 5, 3, 2, 2, 2,1 ,3, 2)
        trade2 = Trade("OMGCHEESE", "OMG", "CHEESE", 20, 50, 10, 30,
                40, 30, 50, 30, 50, 20, 20, 40, 50, 30, 20, 20, 20, 10 ,30, 20)

        array = np.zeros(2, dtype=object)
        array[0] = trade2
        array[1] = trade1

        market = CurrentMarket()
        market.set_trades_array(array)
        market.volume_sort()

        self.assertEqual(market.trades_array[0].symbol, "BTCETH",
                    "Sort returns items by specific variable order smallest first")

    def test_high_price_sort(self):
        trade1 = Trade("BTCETH", "BTC", "ETH", 2, 5, 1, 3,
                4, 3, 5, 3, 5, 2, 2, 4, 5, 3, 2, 2, 2,1 ,3, 2)
        trade2 = Trade("OMGCHEESE", "OMG", "CHEESE", 20, 50, 10, 30,
                40, 30, 50, 30, 50, 20, 20, 40, 50, 30, 20, 20, 20, 10 ,30, 20)

        array = np.zeros(2, dtype=object)
        array[0] = trade2
        array[1] = trade1

        market = CurrentMarket()
        market.set_trades_array(array)
        market.high_price_sort()

        self.assertEqual(market.trades_array[0].symbol, "BTCETH",
                    "Sort returns items by specific variable order smallest first")

    def test_remove_from_asset_ll(self):
        asset1 = Asset(1, "Bitcoin", "BTC", 23421, 12431, 1434,
                        363, 35636, 23452, 25)
        asset2 = Asset(2, "Ethereum", "ETH", 234, 14, 134, 365, 476,
                        41, 3412)

        ll_assets = DoubleLinkedList()
        ll_assets.insert_last(asset1)
        ll_assets.insert_last(asset2)

        hash_table = HashTable(10)

        market = CurrentMarket()
        market.set_asset_data(ll_assets, hash_table)

        market.remove_from_asset_ll("BTC")
        self.assertEqual(market.asset_linked_list.has("BTC"), False,
                    "After removal asset should not be in Linked List")

    def test_remove_from_trades_ll(self):
        trade1 = Trade("BTCETH", "BTC", "ETH", 2, 5, 1, 3,
                4, 3, 5, 3, 5, 2, 2, 4, 5, 3, 2, 2, 2,1 ,3, 2)
        trade2 = Trade("OMGCHEESE", "OMG", "CHEESE", 20, 50, 10, 30,
                40, 30, 50, 30, 50, 20, 20, 40, 50, 30, 20, 20, 20, 10 ,30, 20)

        ll_trades = DoubleLinkedList()
        ll_trades.insert_last(trade1)
        ll_trades.insert_last(trade2)

        hash_table = HashTable(10)

        market = CurrentMarket()
        market.set_trade_data(ll_trades, hash_table)

        market.remove_from_trades_ll("BTC")
        self.assertEqual(market.trade_linked_list.has("BTC"), False,
                    "After removal trade should not be in Linked List")

    def test_remove_from_asset_hash(self):
        asset1 = Asset(1, "Bitcoin", "BTC", 23421, 12431, 1434,
                        363, 35636, 23452, 25)
        asset2 = Asset(2, "Ethereum", "ETH", 234, 14, 134, 365, 476,
                        41, 3412)

        ll_assets = DoubleLinkedList()

        hash_table = HashTable(10)
        hash_table.insert(asset1.symbol, asset1)
        hash_table.insert(asset2.symbol, asset2)

        market = CurrentMarket()
        market.set_asset_data(ll_assets, hash_table)

        market.remove_from_asset_hash("ETH")
        self.assertEqual(market.assets_hashed.retrieve("ETH"), None,
                    "After removal asset should not be in Hash Table")

    def test_graphing(self):
        asset1 = Asset(1, "Bitcoin", "BTC", 23421, 12431, 1434,
                        363, 35636, 23452, 25)
        asset2 = Asset(2, "Ethereum", "ETH", 234, 14, 134, 365, 476,
                        41, 3412)

        assets_hashed = HashTable(10)
        assets_hashed.insert(asset1.symbol, asset1)
        assets_hashed.insert(asset2.symbol, asset2)

        ll_throw_away = DoubleLinkedList()

        trade1 = Trade("BTCETH", "BTC", "ETH", 2, 5, 1, 3,
                4, 3, 5, 3, 5, 2, 2, 4, 5, 3, 2, 2, 2,1 ,3, 2)
        trade2 = Trade("ETHBTC", "ETH", "BTC", 20, 50, 10, 30,
                40, 30, 50, 30, 50, 20, 20, 40, 50, 30, 20, 20, 20, 10 ,30, 20)

        trades_list = DoubleLinkedList()
        trades_list.insert_last(trade1)
        trades_list.insert_last(trade2)

        hash_throw_away = HashTable(10)

        market = CurrentMarket()
        market.set_asset_data(ll_throw_away, assets_hashed)
        market.set_trade_data(trades_list, hash_throw_away)

        market.graphing()
        self.assertEqual(market.trades_graph.get_vertex("ETH").data, asset2,
                    "Data on Vertex should be of the specific asset.")




















        

if __name__ == "__main__":
    unittest.main()