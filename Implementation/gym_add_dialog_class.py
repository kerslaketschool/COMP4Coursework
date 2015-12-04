from PyQt4.QtGui import *

class AddDialog(QDialog):
	"""This class creates the dialog window for Adding items to the database"""

	def __init__(self,num):
		super().__init__()
		
		#create widgets
		self.table_select_combo_box = QComboBox()
		self.fields = {}
		self.num = num
		for count in range(num):
			self.fields["fieldBox{0}".format(count)] = QLabel("Field{0}".format(count))
		self.attributes = {}
		for count in range(num):
			self.attributes["attribute{0}".format(count)]=QLineEdit()
			self.attributes["attribute{0}".format(count)].setPlaceholderText("Enter Attribute")
		self.confirmButton = QPushButton("Add")
		
		self.table_select_combo_box.addItem("Select Table")
		self.table_select_combo_box.addItem("Table 1")
		self.table_select_combo_box.addItem("Table 2")
		
		#create layout
		self.layoutMain = QHBoxLayout()
		self.vertLayout1 = QVBoxLayout()
		self.vertLayout2 = QVBoxLayout()
		self.finalLayout = QVBoxLayout()
		
		#set the window layout
		for count in range(num):
			self.vertLayout1.addWidget(self.fields["fieldBox{0}".format(count)])
			self.vertLayout2.addWidget(self.attributes["attribute{0}".format(count)])
			
		self.layoutMain.addLayout(self.vertLayout1)
		self.layoutMain.addLayout(self.vertLayout2)
		self.finalLayout.addLayout(self.layoutMain)
		self.finalLayout.addWidget(self.confirmButton)
			
	
		#set the window layout
		self.setLayout(self.finalLayout)
		self.setWindowTitle("Add")
		self.setWindowIcon(QIcon("Hugobells.png"))
		
		#connections
		"""To be continued"""

        
