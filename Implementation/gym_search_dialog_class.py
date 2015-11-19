from PyQt4.QtGui import *

class SearchDialog(QDialog):
    """This class creates the dialog window for searching for something"""

    def __init__(self):
        super().__init__()

        #create widgets
        self.table_combo_box = QComboBox()
        self.search_box = QLineEdit()
        self.search_push_button = QPushButton("Search")

        self.table_combo_box.addItem("Select Table")
        self.table_combo_box.addItem("All Tables")
        self.table_combo_box.addItem("Table 1")
        self.search_box.setPlaceholderText("Enter Search Term")

        #create layout
        self.layout = QVBoxLayout()

        #add widgets to layout
        self.layout.addWidget(self.table_combo_box)
        self.layout.addWidget(self.search_box)
        self.layout.addWidget(self.search_push_button)

        #set the window layout
        self.setLayout(self.layout)

        #connections
        """Add Search Button Functionality"""

        
