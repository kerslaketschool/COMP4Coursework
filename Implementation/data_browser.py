from PyQt4.QtGui import *
from PyQt4.QtSql import *

class BrowseDataWidget(QWidget):
	"""A widget for displaying Database data"""
	
	def __init__(self):
		super().__init__()
		self.layout = QVBoxLayout()
		
		self.table_view = QTableView()
		self.PopulateTableView()
		
		self.layout.addWidget(self.table_view)
		self.setLayout(self.layout)


        def PopulateTableView(self):
            teachers = g_database.GetAllTeachers()
            model = QStandardItemModel()
            row = 0
            for teacher in teachers:
              for column in range(2):
                item = QStandardItem("{}".format(teacher[column]))
                model.setItem(row, column, item)
                row+=1
        
            self._tableview.setModel(model)
		
