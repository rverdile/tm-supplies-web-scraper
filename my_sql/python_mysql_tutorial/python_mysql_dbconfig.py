from configparser import ConfigParser

def read_db_config(filename='config.ini', section='mysql'):
	"""
	Reads database from configuration file and returns a dictionary object

	A configuration file is .ini file. See README for example.

	:param filename: name of the configuration file.
	:param section: section of database configuration
	:return: a dictionary of database parameters
	"""

	# create parser and read ini configuration file
	parser = ConfigParser()
	parser.read(filename)

	#get section, default to mysql

	db = {}

	if parser.has_section(section):

		items = parser.items(section)
		for item in items:
			db[item[0]] = item[1]

	else:
		raise Exception('{0} not found in the {1} file'.format(section,filename))

	return db

