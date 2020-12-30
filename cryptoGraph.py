import sys
from marketClass import Market

def main():
    terminal_commands = len(sys.argv)
    user_input = sys.argv[1]

    if terminal_commands == 2 and user_input == "-i":
            print("Enter interactive testing environment")
    elif terminal_commands == 4 and user_input == "-r":
            asset_file = sys.argv[2]
            trade_file = sys.argv[3]
            print("Enter report mode usage")
    else:
        print("Usage info function here")
        return -1


if __name__ == "__main__":
    main()

    

