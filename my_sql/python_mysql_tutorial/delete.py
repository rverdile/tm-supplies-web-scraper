from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def delete_book(book_id):
	db_config = read_db_config()

	query = "DELETE FROM books WHERE id = %s"

	try:
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query,(book_id,))

		conn.commit()

	except Error as e:
		print(e)

	finally:
		cursor.close()
		conn.close()

if __name__ == '__main__':
	delete_book(87)