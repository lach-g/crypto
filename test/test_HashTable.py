import sys
sys.path.append("../assignment")

import unittest
from HashTable_dsa import HashEntry, HashTable

class TestAssetClass(unittest.TestCase):

	def initialise(self):
		students = HashTable(3)
		students.insert(90021176, "Lachlan Greenland")
		students.insert(90035586, "Mike Constantine")
		students.insert(90024257, "Cameron McIntosh")
		return students

	def test_init(self):
		test_table = self.initialise()
		self.assertTrue(test_table)

	def test_same_hashing(self):
		students = HashTable(3)
		hash1 = students._HashTable__hashing(90021176)
		hash2 = students._HashTable__hashing(90021176)
		self.assertEqual(hash1, hash2,
					"Hashing function should return same value for same key each time.")

	def test_resize_table(self):
		test_table = self.initialise()
		length = test_table.actual_size
		test_table.insert(786787, "Steve Madden")
		new_length = test_table.actual_size
		self.assertGreater(new_length, length,
		"Resize should recognize table was over 60 percent full.")

	def test_retrieve(self):
		test_table = self.initialise()
		name = test_table.retrieve(90021176)
		self.assertEqual(name, "Lachlan Greenland",
		"ID should return correct value.")

	def test_insert(self):
		test_table = self.initialise()
		test_table.insert(91879813, "Gary Ablett")
		name = test_table.retrieve(91879813)
		self.assertEqual(name, "Gary Ablett",
		"Insert should save correct value and be retrieve by key.")

	def test_next_prime(self):
		test_table = self.initialise()
		prime = test_table._HashTable__next_prime(3)
		self.assertEqual(prime, 5,
		"Next prime returns the closest higher prime number.")

	def test_find(self):
		test_table = self.initialise()
		node = test_table._HashTable__find(90021176)
		hash_index = test_table._HashTable__hashing(90021176)
		self.assertEqual(node.hash, hash_index,
		"_Find function must return the corresponding node to the key")

	def test_ll_index(self):
		test_table = self.initialise()
		hash_index = test_table._HashTable__hashing(90021176)
		ll_index = test_table._HashTable__ll_index(90021176, hash_index)
		self.assertEqual(ll_index, 0,
		"Hash should not yet have to deal with collisions")
		
	def test_remove(self):
		test_table = self.initialise()
		name = test_table.remove(90024257)
		self.assertEqual(name.value, "Cameron McIntosh",
		"Remove returns the hash node corresponding to the key.")

if __name__ == "__main__":
	unittest.main()