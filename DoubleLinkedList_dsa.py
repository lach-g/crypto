
class ListNode:
    def __init__(self, data):
        """Creates List Node object containing the value and links to the
            adjacent nodes."""
        self.data = data
        self.next = None
        self.prev = None
    

class DoubleLinkedList:
    """
    Data Structure written and previously submitted, used for it's iterative
    expanding capabilities
    """
    def __init__(self):
        """Creates a Double Linked List Object that chains List Nodes together
        starting at the head and finishing at the tail with a count."""
        self.head = None
        self.tail = None
        self.count = 0

    def __iter__(self):
        """Enables iteration"""
        self.curr = self.head
        return self

    def __next__(self):
        """Enables iteration"""
        curr_val = None
        if self.curr == None:
            raise StopIteration
        else:
            curr_val = self.curr.data
            self.curr = self.curr.next
        return curr_val

    def __str__(self):
        """Formatting printing the Linked List object to the command line."""
        db_ll = " "
        curr_node = self.head
        if self.is_empty():
            return "Linked List is empty"
        else:
            while curr_node.next != None:
                db_ll += str(curr_node.data) + " "
                curr_node = curr_node.next
            return "LIST:" + db_ll + str(curr_node.data)

    def is_empty(self):
        """Returns a bool true if the head of the list is empty."""
        if self.head == None:
            return True
        else:
            return False

    def insert_first(self, data):
        """Points the head to the new List Node, and connects the previous first Node"""
        new_node = ListNode(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
        self.count += 1

    def insert_last(self, data):
        """Points the tail to the new List Node and connects the previous last Node"""
        new_node = ListNode(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node
            self.tail = new_node

        self.count += 1

    def peek_first(self):
        """O(1) operation as head always points to the first node; returns the Node data."""
        if self.is_empty():
            return None
        else:
            first_node = self.head
            return first_node.data

    def peek_last(self):
        """O(1) operation as tail always points to the first node; returns the Node data."""
        if self.is_empty():
            raise ValueError("Double Linked List is empty")
        else:
            last_node = self.tail
            return last_node.data

    def remove_first(self):
        """Return the first Node in O(1) and connects the head with
            the next first node to remove it; while making the Node's prev
            point None."""
        first_node = self.head
        if self.is_empty():
            raise ValueError("Double Linked List is empty")
        elif first_node.next == None:
            self.head = None
            self.tail = None
            self.count -= 1
            return first_node.data
        else:
            rep_node = first_node.next
            self.head = rep_node
            rep_node.prev = None
            self.count -= 1
            return first_node.data

    def remove_last(self):
        """Returns the last Node in O(1) connecting the tail with the second last node."""
        last_node = self.tail
        if self.is_empty():
            raise ValueError("Double Linked List is empty")
        elif last_node.prev == None:
            self.head = None
            self.tail = None
            self.count -= 1
            return last_node.data
        else:
            last_node = self.tail
            rep_node = last_node.prev
            self.tail = rep_node
            rep_node.next = None
            self.count -= 1
            return last_node.data

    def has(self, data):
        """Boolean that iterates through the linked list returning true
            if the data is a match to any data in a List Node."""
        curr_node = self.head
        while curr_node != None:
            if curr_node.data == data:
                return True
            curr_node = curr_node.next
        return False

    def copy_list(self):
        """Returns a new Double Linked List with the same data in O(n)."""
        new_list = DoubleLinkedList()
        transfer = self.head

        while transfer != None:
            new_list.insert_last(transfer.data)
            transfer = transfer.next

        return new_list

    def reverse(self):
        """Takes the current list and returns it in reverse order through iterating backwards."""
        new_list = DoubleLinkedList()
        transfer = self.tail

        while transfer != None:
            new_list.insert_last(transfer.data)
            transfer = transfer.prev
        return new_list