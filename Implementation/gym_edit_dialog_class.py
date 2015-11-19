from PyQt4.QtGui import *

class EditDialog(QDialog):
	"""This class creates the dialog window for editing items in the database"""

	def __init__(self):
		super().__init__()
		#create widgets
		self.table_select_combo_box = QComboBox()
		self.field_box1 = QLineEdit("Field 1")
		self.field_box2 = QLineEdit("Field 2")
		self.field_box3 = QLineEdit("Field 3")
		self.attributes = {}
		for count in range(3):
			self.attributes["attribute{0}".format(count)]=QLineEdit()
		
		self.table_select_combo_box.addItem("Select Table")
		self.table_select_combo_box.addItem("Table 1")
		self.table_select_combo_box.addItem("Table 2")
		self.field_box1.setReadOnly(True)
		self.field_box2.setReadOnly(True) 
		self.field_box3.setReadOnly(True) 
		#self.attribute_line_edit.setPlaceholderText("Edit Attribute")
		
		#create layout
		self.layout = QVBoxLayout()
		
		#add widgets to layout
		self.layout.addWidget(self.table_select_combo_box)
		self.layout.addWidget(self.field_box1)
		self.layout.addWidget(self.field_box2)
		self.layout.addWidget(self.field_box3)
		for count in range(3):
			self.layout.addWidget(self.attributes["Attribute{0}"].format(count))
		
		#set the window layout
		self.setLayout(self.layout)
		
		#connections
		"""To be continued"""