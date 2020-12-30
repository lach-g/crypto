import csv
from HashTable_dsa import HashEntry, HashTable
from Graph_dsa import Graph, Vertex
from DoubleLinkedList_dsa import DoubleLinkedList, ListNode
from assetClass import Asset
from tradeClass import Trade

class Market:

    def __init__(self, assets_filename, num_stocks, trades_filename=None, num_trades=None):
        self.assets_filename = assets_filename
        self.num_stocks = num_stocks
        self.trades_filename = trades_filename
        self.num_trades = num_trades
        self.assets = self.read_assets_to_hash()

    def read_assets_to_linked_list(self):
        with open(self.assets_filename, 'r') as obj:
            file_list = DoubleLinkedList()
            reader = csv.reader(obj)
            count = 0
            for row in reader:
                if count == 0:
                    count += 1
                    continue
                file_list.insert_last(Asset(row[0],
                                            row[1],
                                            row[2],
                                            row[4],
                                            row[5],
                                            row[7],
                                            row[8],
                                            row[9],
                                            row[10],
                                            row[11]))
            return file_list

    def read_trades_to_linked_list(self):
        with open(self.trades_filename, 'r') as obj:
            file_list = DoubleLinkedList()
            reader = csv.reader(obj)
            count = 0
            for row in reader:
                if count == 0:
                    count += 1
                    continue
                file_list.insert_last(Trade(row[0],
                                            row[1],
                                            row[2],
                                            row[3],
                                            row[4],
                                            row[5],
                                            row[6],
                                            row[7],
                                            row[8],
                                            row[9],
                                            row[10],
                                            row[11],
                                            row[12],
                                            row[13],
                                            row[14],
                                            row[15],
                                            row[16],
                                            row[17],
                                            row[18],
                                            row[19],
                                            row[20],
                                            row[21],
                                            row[22]))
            return file_list

    def read_assets_to_hash(self):
        file_list = self.read_assets_to_linked_list()
        hash_table = HashTable(self.num_stocks)
        for i in file_list:
            hash_table.insert(str(i.symbol), i)
        return hash_table

    def graph(self):
        trades = self.read_trades_to_linked_list()
        trades_graph = Graph()
        for trade in trades:
            asset_selling = self.assets.retrieve(trade.base_asset)
            asset_buying = self.assets.retrieve(trade.quote_asset)
            if asset_selling != None and asset_buying != None:
                if trades_graph.has_vertex(trade.base_asset) == False:
                    trades_graph.add_vertex(trade.base_asset, asset_selling)
                if trades_graph.has_vertex(trade.quote_asset) == False:
                    trades_graph.add_vertex(trade.quote_asset, asset_buying)
                trades_graph.add_edge(trade.base_asset, trade.quote_asset)
            else:
                if trades_graph.has_vertex(trade.base_asset) == False:
                    trades_graph.add_vertex(trade.base_asset)
                if trades_graph.has_vertex(trade.quote_asset) == False:
                    trades_graph.add_vertex(trade.quote_asset)
                trades_graph.add_edge(trade.base_asset, trade.quote_asset)

        return trades_graph