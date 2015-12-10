import sqlite3

class Database:
	def __init__(self, db_name):
		self.db_name = db_name

	def loadDatabase(self):
		with sqlite3.connect(self.db_name) as db:
			cursor = db.cursor()

	def getAllData(self):
		with sqlite3.connect(self.db_name) as db:
		  cursor = db.cursor()
		  cursor.execute("select name from Teacher")
		  teachers = cursor.fetchall()
		  return teachers
