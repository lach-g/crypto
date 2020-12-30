#
# Short Pickle menu implementation to lessen the need for parsing
#

import pickle
import csv

class Pickle_Menu:
	def __init__(self, data_struct=None):
		self.data_struct = data_struct
	
	# Serializing the data structure
	def save(self, file_name):
		try:
			with open(file_name, "wb") as data_file:
				pickle.dump(self.data_struct, data_file)
				print("Successfully saved.")
		except:
			print("Error: Problem pickling object.")

	# Reading a serialized file
	def load(self, file_name):
		try:
			with open(file_name, "rb") as data_file:
				read_obj = pickle.load(data_file)
				return read_obj
		except:
			print("Error: Object file may not exist.")

	