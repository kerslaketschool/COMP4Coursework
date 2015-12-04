from PyQt4.QtGui import *
from PyQt4.QtSql import *

class BrowseDataWidget(QWidget):
	"""A widget for displaying Database data"""
	
	def __init__(self):
		super().__init__()
		self.layout = QVBoxLayout()
		
		self.table_view = QTableView()
		
		self.layout.addWidget(self.table_view)
		self.setLayout(self.layout)
		
		