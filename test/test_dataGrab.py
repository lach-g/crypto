import sys
sys.path.append("../assignment")

import unittest
from dataGrabClass import DataGrab
from assetClass import Asset
from tradeClass import Trade
from currentMarketClass import CurrentMarket
from DoubleLinkedList_dsa import DoubleLinkedList, ListNode

class TestDataGrabClass(unittest.TestCase):

    def test_init(self):
        grab = DataGrab("assets.csv", "trades.csv")
        self.assertEqual(grab.assets_filename, "assets.csv",
                    "class variable should capture initial input in order.")

    def test_read_assets_to_linked_list(self):
        asset1 = Asset(1, "Bitcoin", "BTC", 23421, 12431, 1434,
                        363, 35636, 23452, 25)
        asset2 = Asset(2, "Ethereum", "ETH", 234, 14, 134, 365, 476,
                        41, 3412)

        ll_assets = DoubleLinkedList()

        ll_assets.insert_first(asset1)
        ll_assets.insert_first(asset2)

        grab = DataGrab()
        grab.set_assets_ll(ll_assets)
        obj_list = grab.read_assets_to_linked_list()
        self.assertEqual(obj_list.peek_first(), ll_assets.peek_first(), 
                        "Read assets should return a preprocessed linked list")

    def test_trades_to_linked_list(self):
        trade1 = Trade("BTCETH", "BTC", "ETH", 2, 5, 1, 3,
                4, 3, 5, 3, 5, 2, 2, 4, 5, 3, 2, 2, 2,1 ,3, 2)
        trade2 = Trade("OMGCHEESE", "OMG", "CHEESE", 20, 50, 10, 30,
                40, 30, 50, 30, 50, 20, 20, 40, 50, 30, 20, 20, 20, 10 ,30, 20)

        ll_trades = DoubleLinkedList()
        ll_trades.insert_last(trade1)
        ll_trades.insert_last(trade2)

        grab = DataGrab()
        grab.set_trades_linked_list(ll_trades)
        self.assertEqual(grab.read_trades_to_linked_list(), ll_trades,
                "The inputed tradfes linked list should be the same being returned")

    def test_dollar_string_to_num(self):
        grab = DataGrab()
        string = "$40,000"
        num = grab.dollar_string_to_num(string)
        self.assertEqual(num, 40000,
                "String to num should strip all extras and return int.")

    def test_process_assets_to_linked_list(self):
        grab = DataGrab("assets.csv")
        asset = grab.assets_ll.peek_first()
        self.assertEqual(asset.symbol, "BTC",
                    "Order of file parsing to object variable characteristics matters.")

    def test_process_trades_to_linked_list(self):
        grab = DataGrab(trades_filename="trades.csv")
        trade = grab.trades_ll.peek_first()
        self.assertEqual(trade.symbol, "ETHBTC",
                    "Order of file parsing to object variable characteristics matters.")

    def test_read_assets_to_hash(self):
        asset1 = Asset(1, "Bitcoin", "BTC", 23421, 12431, 1434,
                        363, 35636, 23452, 25)
        asset2 = Asset(2, "Ethereum", "ETH", 234, 14, 134, 365, 476,
                        41, 3412)
        ll_assets = DoubleLinkedList()
        ll_assets.insert_first(asset1)
        ll_assets.insert_first(asset2)

        grab = DataGrab()
        grab.set_assets_ll(ll_assets)
        hash_assets = grab.read_assets_to_hash()
        asset = hash_assets.retrieve("BTC")
        self.assertEqual(asset.symbol, "BTC",
                        "Hash table must store the full asset as the data.")

    def test_read_trades_to_hash(self):
        trade1 = Trade("BTCETH", "BTC", "ETH", 2, 5, 1, 3,
                4, 3, 5, 3, 5, 2, 2, 4, 5, 3, 2, 2, 2,1 ,3, 2)
        trade2 = Trade("OMGCHEESE", "OMG", "CHEESE", 20, 50, 10, 30,
                40, 30, 50, 30, 50, 20, 20, 40, 50, 30, 20, 20, 20, 10 ,30, 20)

        ll_trades = DoubleLinkedList()
        ll_trades.insert_last(trade1)
        ll_trades.insert_last(trade2)

        grab = DataGrab()
        grab.set_trades_linked_list(ll_trades)
        hash_trades = grab.read_trades_to_hash()
        trade = hash_trades.retrieve("BTCETH")
        self.assertEqual(trade.symbol, "BTCETH",
                        "Hash table must store the full trade as the data.")



if __name__ == "__main__":
    unittest.main()