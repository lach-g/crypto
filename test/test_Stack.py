import sys
sys.path.append("../assignment")

import unittest
from Stack_dll_dsa import Stack

class TestAssetClass(unittest.TestCase):

    def test_init(self):
        s = Stack()
        self.assertEqual(s.stack.head, None,
                    "Initial stack is an empty linked list.")

    def test_iteration(self):
        s = Stack()
        s.push("1")
        s.push("2")
        s_str = ""
        for i in s:
            s_str = s_str + i
        self.assertEqual(s_str, "21",
                        "The stack adds to top and should return this first.")

    def test_push(self):
        s = Stack()
        s.push("1")
        s.push("2")
        self.assertEqual(s.stack.head.data, "2",
                        "Head of the hidden list points to the top of the stack.")

    def test_pull(self):
        s = Stack()
        s.push("1")
        s.push("2")
        data = s.pull()
        self.assertEqual(data, "2",
                    "Pull returns the top of the stack and deletes it from the stack.")

    def test_top(self):
        s = Stack()
        s.push("1")
        s.push("2")
        data = s.top()
        self.assertEqual(data, "2",
                    "Top returns the top of the stack, but leaving it on top.")

if __name__ == "__main__":
    unittest.main()