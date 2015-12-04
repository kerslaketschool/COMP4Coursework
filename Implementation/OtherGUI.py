from PyQt4.QtCore import *
from PyQt4.QtGui import *

from DatabaseForGUI import *

class OtherGUI(QMainWindow):
  def __init__(self, parent):
    super().__init__(parent)
    
    self._parent = parent
    self.setWindowTitle("This is my other window")

    # Create label and line edit
    self._name_label = QLabel("List of teachers")
    self._teacher_list = QComboBox()
    
    self._tableview = QTableView()
    
    self.PopulateTeacherComboBox()
    self.PopulateTableView()

    # Create button
    self._close_button = QPushButton("Close")

    # Create a vertical box layout to put the label, line edit and button into
    self._layout = QVBoxLayout()

    # Add the widgets to the vertical box layout
    self._layout.addWidget(self._name_label)
    self._layout.addWidget(self._teacher_list)
    self._layout.addWidget(self._tableview)
    self._layout.addWidget(self._close_button)

    # We then need to set the layout for the QMainWindow.  However, we can't
    # use the setLayout method as it doesn't work properly.  Therefore, put
    # the layout inside a widget and call setCentralWidget on the QMainWindow.
    self._widget = QWidget()
    self._widget.setLayout(self._layout)

    self.setCentralWidget(self._widget)

    # Connect up the button to some method, in this case 'add_name'
    self._close_button.clicked.connect(self.onCloseClicked)
    
  def onCloseClicked(self):
    # Close the window
    #self._parent.setHidden(False)
    self.close()

  def PopulateTeacherComboBox(self):
    teachers = g_database.GetAllTeachers()
    for teacher in teachers:
      self._teacher_list.addItem(teacher[1])
      
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