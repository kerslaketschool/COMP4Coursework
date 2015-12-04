#Sweat Gymnasium Datbase Management System 9001

import sys
import webbrowser

from gym_open_dialog_class import *
from gym_delete_dialog_class import *
from gym_print_dialog_class import *
from gym_search_dialog_class import *
from gym_edit_dialog_class import *
from gym_add_dialog_class import *
from gym_about_dialog_class import *
from gym_password_dialog_class import *



from data_browser import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AppWindow(QMainWindow):
    """creates the main window"""

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gym Database Management System 9001")

        #toolbars
        self.setWindowIcon(QIcon("Logo.png"))
        self.open_push_button = QPushButton("Open")
        self.add_push_button = QPushButton("Add")
        self.edit_push_button = QPushButton("Edit")
        self.delete_push_button = QPushButton("Delete")
        self.search_push_button = QPushButton("Search")
        self.print_push_button = QPushButton("Print")

        self.tab_bar = QTabWidget()
        
        self.tabs = {}
        for count in range(10):
            self.tabs["tab_{0}".format(count + 1)] = BrowseDataWidget()
            self.tab_bar.addTab(self.tabs["tab_{0}".format(count + 1)],"Tab{0}".format(count + 1))

        self.toolBar = QMenuBar()
        self.file_menu = self.toolBar.addMenu("File")
        self.help_menu = self.toolBar.addMenu("Help")
        self.about = self.help_menu.addAction("About Gym Database Management System 9001")
        self.open_shortcut = self.file_menu.addAction("Open")
        self.add_shortcut = self.file_menu.addAction("Add")
        self.edit_shortcut = self.file_menu.addAction("Edit")
        self.delete_shortcut = self.file_menu.addAction("Delete")
        self.search_shortcut = self.file_menu.addAction("Search")
        self.print_shortcut = self.file_menu.addAction("Print")


        #layout
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QVBoxLayout()

        self.layout1.addWidget(self.open_push_button)
        self.layout1.addWidget(self.add_push_button)
        self.layout1.addWidget(self.edit_push_button)

        self.layout2.addWidget(self.delete_push_button)
        self.layout2.addWidget(self.search_push_button)
        self.layout2.addWidget(self.print_push_button)

        self.layout3.addWidget(self.tab_bar)
        self.layout3.addLayout(self.layout1)
        self.layout3.addLayout(self.layout2)

        self.mainWidget = QWidget()
        self.setMenuWidget(self.toolBar)
        self.mainWidget.setLayout(self.layout3)
        self.setCentralWidget(self.mainWidget)

        #connections
        self.open_push_button.clicked.connect(self.open_file_menu)
        self.delete_push_button.clicked.connect(self.delete)
        self.print_push_button.clicked.connect(self.print_stuff)
        self.search_push_button.clicked.connect(self.search)
        self.edit_push_button.clicked.connect(self.edit)
        self.add_push_button.clicked.connect(self.add)
        self.about.triggered.connect(self.hayley)
        self.open_shortcut.triggered.connect(self.open_file_menu)
        self.add_shortcut.triggered.connect(self.add)
        self.edit_shortcut.triggered.connect(self.edit)
        self.delete_shortcut.triggered.connect(self.delete)
        self.search_shortcut.triggered.connect(self.search)
        self.print_shortcut.triggered.connect(self.print_stuff)


    def open_file_menu(self):
        open_dialog = OpenDialog()
        open_dialog.exec_()

    def open_file(self):
        path = QFileDialog.getOpenFileName(caption="Open Database",filter = "Database file (*.db *.dat)")

    def delete(self):
        self.password()
        delete_dialog = DeleteDialog()
        delete_dialog.exec_()

    def print_stuff(self):
        print_dialog = PrintDialog()
        print_dialog.exec_()
        
    def search(self):
        search_dialog = SearchDialog()
        search_dialog.exec_()

    def edit(self):
        edit_dialog = EditDialog(17)
        edit_dialog.exec_()

    def add(self):
        add_dialog = AddDialog(12)
        add_dialog.exec_()

    def hayley(self):
        QSound.play("Westenraaaaaa.wav")
        about_dialog = AboutDialog()
        about_dialog.exec_()

    def password(self):
        passWord = ""
        while passWord != "ryansucks":
            password_dialog = PasswordDialog()
            password_dialog.exec_()
            passWord = PasswordDialog.close_funk
            print(passWord)

        
def main():   
    gym_program = QApplication(sys.argv)
    gym_window = AppWindow()
    gym_window.resize(700,600)
    gym_window.show()
    gym_window.raise_()
    gym_program.exec_()
    

if __name__ == "__main__":
    main()
