from DoubleLinkedList_dsa import ListNode, DoubleLinkedList

class Queue:
    """
    Data Structure written and previously submitted, it is used
    for the first in first out functionality during traversals
    """
    def __init__(self):
        """Is actually implemented on top of a Double Linked List"""
        self.queue = DoubleLinkedList()

    def __str__(self):
        """For iteration purposes."""
        return self.queue.__str__()

    def __iter__(self):
        """For iteration purposes."""
        curr_node = self.queue.head
        while curr_node != None:
            yield curr_node.data
            curr_node = curr_node.next

    def enqueue(self, obj):
        """Function is O(1) with Double Linked List having a tail,
            Vertex is deleted."""
        self.queue.insert_last(obj)

    def dequeue(self):
        """Function is O(1) with Double Linked List having a head,
            Vertex is deleted."""
        return self.queue.remove_first()

    def peek(self):
        """Operation is O(1) with head, does not delete item."""
        return self.queue.peek_first()

    def has(self, data):
        """Wrapper for Double Linked List function, returning boolean
            if data is in list; is O(n)"""
        return self.queue.has(data)

    def count(self):
        """Returns integer of Double Linked List count."""
        return self.queue.count

