import sys
from menu import cryptoMenu

def main():
    terminal_commands = len(sys.argv)
    user_input = sys.argv[1]

    if terminal_commands == 2 and user_input == "-i":
            menu = cryptoMenu()
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
            print("Enter report mode usage")
    else:
        print("Usage info function here")
        return -1


if __name__ == "__main__":
    main()

    

