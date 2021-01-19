import csv
from HashTable_dsa import HashEntry, HashTable
from Graph_dsa import Graph, Vertex
from DoubleLinkedList_dsa import DoubleLinkedList, ListNode
from assetClass import Asset
from tradeClass import Trade

class DataGrab:
    """
    Contains the class definition of a data grab object for parsing and loading .csv
    files into a current market object
    """

    def __init__(self, assets_filename=None, trades_filename=None):
        """Object can save filenames of different types and is given a standard number
            of assets and trades for the hash table, which is adjusted with each
            addition."""
        self.assets_filename = assets_filename
        self.trades_filename = trades_filename
        self.num_trades = 1500
        self.num_stocks = 2600

        if self.assets_filename != None:
            self.assets_ll = self.process_assets_to_linked_list()

        if self.trades_filename != None:
            self.trades_ll = self.process_trades_to_linked_list()

    def set_assets_ll(self, ll):
        """Assigns the objects assets linked list to a new linked list."""
        self.assets_ll = ll

    def read_assets_to_linked_list(self):
        """Returns the asset linked list already processed."""
        return self.assets_ll

    def read_trades_to_linked_list(self):
        """Returns the trades linked list already processed."""
        return self.trades_ll

    def dollar_string_to_num(self, string):
        """Parses the dollar value to return a usable float."""
        no_dollar = string[1:]
        no_spaces = no_dollar.strip()
        num = float(no_spaces.replace(",", ""))
        return num

    def process_assets_to_linked_list(self):
        """Using filename variable for assets opens and reads in the asset data
            based on the predetermined file format parsing some important data points."""
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

                    if row[10] == "> 9000%":
                        row[10] = "9000%"

                    price = self.dollar_string_to_num(row[5])

                    file_list.insert_last(Asset(row[0],
                                                row[1],
                                                row[2],
                                                row[4],
                                                price,
                                                row[7],
                                                row[8],
                                                row[9][:-1],
                                                row[10][:-1],
                                                row[11][:-1]))
                return file_list
        except Exception as e:
            print(e)

    def process_trades_to_linked_list(self):
        """Using filename variable for trades opens and reads in the asset data
            based on the predetermined file format."""
        try:
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
        except Exception as e:
            print(e)

    def read_assets_to_hash(self):
        """Loops through a non-empty assets linked list inserting the symbol
        as the key and the asset object as the value."""
        if self.assets_ll != None:
            hash_table = HashTable(self.num_stocks)
            for i in self.assets_ll:
                hash_table.insert(str(i.symbol), i)
            return hash_table

    def read_trades_to_hash(self):
        """Loops through a non-empty trades linked list inserting the symbol
        as the key and the trades object as the value."""
        if self.trades_ll != None:
            hash_table = HashTable(self.num_trades)
            for i in self.trades_ll:
                hash_table.insert(str(i.symbol), i)
            return hash_table

    def set_trades_linked_list(self, to_set):
        """Switches out the current trades linked list for an update."""
        self.trades_ll = to_set
