from PyQt4.QtGui import *
from PyQt4.QtSql import *
from sqlite3 import *

from gym_database_class import *

class BrowseDataWidget(QWidget):
	"""A widget for displaying Database data"""
	
	def __init__(self):
		super().__init__()
		self.layout = QVBoxLayout()
		
		self.table_view = QTableView()
		self.PopulateTable()
		
		self.layout.addWidget(self.table_view)
		
		self.setLayout(self.layout)

		self.database = None 
		self.PopulateTable()

		
	def PopulateTable(self):
				self.database = Database("Teacher Database.db")
				self.database.loadDatabase()
				data = self.database.getAllData()
				model = QStandardItemModel()
				row = 0
				for item in data:
						for column in range(1):
								item = QStandardItem("{}".format(data[column]))
								model.setItem(row, column, item)
								row += 1
				self.table_view.setModel(model)








