from DoubleLinkedList_dsa import ListNode, DoubleLinkedList

class Queue:
    def __init__(self):
        self.queue = DoubleLinkedList()

    def __str__(self):
        return self.queue.__str__()

    def __iter__(self):
        curr_node = self.queue.head
        while curr_node != None:
            yield curr_node.data
            curr_node = curr_node.next

    def enqueue(self, obj):
        self.queue.insert_last(obj)

    def dequeue(self):
        return self.queue.remove_first()

    def peek(self):
        return self.queue.peek_first()

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print("Testing iterator (Should be 1, 2, 3, 4: ")
    for i in q:
        print(i)

    print("Peek should be 1: ", q.peek())
    print("Dequeue should be 1: ", q.dequeue())
    print("After dequeue using linked list __str__:", q)
