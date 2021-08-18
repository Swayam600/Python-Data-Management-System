import re


def is_date(date):
	date_pattern = re.compile('\d{4}-\d{2}-\d{2}')
	match = re.match(date_pattern, date)

	return True if match is not None else False
	
