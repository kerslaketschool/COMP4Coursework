from PyQt4.QtGui import *

class EditDialog(QDialog):
	"""This class creates the dialog window for editing items in the database"""

	def __init__(self):
		super().__init__()
		#create widgets
		self.table_select_combo_box = QComboBox()
		self.fields = {}
		for count in range(4):
			self.fields["fieldBox{0}".format(count)] = QLineEdit("Field{0}".format(count))
		self.attributes = {}
		for count in range(4):
			self.attributes["attribute{0}".format(count)]=QLineEdit()
			self.attributes["attribute{0}".format(count)].setPlaceholderText("Enter Attribute")
		
		self.table_select_combo_box.addItem("Select Table")
		self.table_select_combo_box.addItem("Table 1")
		self.table_select_combo_box.addItem("Table 2")
		#self.attribute_line_edit.setPlaceholderText("Edit Attribute")
		
		#create layout
		self.layoutMain = QVBoxLayout()
		self.horizBoxLayouts = {}
		for count in range(4):
			self.horizBoxLayouts["BoxLayout{0}".format(count)]=QHBoxLayout()
		
		#add widgets to layout
		self.layoutMain.addWidget(self.table_select_combo_box)
		for count in range(4):
			self.horizBoxLayouts["BoxLayout{0}".format(count)].addWidget(self.fields["fieldBox{0}".format(count)])
			self.horizBoxLayouts["BoxLayout{0}".format(count)].addWidget(self.attributes["attribute{0}".format(count)])
			self.layoutMain.addLayout(self.horizBoxLayouts["BoxLayout{0}".format(count)])
			
	
		
		#set the window layout
		self.setLayout(self.layoutMain)
		
		#connections
		"""To be continued"""