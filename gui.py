# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
# import sqlite3

# class LearnerManagementSystem(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Learner Management System")
#         self.setGeometry(100, 100, 400, 300)

#         self.init_ui()

#     def init_ui(self):
#         self.name_label = QLabel("Name:", self)
#         self.name_label.move(50, 50)
#         self.name_entry = QLineEdit(self)
#         self.name_entry.setGeometry(150, 50, 150, 20)

#         self.age_label = QLabel("Age:", self)
#         self.age_label.move(50, 80)
#         self.age_entry = QLineEdit(self)
#         self.age_entry.setGeometry(150, 80, 50, 20)

#         self.grade_label = QLabel("Grade:", self)
#         self.grade_label.move(50, 110)
#         self.grade_entry = QLineEdit(self)
#         self.grade_entry.setGeometry(150, 110, 50, 20)

#         self.class_label = QLabel("Class:", self)
#         self.class_label.move(50, 140)
#         self.class_entry = QLineEdit(self)
#         self.class_entry.setGeometry(150, 140, 150, 20)

#         self.add_button = QPushButton("Add Learner", self)
#         self.add_button.setGeometry(100, 200, 200, 30)
#         self.add_button.clicked.connect(self.add_learner)

#     def add_learner(self):
#         name = self.name_entry.text()
#         age = self.age_entry.text()
#         grade = self.grade_entry.text()
#         class_name = self.class_entry.text()

#         if not all([name, age, grade, class_name]):
#             QMessageBox.critical(self, "Error", "Please fill in all fields.")
#             return

#         try:
#             age = int(age)
#             grade = int(grade)
#         except ValueError:
#             QMessageBox.critical(self, "Error", "Age and grade must be numbers.")
#             return

#         try:
#             with sqlite3.connect("StudentSystemv.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT INTO learner (name, age, grade, class) VALUES (?, ?, ?, ?)",
#                             (name, age, grade, class_name))
#                 con.commit()
#                 QMessageBox.information(self, "Success", f"Learner {name} added successfully!")
#         except sqlite3.Error as e:
#             QMessageBox.critical(self, "Error", f"Database error: {e}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = LearnerManagementSystem()
#     window.show()
#     sys.exit(app.exec_())
import sysk
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Menus and Toolbars')
        self.setGeometry(100, 100, 400, 300)
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        toolbar = self.addToolBar('Main Toolbar')
        toolbar.addAction(open_action)
    def open_file(self):
        print('Open file action triggered')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
