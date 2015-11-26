from PyQt4.QtGui import *

class AboutDialog(QDialog):
	"""This is the about page"""

	def __init__(self):
		super().__init__()

		#create widgets
		self.pixmap = QPixmap("toby+dave")
		self.bigD = QLabel(self)
		self.bigD.setPixmap(self.pixmap)#change this variable name
		self.text1 = QLineEdit("Created by Sir Tobias Kerslake the Third")
		self.text2 = QLineEdit("In Loving Memory of Hayley Westenra even though she isn't dead")
		self.text1.setReadOnly(True)
		self.text2.setReadOnly(True)
		
		#create layout
		self.layout = QVBoxLayout()


		#add widgets to layout
		self.layout.addWidget(self.bigD)
		self.layout.addWidget(self.text1)
		self.layout.addWidget(self.text2)


		#set the window layout
		self.setLayout(self.layout)
		self.setWindowTitle("About")
		self.setWindowIcon(QIcon("Hugobells.png"))

		#connections
		"""Maybe Later"""
