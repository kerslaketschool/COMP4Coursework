from PyQt4.QtGui import *
from gym_add_dialog_class import *

class EditDialog(AddDialog):
	"""This class creates the dialog window for editing items in the database"""

	def __init__(self,num):
		super().__init__(num)
		
		self.confirmButton.setText("Edit")
		self.setWindowTitle("Edit")
		
		