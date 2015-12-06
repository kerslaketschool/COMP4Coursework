from PyQt4.QtGui import *
from PyQt4.QtSql import *
from sqlite3 import *

class BrowseDataWidget(QWidget):
	"""A widget for displaying Database data"""
	
	def __init__(self):
		super().__init__()
		self.layout = QVBoxLayout()
		
		self.table_view = QTableView()
		self.PopulateTable()
		
		self.layout.addWidget(self.table_view)
		
		self.setLayout(self.layout)

		
	def PopulateTable(self):
		model = QStandardItemModel()
		model.setItem(0, 0, QStandardItem("Gay"))
		model.setItem(0, 1, QStandardItem("Butts"))
		model.setItem(0, 2, QStandardItem("Chums"))
		model.setItem(1, 0, QStandardItem("sup"))
		model.setItem(1, 1, QStandardItem("clunge"))
		model.setItem(1, 2, QStandardItem("plunge"))
		
		self.table_view.setModel(model)
		
