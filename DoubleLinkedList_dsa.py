
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def get_next(self):
        return self.data

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __iter__(self):
        self.curr = self.head
        return self

    def __next__(self):
        curr_val = None
        if self.curr == None:
            raise StopIteration
        else:
            curr_val = self.curr.data
            self.curr = self.curr.next
        return curr_val

    def __str__(self):
        db_ll = " <-> "
        curr_node = self.head
        if self.is_empty():
            return "Linked List is empty"
        else:
            while curr_node.next != None:
                db_ll += str(curr_node.data) + " <-> "
                curr_node = curr_node.next
            return "head " + db_ll + str(curr_node.data) + " <-> tail"

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def insert_first(self, data):
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
        if self.is_empty():
            return None
        else:
            first_node = self.head
            return first_node.data

    def peek_last(self):
        if self.is_empty():
            raise ValueError("Double Linked List is empty")
        else:
            last_node = self.tail
            return last_node.data

    def remove_first(self):
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
        curr_node = self.head
        while curr_node != None:
            if curr_node.data == data:
                return True
            curr_node = curr_node.next
        return False
        







if __name__ == "__main__":
    ll = DoubleLinkedList()
    ll.insert_first(5)
    ll.insert_last(10)
    ll.insert_last(40)
    ll.insert_last(70)
    print("Should be 5: ", ll.peek_first())
    print("Should be 70: ", ll.peek_last())
    print("Printing whole list:")
    print(ll)
    print()
    print("Remove last should be 70: ", ll.remove_last())
    print("Remove first should be 5: ", ll.remove_first())
    print("After removed and last: ", ll)
    print()
    print("Using for loop:")
    for value in ll:
        print(value)