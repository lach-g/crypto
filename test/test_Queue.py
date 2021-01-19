import sys
sys.path.append("../assignment")

import unittest
from Queue_dll_dsa import Queue

class TestAssetClass(unittest.TestCase):

    def test_init(self):
        q = Queue()
        self.assertEqual(q.queue.head, None,
                    "Queue is a wrapper for a linked list with head.")

    def test_iteration(self):
        q = Queue()
        q.enqueue("1")
        q.enqueue("2")
        q_str = ""
        for i in q:
            q_str = q_str + i

        self.assertEqual(q_str, "12",
                    "Iteration through queue from front to back.")

    def test_enqueue(self):
        q = Queue()
        q.enqueue("1")
        q.enqueue("2")
        self.assertEqual(q.queue.head.data, "1",
                    "The inner head must point at the front.")

    def test_dequeue(self):
        q = Queue()
        q.enqueue("1")
        q.enqueue("2")
        data = q.dequeue()
        self.assertEqual(data, "1",
                    "Dequeue returns the front of the queue.")

    def test_peek(self):
        q = Queue()
        q.enqueue("1")
        q.enqueue("2")
        self.assertEqual(q.peek(), "1",
                    "Peek must return, but not delete the front of queue's data.")
    
    def test_has(self):
        q = Queue()
        q.enqueue("1")
        q.enqueue("2")
        self.assertTrue(q.has("1"),
                    "The queue must contain the enqueued data returning True.")

    def test_count(self):
        q = Queue()
        q.enqueue("1")
        q.enqueue("2")
        q.dequeue()
        self.assertEqual(q.count(), 1, 
                "Queue must track all enqueues and dequeues for an accurate count.")


if __name__ == "__main__":
    unittest.main()