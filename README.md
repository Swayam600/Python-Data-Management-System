# PyDB

## Why PyDB
**PyDB** is a very flexible Data Management System, completely written in **Python**

**PyDb** helps you write clear code to create horizontal scalable database which scales infinitely.

## Features

**PyDbB** allows us to do following things
- Create Tables
- Add Columns
- Insert Data to the table
- Data types (BETA)
	- INT
	- STRING
	- FLOAT
	- DATE
## Syntax

### Creating Tables

```python

student_table = Table()

student_table.create_columns(
	id = 'INT',
	first_name = 'STRING',
	last_name = 'STRING',
	date_joined = 'DATE'
)
```

### Adding data to the table

```python
student_table.insert_value(1, 'Sam', 'Dane', '2015-11-12')

student_table.insert_values(
	[2, 'Steve', 'Clinton', '2011-01-12'],
	[3, 'Jimmy', 'De Santa', '2000-09-09'],
	[4, 'Maria', 'Cameron', '2019-01-23']
)
```
