from PyQt4.QtGui import *

class PrintDialog(QDialog):
	"""This class creatres the dialog window for creating forms and printing them"""

	def __init__(self):
		super().__init__()

		#create widgets
		self.form_combo_box = QComboBox()
		self.table_combo_box = QComboBox()
		self.item_combo_box = QComboBox()
		self.print_push_button = QPushButton("Print")

		self.form_combo_box.addItem("Select Form")
		self.form_combo_box.addItem("Invoice")
		self.form_combo_box.addItem("Member Details")
		self.item_combo_box.addItem("Select Item")
		self.item_combo_box.addItem("Item1")
		self.item_combo_box.addItem("Item2")
		self.table_combo_box.addItem("Select Table")
		self.table_combo_box.addItem("Members")
		self.table_combo_box.addItem("Payment")

		#create layout
		self.layout = QVBoxLayout()

		#add widgets to layout
		self.layout.addWidget(self.form_combo_box)
		self.layout.addWidget(self.table_combo_box)
		self.layout.addWidget(self.item_combo_box)
		self.layout.addWidget(self.print_push_button)

		#set the window layout
		self.setLayout(self.layout)
		self.setWindowTitle("Print")
		self.setWindowIcon(QIcon("Hugobells.png"))

		#connections
		"""Add Print Button Functionality"""
