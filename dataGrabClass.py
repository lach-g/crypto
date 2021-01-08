import csv
from HashTable_dsa import HashEntry, HashTable
from Graph_dsa import Graph, Vertex
from DoubleLinkedList_dsa import DoubleLinkedList, ListNode
from assetClass import Asset
from tradeClass import Trade

class DataGrab:

    def __init__(self, assets_filename=None, trades_filename=None):
        self.assets_filename = assets_filename
        self.trades_filename = trades_filename
        self.num_trades = 1500
        self.num_stocks = 2600

        if self.assets_filename != None:
            self.assets_ll = self.__read_assets_to_linked_list()

        if self.trades_filename != None:
            self.trades_ll = self.__read_trades_to_linked_list()

    def read_assets_to_linked_list(self):
        return self.assets_ll

    def read_trades_to_linked_list(self):
        return self.trades_ll

    def __read_assets_to_linked_list(self):
        try:
            with open(self.assets_filename, 'r') as obj:
                file_list = DoubleLinkedList()
                reader = csv.reader(obj)
                count = 0
                for row in reader:
                    if count == 0:
                        count += 1
                        continue
                    if row[7] == "?":
                        row[7] = 0
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
        except Exception as e:
            print(e)

    def __read_trades_to_linked_list(self):
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
        if self.assets_ll != None:
            hash_table = HashTable(self.num_stocks)
            for i in self.assets_ll:
                hash_table.insert(str(i.symbol), i)
            return hash_table

    def read_trades_to_hash(self):
        if self.trades_ll != None:
            hash_table = HashTable(self.num_trades)
            for i in self.trades_ll:
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