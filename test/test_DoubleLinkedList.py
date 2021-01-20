import sys
sys.path.append("../assignment")

import unittest
from DoubleLinkedList_dsa import DoubleLinkedList, ListNode

class TestAssetClass(unittest.TestCase):

    def test_init(self):
        ll = DoubleLinkedList()
        self.assertEqual(ll.head, None,
                    "List is empty, head must point to none.")

    def test_iteration(self):
        ll = DoubleLinkedList()
        ll.insert_last("3")
        ll.insert_last("2")
        ll.insert_last("1")

        iter_string = ""
        for i in ll:
            iter_string = iter_string + i

        self.assertEqual(iter_string, "321",
                    "Iteration must go in order from head to tail.")

    def test_is_empty(self):
        ll = DoubleLinkedList()
        self.assertEqual(ll.is_empty(), True,
                    "Nothing in list, must be empty.")

    def test_insert_first(self):
        ll = DoubleLinkedList()
        ll.insert_first(1)
        self.assertEqual(ll.head.data, 1,
                        "Was inserted first, must return what the head points to.")

    def test_insert_last(self):
        ll = DoubleLinkedList()
        ll.insert_last(1)
        self.assertEqual(ll.tail.data, 1,
                        "Was inserted last, must return what the tail points to.")

    def test_peek_first(self):
        ll = DoubleLinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        data = ll.peek_first()
        self.assertEqual(data, 1,
                        "Peek first must return the data at the front of the list.")

    def test_peek_last(self):
        ll = DoubleLinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        data = ll.peek_last()
        self.assertEqual(data, 2,
                        "Peek first must return the data at the front of the list.")

    def test_remove_first(self):
        ll = DoubleLinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        data = ll.remove_first()
        first = ll.peek_first()
        self.assertEqual(first, 2,
        "Remove first must return the data at the front of the list and remove it from the list.")

    def test_remove_last(self):
        ll = DoubleLinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        data = ll.remove_last()
        last = ll.peek_last()
        self.assertEqual(last, 1,
        "Remove last must return the data at the back of the list and remove it from the list.")

    def test_has(self):
        ll = DoubleLinkedList()
        ll.insert_last(1)
        ll.insert_last(2)
        self.assertEqual(ll.has(1), True,
                    "Has must return True if when the list contains the given data.")

    def test_copy_list(self):
        ll = DoubleLinkedList()
        ll.insert_last("1")
        ll.insert_last("2")
        copy_ll = ll.copy_list()

        ll_str = ""
        copy_str = ""
        for i in ll:
            ll_str = ll_str + i
        for i in copy_ll:
            copy_str = copy_str + i

        self.assertEqual(ll_str, copy_str,
                "The copy must return an exact match of every data point in the list.")

    def test_reverse(self):
        ll = DoubleLinkedList()
        ll.insert_last("1")
        ll.insert_last("2")
        rev_ll = ll.reverse()
        rev_str = ""
        for i in rev_ll:
            rev_str = rev_str + i

        self.assertEqual(rev_str, "21",
                "The copy must return an exact match of every data point in the list.")



if __name__ == "__main__":
    unittest.main()