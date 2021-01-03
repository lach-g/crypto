from os import system
from time import sleep
from dataGrabClass import DataGrab
from assetClass import Asset
from currentMarketClass import CurrentMarket

class cryptoMenu:

    def __init__(self):
        self.current_market = CurrentMarket()

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
            market = self.loading_data_menu()
            self.current_market.add_market(market)
        elif choice == 2:
            if self.current_market.is_empty():
                print("\n--Load asset data first--\n")
            else:
                print("\nFinding asset details")
                self.asset_details_menu()
        elif choice == 3:
            print("\nFinding trade details")
        elif choice == 4:
            print("\nFinding trade paths")
        elif choice == 5:
            print("\nSetting asset filter")
        elif choice == 6:
            print("\nShowing asset overview")
        elif choice == 7:
            print("\nShowing trade overview")
        elif choice == 8:
            print("\nSaving data")

    def loading_data_menu(self):
        self.clear_screen()
        num_menu_options = self.adjust_option_num(2)
        csv_extension = ".csv"
        print("\nLOADING DATA")
        print("------")
        print("Type of file to load: (1) Asset file (2) Trade file\n")

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
                file = str(input("Enter filename (ending in .csv): "))
                if file[-4:] == csv_extension and len(file) > 4:
                    break
                print("Invalid filename entered")
            except Exception as e:
                print(e)

        if choice == 1:
            market = DataGrab(assets_filename=file)
            print("Assset file loaded")
        elif choice == 2:
            market = DataGrab(trades_filename=file)
            print("Trades file loaded")
        return market

    def asset_details_menu(self):
        self.clear_screen()
        while True:
            try:
                symbol = str(input("Enter asset symbol (Bitcoin is BTC): "))
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
        

    def adjust_option_num(self, num):
        return num + 1

    def clear_screen(self):
        system("clear")

            