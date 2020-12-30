#
# Hash table implementation
#

import numpy as np
import math
from LinkedList_dsa import LinkedList, ListNode

class HashTable:

	# Max filling of the array is 60 percent
	# Min filling of the array is 20 percent
	# Takes the size of data to fit and transforms to larger array
	# decreasing clashes
	def __init__(self, table_size):
		self.MAX_LOAD_FACTOR = 0.6
		self.MIN_LOAD_FACTOR = 0.2
		self.count = 0

		self.actual_size = self.__next_prime(table_size)
		self.hash_array = np.zeros(self.actual_size, dtype=object)

		self.__array_indices_to_lists(self.hash_array, self.actual_size)

	# Initialises a Linked List at each array index
	def __array_indices_to_lists(self, linked_list, size):
		for i in range(size):
			linked_list[i] = LinkedList()

	# Returns the hash value from the key
	def __hashing(self, key):
		hash_index = 2166136261
		key_len = len(str(key))
		for i in range(key_len):
			str_key = str(key)
			# hash_index = (hash_index * 16777619) ^ int(str_key[i]) is for numerical keys
			hash_index = (hash_index * 16777619) ^ ord(str_key[i])
		return hash_index % self.actual_size

	# Calls larger or smaller resize dependant on current array fullness
	def __check_resize(self):
		if self.__outside_upper_bound():
			self.__larger_table()
		if self.__outside_lower_bound():
			self.__smaller_table()

	# Returns true if array fullness goes over the maximum set globally
	def __outside_upper_bound(self):
		if self.__check_load() > self.MAX_LOAD_FACTOR:
			return True
		else:
			return False

	# Returns true if array fullness goes over the minimum set globally
	def __outside_lower_bound(self):
		if self.__check_load() < self.MIN_LOAD_FACTOR:
			return True
		else:
			return False

	# Returns current fullness of the array
	def __check_load(self):
		return self.count / self.actual_size

	# Overwrites the table to a larger size
	def __larger_table(self):
		curr_length = self.actual_size
		new_size = 2 * self.actual_size
		self.actual_size = self.__next_prime(new_size)
		new_table = np.zeros(self.actual_size, dtype=object)

		self.__array_indices_to_lists(new_table, self.actual_size)

		old_hash_array = self.hash_array
		self.hash_array = new_table
		for i in range(curr_length):
			if old_hash_array[i] != None:
				hash_list = old_hash_array[i]
				for entry in hash_list:
					self.__insert(entry.key, entry.value)

	# Overwrites the table to a smaller size
	def __smaller_table(self):
		curr_length = self.actual_size
		new_size = self.actual_size / 2
		self.actual_size = self.__next_prime(int(new_size))
		new_table = np.zeros(self.actual_size, dtype=object)

		self.__array_indices_to_lists(new_table, self.actual_size)

		old_hash_array = self.hash_array
		self.hash_array = new_table
		for i in range(curr_length):
			if old_hash_array[i] != None:
				hash_list = old_hash_array[i]
				for entry in hash_list:
					self.__insert(entry.key, entry.value)

	# No count addition or check resize specifically for the table resizing
	def __insert(self, key, value):
		hashed = self.__hashing(key)
		bucket = self.hash_array[hashed]
		bucket.insert_last(HashEntry(key, value, hashed))

	# Given a key in the hash table it returns the corresponding value
	def retrieve(self, key):
		hash_node = self.__find(key)
		return hash_node.value

	# Adds a value with a corresponding key to the hash array in
	# the indexed linked list
	def insert(self, key, value):
		self.count += 1
		self.__check_resize()
		hashed = self.__hashing(key)
		bucket = self.hash_array[hashed]
		bucket.insert_last(HashEntry(key, value, hashed))

	# Returns the closest larger prime number to the given value
	def __next_prime(self, start_val):
		if start_val % 2 == 0:
			prime_val = start_val - 1
		else:
			prime_val = start_val

		is_prime = False
		while not is_prime:
			prime_val += 2
			i = 3
			is_prime = True
			root_val = math.sqrt(prime_val)
			while i <= root_val and is_prime:
				if prime_val % i == 0:
					is_prime = False
				else:
					i += 2
		
		return prime_val

	# Goes to array index based off hashed key 
	# and loops through returning a match if key found
	def __find(self, key):
		hash_node = None
		index = self.__hashing(key)
		linked_list = self.hash_array[index]
		for i in linked_list:
			if i.key == key:
				hash_node = i
				break
		if hash_node == None:
			raise ValueError("Key not in hash table.")
		return hash_node

	# Returns the hash node and removes it from hash table
	def remove(self, key):
		if self.count == 0:
			raise ValueError("Hash table is empty.")
		else:
			self.__check_resize()
			hash_node = self.__find(key)
			hash_index = hash_node.hash
			linked_list = self.hash_array[hash_index]
			list_index = self.__ll_index(key, hash_index)
			linked_list.remove_at(list_index)
			self.count -= 1
			return hash_node
	
	# Returns the index of the hash node in the Linked List at the hash array index
	def __ll_index(self, key, hash_table_index):
		hash_node = None
		linked_list = self.hash_array[hash_table_index]
		index = 0
		for i in linked_list:
			if i.key == key:
				hash_node = i
				return index
			index += 1
		if hash_node == None:
			raise ValueError("Key not in hash table.")


class HashEntry:
	# Container for key, value linked to key, and hash value
	def __init__(self, key=None, value=None, hash=None):
		self.key = key
		self.value = value
		self.hash = hash













if __name__ == "__main__":
	
	students = HashTable(20)
	print("First insert:")
	students.insert(90021176, "Lachlan Greenland")
	print("\nSecond insert:")
	students.insert(90035586, "Mike Constantine")
	print("\nThird insert:")
	students.insert(90024257, "Cameron McIntosh")
	print("\nFourth insert:")
	students.insert(79348, "Matt Metics")
	print("\nFifth insert:")
	students.insert(989698, "Harry Potter")


	print("\n")
	name = students.retrieve(90021176)
	print(name)
