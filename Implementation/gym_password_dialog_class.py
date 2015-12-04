from PyQt4.QtGui import *

class PasswordDialog(QDialog):
	"""This class creates a dialog box for a password"""

	def __init__(self):
		super().__init__()

		#create widgets
		self.password_lineEdit = QLineEdit()
		self.password_lineEdit.setPlaceholderText("Password")
		self.enterButton = QPushButton("Enter Password")

		#create and set layout
		self.layoutMain = QVBoxLayout()
		self.layoutMain.addWidget(self.password_lineEdit)
		self.layoutMain.addWidget(self.enterButton)
		self.setLayout(self.layoutMain)
		self.setWindowTitle("Password")
		self.setWindowIcon(QIcon("Hugobells.png"))

		#connections
		self.enterButton.clicked.connect(self.close)
	
	def close_funk(self):
		return self.password_lineEdit.text()
		
