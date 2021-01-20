from DoubleLinkedList_dsa import ListNode, DoubleLinkedList

class Stack:
    """
    Data Structure written and previously submitted, it is used for
    the last in first out functionality during traversals
    """
    def __init__(self):
        """Is actually implemented on top of a Double Linked List"""
        self.stack = DoubleLinkedList()

    def __str__(self):
        """For iteration purposes."""
        return self.stack.__str__()

    def __iter__(self):
        """For iteration purposes."""
        curr_node = self.stack.head
        while curr_node != None:
            yield curr_node.data
            curr_node = curr_node.next
    
    def push(self, obj):
        """Function is O(1) with Double Linked List having a head,
            Vertex is deleted."""
        self.stack.insert_first(obj)

    def pull(self):
        """Function is O(1) with Double Linked List having a head,
            Vertex is deleted."""
        return self.stack.remove_first()

    def top(self):
        """Operation is O(1) with head, does not delete item."""
        return self.stack.peek_first()

