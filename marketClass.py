import csv
from HashTable_dsa import HashEntry, HashTable
from LinkedList_dsa import LinkedList, ListNode
from assetClass import Asset
from tradeClass import Trade

class Market:

    def __init__(self, filename, num_stocks, num_trades=None):
        self.filename = filename
        self.num_stocks = num_stocks
        self.num_trades = num_trades

    def read_assets_to_linked_list(self):
        with open(self.filename, 'r') as obj:
            file_list = LinkedList()
            reader = csv.reader(obj)
            for row in reader:
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
        with open(self.filename, 'r') as obj:
            file_list = LinkedList()
            reader = csv.reader(obj)
            for row in reader:
                file_list.insert_last(Trade(row[0],
                                            row[1],
                                            row[2],
                                            row[4],
                                            row[5],
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
                                            row[11],
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
