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
                menu.repeat_til_quit()
        elif terminal_commands == 4 and user_input == "-r":
                asset_file = sys.argv[2]
                trade_file = sys.argv[3]
                menu.assign_assets_to_market(asset_file)
                menu.assign_trades_to_market(trade_file)

                menu.repeat_til_quit()

if __name__ == "__main__":
    main()

    
'''
if linked_list.count == 1:
            linked_list.head = None
            linked_list.tail = None
            print("Successfully filtered out only node")
        
        current_node = linked_list.head
        moved = 0
        while current_node != None:
            if current_node.data.symbol == to_remove:
                if moved == 0:
                    new_first_node = current_node.next
                    linked_list.head = new_first_node
                    new_first_node.prev = linked_list.head
                elif moved == linked_list.count:
                    prev_node = current_node.prev
                    prev_node.next = linked_list.tail
                    linked_list.tail = prev_node
                else:
                    prev_node = current_node.prev
                    new_next_node = current_node.next
                    prev_node.next = new_next_node
                linked_list.count -= 1
                print("Successfully filtered out", current_node.data.symbol)
                break
            else:
                moved += 1
                current_node = current_node.next
'''