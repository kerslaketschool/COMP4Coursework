from PyQt4.QtGui import *

class DeleteDialog(QDialog):
	"""This class creates the dialog window for deleting items from the database"""

	def __init__(self):
		super().__init__()

		#create widgets
		self.table_select_combo_box = QComboBox()
		self.item_select_combo_box = QComboBox()
		self.delete_push_button = QPushButton("Delete")
		self.delete_all_push_button = QPushButton("Delete All Items")

		self.table_select_combo_box.addItem("Select Table")
		self.table_select_combo_box.addItem("Table 1")
		self.table_select_combo_box.addItem("Table 2")
		self.table_select_combo_box.addItem("Table 3")

		self.item_select_combo_box.addItem("Select Item")
		self.item_select_combo_box.addItem("Item 1")
		self.item_select_combo_box.addItem("Item 2")
		self.item_select_combo_box.addItem("Item 3")

		#create layout
		self.layout = QVBoxLayout()

		#add widgets to layout
		self.layout.addWidget(self.table_select_combo_box)
		self.layout.addWidget(self.item_select_combo_box)
		self.layout.addWidget(self.delete_push_button)
		self.layout.addWidget(self.delete_all_push_button)

		#set the window layout
		self.setLayout(self.layout)
		self.setWindowTitle("Delete")
		self.setWindowIcon(QIcon("Hugobells.png"))

		#connections
		"""To Be Continued"""
