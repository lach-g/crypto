import sys
sys.path.append("../assignment")

import unittest
from LinkedList_dsa import ListNode, LinkedList

class TestAssetClass(unittest.TestCase):

    def test_init(self):
            ll = LinkedList()
            self.assertEqual(ll.head, None,
                        "List is empty, head must point to none.")

    def test_iteration(self):
        ll = LinkedList()
        ll.insert_first("3")
        ll.insert_first("2")
        ll.insert_first("1")

        iter_string = ""
        for i in ll:
            iter_string = iter_string + i

        self.assertEqual(iter_string, "123",
                    "Iteration must go in order from head to tail.")

    def test_is_empty(self):
        ll = LinkedList()
        self.assertEqual(ll.is_empty(), True,
                    "Nothing in list, must be empty.")

    def test_insert_first(self):
        ll = LinkedList()
        ll.insert_first(1)
        self.assertEqual(ll.head.data, 1,
                        "Was inserted first, must return what the head points to.")

    def test_insert_last(self):
        ll = LinkedList()
        ll.insert_last(1)
        self.assertEqual(ll.peek_last(), 1,
                        "Was inserted last, must return what the tail points to.")

    def test_peek_first(self):
        ll = LinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        data = ll.peek_first()
        self.assertEqual(data, 1,
                        "Peek first must return the data at the front of the list.")

    def test_peek_last(self):
        ll = LinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        data = ll.peek_last()
        self.assertEqual(data, 2,
                        "Peek first must return the data at the front of the list.")

    def test_remove_first(self):
        ll = LinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        data = ll.remove_first()
        first = ll.peek_first()
        self.assertEqual(first, 2,
        "Remove first must return the data at the front of the list and remove it from the list.")

    def test_remove_last(self):
        ll = LinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        data = ll.remove_last()
        last = ll.peek_last()
        self.assertEqual(last, 1,
        "Remove last must return the data at the back of the list and remove it from the list.")

    def test_remove_at(self):
        ll = LinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        ll.remove_at(1)
        self.assertEqual(ll.peek_last(), 1,
                "The remove at removes by index in the list.")


if __name__ == "__main__":
    unittest.main()