from typing import List

from date_regex import is_date

"""
Data-types (BETA)
	- STRING
	- INT
	- FLOAT
	- DATE
"""

class Table:
	"""
	Initializes a dummy table.
	Now includes type system(BETA)
	"""

	def __init__(self, columns = {}, rows = []):
		self.columns = columns
		self.rows = rows

	def create_columns(self, **name_type):
		 self.columns = {
			 key: type_
			 for (key, type_) in name_type.items()
		 }

	def _check_len(self, data_list):
		if len(self.columns) == len(data_list):
			return True

		return False

	def _check_type(self, data, type_):
		result = False

		if type_ == 'STRING' and type(data) == str:
			result = True
		elif type_ == 'INT' and type(data) == int:
			result = True
		elif type_ == 'FLOAT' and type(data) == float:
			result = True
		elif type_ == 'DATE' and is_date(data):
			result = True
		else:
			result = False

		return result

	def _check_types(self, *data):
		types_ = [ self.columns[field] for field in self.columns]
		datas_ = [*data]

		try:


			for data in datas_:
				for i in range(len(types_)):
					if not self._check_type(data[i], types_[i]):
						return False

			return True

		except IndexError:
			raise Exception('PLease provide all the mentioned data set')


	def insert_value(self, *data):
		no_of_data_field = self._check_len([*data])
		valid_types = self._check_types([*data])

		if no_of_data_field and valid_types:
			self.rows.append([*data])
		else:
			if no_of_data_field:
				raise Exception('Please check the data type and fill in the data')
			elif valid_types:
				raise Exception('Please provide all the mentioned data-set')
			else:
				raise Exception('Please check data types and fill in the data')	

	
	def insert_values(self, *data_list):
		for data in [*data_list]:
			try:
				self.insert_value(*data)
			except:
				raise Exception("Please provide all the mentioned data-set")

names = Table()

names.create_columns(
	id = 'INT',
	name = 'STRING',
	date = 'DATE'
)

names.insert_values(
	[1, 'Sam', '1990-09-25'],
	[2, 'Steve', '1905-11-09']
)