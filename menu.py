from os import system
from time import sleep
from dataGrabClass import DataGrab
from assetClass import Asset
from currentMarketClass import CurrentMarket
from Pickling import Pickle_Menu

import keyboard
import sys

class cryptoMenu:

    def __init__(self):
        self.current_market = CurrentMarket()


    def usage_info(self):
        print("\nUsage:")
        print("python3 cryptoGraph.py [options]\n")
        print("Options:")
        print("-i\tWill enable interactive testing environment")
        print("-r <asset_file.csv> <trade_file.csv>\tWill enable report mode")

    def repeat_til_quit(self):
        self.clear_screen()
        choice = self.main_menu_options()
        while choice:
            if choice == 9:
                self.clear_screen()
                break
            self.direct_choice(choice)
            choice = self.main_menu_options()

    def main_menu_options(self):
        num_menu_options = self.adjust_option_num(9)
        print("------------------------")
        print("CRYPTOGRAPH MENU OPTIONS")
        print("     ENTER NUMBER")
        print("------------------------")
        print("(1) Load data")
        print("(2) Find and display asset details")
        print("(3) Find and display trade details")
        print("(4) Find and display potential trade paths")
        print("(5) Set asset filter")
        print("(6) Asset overview")
        print("(7) Trade overview")
        print("(8) Save data")
        print("(9) Exit")
        print("(10) Find edges of asset")

        while True:
            try:
                choice = int(input("Enter choice: "))
                if choice > 0 and choice < (num_menu_options):
                    return choice
                print("Invalid choice entered")
            except Exception as e:
                print(e)

    def direct_choice(self, choice):
        if choice == 1:
            self.loading_data_menu()
        elif choice == 2:
            self.asset_details_menu()
        elif choice == 3:
            self.trade_details_menu()
        elif choice == 4:
            self.graph_current_market()
        elif choice == 5:
            self.set_asset_filter()
        elif choice == 6:
            self.asset_overview()
        elif choice == 7:
            self.trade_overview()
        elif choice == 8:
            self.save_data_menu()
        elif choice == 0:
            self.current_market.graphing()
            input_vert = str(input("Vertex:"))
            self.current_market.trades_graph.display_edges(input_vert)

    def loading_data_menu(self):
        self.clear_screen()
        num_menu_options = self.adjust_option_num(3)
        csv_extension = ".csv"
        object_extension = ".obj"
        print("LOADING DATA")
        print("------")
        print("Type of file to load: (1) Asset file (2) Trade file (3) Object file\n")

        # Asset or trade file to process
        while True:
            try:
                choice = int(input("Enter choice: "))
                if choice > 0 and choice < (num_menu_options):
                    break
                print("Invalid choice entered")
            except Exception as e:
                print(e)

        # Getting filename input
        while True:
            try:
                file = str(input("Enter filename (ending in .csv or .obj): "))
                if file[-4:] == csv_extension or file[-4:] == object_extension and len(file) > 4:
                    break
                print("Invalid filename entered")
            except Exception as e:
                print(e)

        if choice == 1:
            self.assign_assets_to_market(file)
            print("\n---ASSET FILE LOADED---\n")
        elif choice == 2:
            self.assign_trades_to_market(file)
            print("\n---TRADES FILE LOADED---\n")
        elif choice == 3:
            pickle_obj = Pickle_Menu()
            self.current_market = pickle_obj.load(file)
            if self.current_market != None:
                print("\n---OBJECT FILE LOADED---\n")

    def assign_assets_to_market(self, filename):
        data = DataGrab(assets_filename=filename)
        self.current_market.set_asset_data(data.read_assets_to_linked_list(),
                                                data.read_assets_to_hash())

    def assign_trades_to_market(self, filename):
        data = DataGrab(trades_filename=filename)
        self.current_market.set_trade_data(data.read_trades_to_linked_list(),
                                                data.read_trades_to_hash())

    def asset_details_menu(self):
        if self.current_market.has_asset_data() == False:
                print("\n--LOAD ASSETS DATA FIRST--\n")
        else:
            self.clear_screen()
            print("\nFIND ASSET DETAILS")
            print("------")
            while True:
                try:
                    symbol = str(input("Enter asset symbol ( eg. Bitcoin is BTC): "))
                    if len(symbol) > 2:
                        asset_data = self.current_market.find_asset_details(symbol)
                        if asset_data != None:
                            asset_data.print_info()
                        else:
                            print("Asset symbol not found")
                        break
                    print("Invalid symbol entered")
                except Exception as e:
                    print("Error: ", e)
        
    def trade_details_menu(self):
        if self.current_market.has_trades_data() == False:
                print("\n--LOAD TRADES DATA FIRST--\n")
        else:       
            self.clear_screen()
            print("\nFIND TRADE DETAILS")
            print("------")
            while True:
                try:
                    symbol = str(input("Enter trades symbol (eg. Bitcoin to Ethereum is BTCETH): "))
                    if len(symbol) > 2:
                        trade_data = self.current_market.find_trade_details(symbol)
                        if trade_data != None:
                            trade_data.print_info()
                        else:
                            print("Trade symbol not found")
                        break
                    print("Invalid symbol entered")
                except Exception as e:
                    print("Error: ", e)

    def set_asset_filter(self):
        if self.current_market.has_asset_data() == False or self.current_market.has_trades_data == False:
                print("\n--LOAD ASSETS AND TRADES DATA FIRST--\n")
        else:
            self.clear_screen()
            print("\nFILTER ASSET OUT OF CURRENT MARKET"
                    "\n(INCLUDING ALL TRADES OF ASSET)"
                    "\n--------------------------------------------")
            while True:
                try:
                    symbol = str(input("Enter asset symbol to filter out ( eg. Bitcoin is BTC): "))
                    if len(symbol) > 2:
                        asset_data = self.current_market.find_asset_details(symbol)
                        if asset_data != None:
                            # will also remove from array as it is made at each run
                            self.remove_from_linked_lists(asset_data.symbol)
                            self.remove_from_hash_tables(asset_data.symbol)
                        else:
                            print("Asset symbol not found")
                        break
                    print("Invalid symbol entered")
                except Exception as e:
                    print("Error: ", e)

    def remove_from_linked_lists(self, to_remove):
        self.current_market.remove_from_asset_ll(to_remove)
        self.current_market.remove_from_trades_ll(to_remove)

    def remove_from_hash_tables(self, to_remove):
        self.current_market.remove_from_asset_hash(to_remove)
        self.current_market.remove_from_trade_hash(to_remove)

    def asset_overview(self):
        if self.current_market.has_asset_data() == False:
                print("\n--LOAD ASSETS DATA FIRST--\n")
        else:
            self.clear_screen()
            self.current_market.hidden_assets_overview()

    def trade_overview(self):
        if self.current_market.trade_list_has_data() == False:
                print("\n--LOAD TRADES DATA FIRST--\n")
        else:
            self.clear_screen()
            self.current_market.hidden_trades_overview()

    def save_data_menu(self):
        if self.current_market.has_trades_data() == False:
                print("\n--LOAD TRADES DATA FIRST--\n")
        else:
            self.clear_screen()
            print("SAVE DATA")
            print("------")
            name = str(input("Choose filename to save object as: "))
            name = name + ".obj"
            pickle_obj = Pickle_Menu(self.current_market)
            pickle_obj.save(name)
            print("\n---MARKET SAVED---\n")

    def adjust_option_num(self, num):
        return num + 1

    def clear_screen(self):
        system("clear")

    def graph_current_market(self):
        if self.current_market.has_trades_data() == False and self.current_market.has_asset_data() == False:
                print("\n--LOAD ASSETS AND TRADES DATA FIRST--\n")
        else:       
            self.clear_screen()
            print("Only trades with asset data will be processed")
            self.current_market.graphing()
            while True:
                try:
                    base_symbol = str(input("Enter base asset symbol( eg. Bitcoin is BTC): "))
                    quote_symbol = str(input("Enter quote asset symbol( eg. Bitcoin is BTC): "))
                    if len(base_symbol) > 2 or len(quote_symbol) > 2:
                        asset_data = self.current_market.find_asset_details(base_symbol)
                        if asset_data != None:
                            self.current_market.find_direct_path(base_symbol, quote_symbol)

                        else:
                            print("Asset symbol not found")
                        break
                    print("Invalid symbol entered")
                except Exception as e:
                    print("Error: ", e)
        