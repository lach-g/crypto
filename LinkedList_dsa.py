
class ListNode():
    def __init__(self, data):
        """Creates List Node object containing the value and link to the
            next node."""
        self.data = data
        self.next = None

    def get_data(self):
        """Returns whatever is stored in the data variable."""
        return self.data
    
    def set_data(self, new_data):
        """Replaces the data variable with new data."""
        self.data = new_data

    def get_next(self):
        """Returns the next vertex in the list."""
        return self.next

    def set_next(self, new_next):
        """Sets the next vertex of the List Node."""
        self.next = new_next


class LinkedList:

    def __init__(self):
        """Creates a Single Linked List Object that chains List Nodes together
        starting at the head unidirectionally."""
        self.head = None
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
        ll_str = "head -> "
        if self.is_empty():
            return ll_str + "None"
        else:
            curr_node = self.head
            while curr_node.get_next() != None:
                ll_str += str(curr_node.get_data()) + " -> "
                curr_node = curr_node.get_next()
            ll_str += str(curr_node.get_data()) + " -> None"
            return ll_str

    def insert_first(self, data):
        """Points the head of the list to the new list node
            and connects the previous first node as second."""
        new_node = ListNode(data)

        if self.is_empty():
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.count += 1

    def insert_last(self, data):
        """Iterates through and sets the last list node to point to
            the new list node in O(1) operation."""
        new_node = ListNode(data)

        if self.is_empty():
            self.head = new_node

        else:
            curr_node = self.head
            while curr_node.get_next() != None:
                curr_node = curr_node.get_next()
            curr_node.set_next(new_node)

        self.count += 1

    def is_empty(self):
        """Returns a bool true if the head of the list is empty."""
        if self.head == None:
            return True
        else:
            return False

    def peek_first(self):
        """O(1) operation as head always points to the first node; returns the Node data."""
        if self.is_empty():
            raise ValueError("Linked List is empty")
        else:
            first_node = self.head
            return first_node.get_data()

    def peek_last(self):
        """O(n) operation to iterate to the end of the list and return the
            data contained in the list node."""
        if self.is_empty():
            raise ValueError("Linked List is empty")
        else:
            curr_node = self.head
            while curr_node.get_next() != None:
                curr_node = curr_node.get_next()
            return curr_node.get_data()

    def remove_first(self):
        """Returns the head of the List in O(1) and replaces it by redirecting the
            head to point to the second node."""
        if self.is_empty():
            raise ValueError("Linked List is empty")
        else:
            first_node = self.head
            self.head = first_node.get_next()
            self.count -= 1
            return first_node.get_data()

    def remove_last(self):
        """Returns the last node in O(n) replacing by skipping over it from the
            node pointing to it."""
        if self.is_empty():
            raise ValueError("Linked List is empty")
        elif self.head.get_next() == None:
            last_node = self.head
            self.head = None
            self.count -= 1
            return last_node.get()
        else:
            prev_node = None
            curr_node = self.head
            while curr_node.get_next() != None:
                prev_node = curr_node
                curr_node = curr_node.get_next()
            prev_node.set_next(None)
            self.count -= 1
            return curr_node.get_data()

    def remove_at(self, index):
        """Used in the Hash Table to remove a specific vertex."""
        if index == 0:
            self.remove_first()
        else:
            count = 0
            curr_node = self.head
            while curr_node.get_next() != None:
                prev_node = curr_node
                curr_node = curr_node.get_next()
                count += 1
                if count == index:
                    prev_node.set_next(curr_node.next)



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_first(5)
    ll.insert_last(10)
    ll.insert_first(4)
    ll.insert_last(13)


        
    for i in ll:
        print(i)
    print("testing remove at function:")
    print("FIRST")
    ll.remove_at(0)
    for i in ll:
        print(i)
    print("SECOND")
    ll.remove_at(1)
    for i in ll:
        print(i)
    print("THIRD")
    ll.remove_at(0)
    for i in ll:
        print(i)
    ll.remove_at(0)
    print(ll.is_empty())
