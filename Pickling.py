import pickle
import csv
import sys

class Pickle_Menu:
	def __init__(self, data_struct=None):
		"""Optional data structure to intake upon object creation."""
		self.data_struct = data_struct
	
	def save(self, file_name):
		"""Serializing the data structure"""
		sys.setrecursionlimit(20000)
		try:
			with open(file_name, "wb") as data_file:
				pickle.dump(self.data_struct, data_file)
		except Exception as e:
			print("Error: Problem pickling object: ", e)

	def load(self, file_name):
		"""Reading a serialized file"""
		try:
			with open(file_name, "rb") as data_file:
				read_obj = pickle.load(data_file)
				return read_obj
		except:
			print("Error: Object file may not exist.")

	