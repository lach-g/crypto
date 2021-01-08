#
# Used to deal with collisions in the HashTable class
#


class ListNode():
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:

    def __init__(self):
        self.head = None
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
        new_node = ListNode(data)

        if self.is_empty():
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.count += 1

    def insert_last(self, data):
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
        if self.head == None:
            return True
        else:
            return False

    def peek_first(self):
        if self.is_empty():
            raise ValueError("Linked List is empty")
        else:
            first_node = self.head
            return first_node.get_data()

    def peek_last(self):
        if self.is_empty():
            raise ValueError("Linked List is empty")
        else:
            curr_node = self.head
            while curr_node.get_next() != None:
                curr_node = curr_node.get_next()
            return curr_node.get_data()

    def remove_first(self):
        if self.is_empty():
            raise ValueError("Linked List is empty")
        else:
            first_node = self.head
            self.head = first_node.get_next()
            self.count -= 1
            return first_node.get_data()

    def remove_last(self):
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
        if index == 0:
            self.remove_first()
        else:
            count = 0
            curr_node = self.head
            while curr_node.get_next() != None:
                if count == index:
                    prev_node.set_next(curr_node.next)
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
