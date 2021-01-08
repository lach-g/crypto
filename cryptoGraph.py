import sys
from menu import cryptoMenu

def main():
    menu = cryptoMenu()    
    terminal_commands = len(sys.argv)
    if terminal_commands < 2 or terminal_commands > 4:
            menu.usage_info()
            return -1

    else:
        user_input = sys.argv[1]

        if terminal_commands == 2 and user_input == "-i":
                menu.clear_screen()
                choice = menu.main_menu_options()
                while choice:
                        if choice == 9:
                                menu.clear_screen()
                                break
                        menu.direct_choice(choice)
                        choice = menu.main_menu_options()
        elif terminal_commands == 4 and user_input == "-r":
                asset_file = sys.argv[2]
                trade_file = sys.argv[3]
                menu.assign_assets_to_market(asset_file)
                menu.assign_trades_to_market(trade_file)
                menu.clear_screen()
                choice = menu.main_menu_options()
                while choice:
                        if choice == 9:
                                menu.clear_screen()
                                break
                        menu.direct_choice(choice)
                        choice = menu.main_menu_options()

                print("Enter report mode usage")


if __name__ == "__main__":
    main()

    

