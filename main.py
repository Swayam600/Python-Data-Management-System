from typing import List, Any


class Table:
	"""
	Intializes a dummy table.
	Can store columns and rows of data
	"""

	def __init__(self, columns = [], rows = []):
		self.columns = columns
		self.rows = rows

	def create_column(self, *column_names):
		self.columns = [*column_names]


	def show_columns(self):
		return self.columns

	def insert_value(self, *rows_data):
		self.rows.append([*rows_data])

	def insert_values(self, *rows_data):
		self.rows.extend([*rows_data])








