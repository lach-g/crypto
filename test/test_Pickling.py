import sys
sys.path.append("../assignment")

import unittest
import os
from Pickling import Pickle_Menu
from LinkedList_dsa import ListNode, LinkedList

class TestAssetClass(unittest.TestCase):

    def test_init(self):
        ll = LinkedList()
        ll.insert_first(1)
        p = Pickle_Menu(ll)
        self.assertEqual(p.data_struct.peek_first(), 1,
                "The object should take in a data struct in a variable.")

    def test_save(self):
        opened = False
        ll = LinkedList()
        ll.insert_first(1)
        p = Pickle_Menu(ll)
        p.save("test_sav.obj")
        base_path = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(base_path, "..", "test_sav.obj"))
        try:
            with open(file_path, "r") as f:
                opened = True
                os.remove(file_path)
        except Exception as e:
            print(e)
        self.assertTrue(opened,
                "Pickle saving should save a file to the directory.")

    def test_load(self):
        loaded = False
        ll = LinkedList()
        ll.insert_first(1)
        p = Pickle_Menu(ll)
        p.save("test_sav.obj")
        base_path = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(base_path, "..", "test_sav.obj"))
        try:
            struct = p.load(file_path)
            loaded = True
            os.remove(file_path)
        except Exception as e:
            print(e)

            
if __name__ == "__main__":
    unittest.main()