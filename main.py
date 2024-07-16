#  Combines the UI with the database, connects buttons to functions, and runs the application.
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from learnermanagement2 import Ui_MainWindow 
from database import add_learner,select_learners,searchByName,delete_learner

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        
        
        # Connect buttons to functions
        self.pushButton_12.clicked.connect(self.handle_add_learner)
        self.pushButton_search.clicked.connect(self.handle_search_by_name)
        self.deletebutton.clicked.connect(self.handledeleteSelected)

        
    def handle_add_learner(self):
        name = self.lineEdit_name.text()
        surname = self.lineEdit_surname.text()
        grade = self.lineEdit_grade.text()
        contact = self.lineEdit_contact.text()
        class_name = self.lineEdit_class.text()
        dob = self.lineEdit_dob.text()
        add_learner(name, surname, grade, contact, class_name, dob)
        self.refresh_learners_table()
        print("succcessfully, created")
        self.clear_input_fields()
        
        
#delete selected learners
    def handledeleteSelected(self):
        selected_items = self.tableWidget.selectedItems()
        row = selected_items[0].row()  # Get the row index
        item_id = int(self.tableWidget.item(row, 0).text())
        delete_learner(item_id)
        self.refresh_learners_table()
                    
        
    def clear_input_fields(self):
        self.lineEdit_name.clear()
        self.lineEdit_surname.clear()
        self.lineEdit_grade.clear()
        self.lineEdit_class.clear()
        self.lineEdit_dob.clear()
        self.lineEdit_contact.clear()
        
        
# handles the action of selecting and displaying learners in a table widget.        
    def handle_select_learners(self):
        rows = select_learners()
        #sets the number of rows in self.tableWidget (a QTableWidget) to match the number of rows retrieved (len(rows)).
        self.tableWidget.setRowCount(len(rows))
        for row_num, row_data in enumerate(rows):
            for col_num, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))
                
        
        
    def refresh_learners_table(self):
        # Call handle_select_learners to refresh the table view
        self.handle_select_learners()
        
    def handle_search_by_name(self):
        name = self.lineEdit_search.text()
        rows=searchByName(name)
        
        self.tableWidget.setRowCount(0)

        # Populate the table with the results
        for row_num, row in enumerate(rows):
            self.tableWidget.insertRow(row_num)
            for col_num, data in enumerate(row):
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())