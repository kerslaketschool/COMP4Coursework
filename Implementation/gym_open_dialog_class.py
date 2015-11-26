from PyQt4.QtGui import *

class OpenDialog(QDialog):
	"""This class creates the dialog window for opening files"""

	def __init__(self):
		super().__init__()

		#create widgets
		self.open_push_button = QPushButton("Open")
		self.close_push_button = QPushButton("Close")

		#create layout
		self.layout = QVBoxLayout()

		#add widgets to layout
		self.layout.addWidget(self.open_push_button)
		self.layout.addWidget(self.close_push_button)

		#set the window layout
		self.setLayout(self.layout)
		self.setWindowTitle("Open")
		self.setWindowIcon(QIcon("Hugobells.png"))

		#connections
		self.open_push_button.clicked.connect(self.open_file)
		self.close_push_button.clicked.connect(self.close)
	
	def open_file(self):
		path = QFileDialog.getOpenFileName(caption="Open Database",filter = "Database file (*.db *.dat)")
		

		
