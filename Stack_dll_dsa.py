from DoubleLinkedList_dsa import ListNode, DoubleLinkedList

class Stack:

    def __init__(self):
        self.stack = DoubleLinkedList()

    def __str__(self):
        return self.stack.__str__()

    def __iter__(self):
        curr_node = self.stack.head
        while curr_node != None:
            yield curr_node.data
            curr_node = curr_node.next
    
    def push(self, obj):
        self.stack.insert_first(obj)

    def pull(self):
        return self.stack.remove_first()

    def top(self):
        return self.stack.peek_first()

# Testing
if __name__ == "__main__":

    test = Stack()
    test.push(20)
    test.push(5)
    test.push(8)
    print("Starting with: ", test)
    print("Top should be 8: ", test.top())
    print("Pull should be 8: ", test.pull())
    print("After pull stack is (using linked list __str__ format): ", test)
    print()
    print("Testing iterator:")
    for i in test:
        print(i)