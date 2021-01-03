class cryptoMenu:

    def main_menu_options(self):
        num_menu_options = 9
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
                if choice > 0 and choice < (num_menu_options + 1):
                    return choice
                print("Invalid choice entered")
            except Exception as e:
                print(e)
