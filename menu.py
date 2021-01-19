from os import system
from dataGrabClass import DataGrab
from assetClass import Asset
from currentMarketClass import CurrentMarket
from Pickling import Pickle_Menu

class cryptoMenu:

    def __init__(self):
        """Creates a current market object."""
        self.current_market = CurrentMarket()

    def usage_info(self):
        """Print help to command line if not run correctly."""
        print("\nUsage:\npython3 cryptoGraph.py [options]\n\nOptions:"
                "\n-i\tWill enable interactive testing environment"
                "\n-r <asset_file.csv> <trade_file.csv>\tWill enable report mode")

    def repeat_til_quit(self):
        """Clears screen, displays menu options and stores user choice,
            repeating if choice is not 9."""
        self.clear_screen()
        choice = self.main_menu_options()
        while choice:
            if choice == 9:
                self.clear_screen()
                break
            self.direct_choice(choice)
            choice = self.main_menu_options()

    def main_menu_options(self):
        """Prints menu options to command line and get's user input
            checking it is valid."""
        num_menu_options = self.adjust_option_num(10)
        print("------------------------\n"
                "CRYPTOGRAPH MENU OPTIONS\n"
                "     ENTER NUMBER\n"
                "------------------------\n"
                "(1) Load data\n"
                "(2) Find and display asset details\n"
                "(3) Find and display trade details\n"
                "(4) Find and display potential trade paths\n"
                "(5) Set asset filter\n"
                "(6) Asset overview\n"
                "(7) Trade overview\n"
                "(8) Save data\n"
                "(9) Exit\n"
                "(10) Refresh Asset data to Current Market Conditions\n"
                "NOTE--> Asset data must be loaded to view all options...\n")

        user_choice = self.get_int_inside_range(0, 11)
        return user_choice

    def direct_choice(self, choice):
        """Begins a menu option based on the user choice."""
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
        elif choice == 10:
            self.extra_feature()


    def loading_data_menu(self):
        """Takes filename as input, checks validity, directs choice to
            correct file parsing function."""
        self.clear_screen()
        num_menu_options = self.adjust_option_num(3)
        csv_extension = ".csv"
        object_extension = ".obj"
        print("LOADING DATA\n"
                "------\n"
                "Type of file to load: (1) Asset file (2) Trade file (3) Object file\n")

        user_choice = self.get_int_inside_range(0, 4)
        while True:
            try:
                file = str(input("Enter filename (ending in .csv or .obj): "))
                if file[-4:] == csv_extension or file[-4:] == object_extension and len(file) > 4:
                    break
                print("Invalid filename entered")
            except Exception as e:
                print(e)

        if user_choice == 1:
            self.assign_assets_to_market(file)
            if self.current_market.has_asset_data():
                print("\n---ASSET FILE LOADED---\n")
        elif user_choice == 2:
            self.assign_trades_to_market(file)
            if self.current_market.has_trades_data():
                print("\n---TRADES FILE LOADED---\n")
        elif user_choice == 3:
            pickle_obj = Pickle_Menu()
            self.current_market = pickle_obj.load(file)
            if self.current_market != None:
                print("\n---OBJECT FILE LOADED---\n")

    def get_int_inside_range(self, start, end):
        """Gets user input of integer in given range."""
        while True:
            try:
                choice = int(input("Enter choice: "))
                if choice >= start and choice < end:
                    return choice
                    break
                print("Invalid choice entered")
            except Exception as e:
                print(e)

    def assign_assets_to_market(self, filename):
        """Pulls data from file and enters the data parsed into the current asset market."""
        data = DataGrab(assets_filename=filename)
        self.current_market.set_asset_data(data.read_assets_to_linked_list(),
                                                data.read_assets_to_hash())

    def assign_trades_to_market(self, filename):
        """Pulls data from file and enters the data parsed into the current trades market."""
        data = DataGrab(trades_filename=filename)
        self.current_market.set_trade_data(data.read_trades_to_linked_list(),
                                                data.read_trades_to_hash())

    def asset_details_menu(self):
        """Gets user input for asset symbol and hash retrieves in O(1) if it exists, printing
            result to command line."""
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
        """Gets user input for trade symbol and hash retrieves in O(1) if it exists, printing
            result to command line."""
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
        """Wrapper for getting user input for asset to delete, will remove from all data structures
            including trades."""
        if self.current_market.has_asset_data() == False or self.current_market.has_trades_data == False:
                print("\n--LOAD ASSETS AND TRADES DATA FIRST--\n")
        else:
            self.clear_screen()
            print("\nFILTER ASSET OUT OF CURRENT MARKET"
                    "\n(INCLUDING ALL TRADES OF ASSET IF LOADED)"
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
        """Wrapper to execute asset and trade linked list removal of symbol."""
        if self.current_market.trade_list_has_data() == False:
            self.current_market.remove_from_asset_ll(to_remove)
        else:
            self.current_market.remove_from_asset_ll(to_remove)
            self.current_market.remove_from_trades_ll(to_remove)

    def remove_from_hash_tables(self, to_remove):
        """Wrapper to execute asset and trade hash table removal of symbol."""
        self.current_market.remove_from_asset_hash(to_remove)
        self.current_market.remove_from_trade_hash()

    def asset_overview(self):
        """Checks if asset data is loaded printing to command line
            an overview if so."""
        if self.current_market.has_asset_data() == False:
                print("\n--LOAD ASSETS DATA FIRST--\n")
        else:
            self.clear_screen()
            self.current_market.collected_assets_overview()

    def trade_overview(self):
        """Checks if trades data is loaded printing to command line
            an overview if so."""
        if self.current_market.trade_list_has_data() == False or self.current_market.has_asset_data() == False:
                print("\n--LOAD ASSETS AND TRADE DATA FIRST--\n")
        else:
            self.clear_screen()
            self.current_market.collected_trades_overview()

    def save_data_menu(self):
        """Checks if asset data exists, gets filename and adds .obj
            pickling the current market object to current directory of user."""
        if self.current_market.has_asset_data() == False:
                print("\n--LOAD DATA FIRST--\n")
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
        """Returns a number increased by one."""
        return num + 1

    def clear_screen(self):
        """Sends a system command clearing the screen."""
        system("clear")

    def graph_current_market(self):
        """Checks if either asset or trade data is loaded, doing a breadth first and depth first
            traversal of user picked assets printing the paths to the command line if so."""
        if self.current_market.has_trades_data() == False or self.current_market.has_asset_data() == False:
                print("\n--LOAD ASSETS AND TRADES DATA FIRST--\n")
        else:       
            self.clear_screen()
            print("TRADE PATHS\n"
                    "-----------\n"
                    "Only trades with asset data will be processed")
            self.current_market.graphing()
            while True:
                try:
                    base_symbol = str(input("\nEnter base asset symbol( eg. Bitcoin is BTC): "))
                    quote_symbol = str(input("Enter quote asset symbol( eg. Bitcoin is BTC): "))
                    if len(base_symbol) > 2 or len(quote_symbol) > 2:
                        asset_data = self.current_market.find_asset_details(base_symbol)
                        if asset_data != None:
                            self.current_market.find_direct_paths(base_symbol, quote_symbol)
                            print("\n---SCROLL TO TOP FOR ALL INFO---\n")
                        else:
                            print("Asset symbol not found")
                        break
                    print("Invalid symbol entered")
                except Exception as e:
                    print("Error: ", e)



    def extra_feature(self):
        """Makes request to crypto market for latest asset data
            iterating through the current asset linked list updating
            matches with the newest corresponding data."""
        filename = "latest_market_data.obj"
        if self.current_market.has_asset_data() == False:
                print("\n--LOAD ASSETS DATA FIRST--\n")
        else:
            import pickle
            from requests import Request, Session
            from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
            import json


            API_KEY = "4c4e130c-641a-4e1d-825c-8e732d456e9f"      
            URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest" 
            parameters = {
                "convert": "USD"
            }

            headers = {
                "Accepts": "application/json",
                "X-CMC_PRO_API_KEY": "4c4e130c-641a-4e1d-825c-8e732d456e9f" 
            }

            session = Session()
            session.headers.update(headers)

            try:
                response = session.get(URL, params=parameters)
                data = json.loads(response.text)
                for i in data["data"]:
                    asset = self.current_market.assets_hashed.retrieve(i["symbol"])
                    if asset != None:
                        asset.market_cap = i["quote"]["USD"]["market_cap"]
                        asset.price = i["quote"]["USD"]["price"]
                        asset.circulating_supply = i["circulating_supply"]
                        asset.volume = i["quote"]["USD"]["volume_24h"]
                        asset.percent_1_hour = i["quote"]["USD"]["percent_change_1h"]
                        asset.percent_24_hours = i["quote"]["USD"]["percent_change_24h"]
                        asset.percent_7_days = i["quote"]["USD"]["percent_change_7d"]
                print("Current data has been loaded...")

            except (ConnectionError, Timeout, TooManyRedirects) as e:
                print(e)

        