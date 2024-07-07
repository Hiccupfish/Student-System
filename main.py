#  Combines the UI with the database, connects buttons to functions, and runs the application.
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from learner_management import Ui_MainWindow 
from database import add_learner,select_learners

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        
        
        # Connect buttons to functions
        self.pushButton_add.clicked.connect(self.handle_add_learner)

        
    def handle_add_learner(self):
        name = self.lineEdit_name.text()
        surname = self.lineEdit_surname.text()
        grade = self.lineEdit_grade.text()
        contact = self.lineEdit_contact.text()
        class_name = self.LineEdit_class.text()
        dob = self.lineEdit_dob.text()
        add_learner(name, surname, grade, contact, class_name, dob)
        self.refresh_learners_table()
        print("succcessfully, created")
        
    def handle_select_learners(self):
        rows = select_learners()
        self.tableWidget.setRowCount(len(rows))
        for row_num, row_data in enumerate(rows):
            for col_num, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))
        
        
    def refresh_learners_table(self):
        # Call handle_select_learners to refresh the table view
        self.handle_select_learners()
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())