# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Tshidiso\Student-System\studentfrontside\studentHome.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 512)
        MainWindow.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IconNameWidget = QtWidgets.QWidget(self.centralwidget)
        self.IconNameWidget.setGeometry(QtCore.QRect(0, 0, 231, 511))
        self.IconNameWidget.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(65, 105, 225);\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:white;\n"
"    text-align:left;\n"
"}")
        self.IconNameWidget.setObjectName("IconNameWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.IconNameWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.IconNameWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.IconNameWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_7 = QtWidgets.QPushButton(self.IconNameWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.IconNameWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.IconNameWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_14 = QtWidgets.QPushButton(self.IconNameWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout.addWidget(self.pushButton_14)
        spacerItem = QtWidgets.QSpacerItem(20, 255, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_13 = QtWidgets.QPushButton(self.IconNameWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.Main = QtWidgets.QWidget(self.centralwidget)
        self.Main.setGeometry(QtCore.QRect(240, 0, 541, 521))
        self.Main.setObjectName("Main")
        self.HeaderWidget = QtWidgets.QWidget(self.Main)
        self.HeaderWidget.setGeometry(QtCore.QRect(-60, 0, 507, 45))
        self.HeaderWidget.setObjectName("HeaderWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.HeaderWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_search = QtWidgets.QPushButton(self.HeaderWidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout.addWidget(self.pushButton_search)
        spacerItem2 = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lineEdit_search = QtWidgets.QLineEdit(self.HeaderWidget)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout.addWidget(self.lineEdit_search)
        spacerItem3 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.stackedWidget = QtWidgets.QStackedWidget(self.Main)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 551, 461))
        self.stackedWidget.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: whitergb(255, 247, 252);\n"
"}\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.header = QtWidgets.QLabel(self.page)
        self.header.setGeometry(QtCore.QRect(50, 10, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setObjectName("header")
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setGeometry(QtCore.QRect(20, 200, 491, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.AddStudentFrame = QtWidgets.QFrame(self.page)
        self.AddStudentFrame.setGeometry(QtCore.QRect(30, 40, 491, 91))
        self.AddStudentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AddStudentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AddStudentFrame.setObjectName("AddStudentFrame")
        self.layoutWidget = QtWidgets.QWidget(self.AddStudentFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 0, 139, 88))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_4.addWidget(self.lineEdit_name)
        self.lineEdit_grade = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_grade.setObjectName("lineEdit_grade")
        self.verticalLayout_4.addWidget(self.lineEdit_grade)
        self.lineEdit_contact = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_contact.setObjectName("lineEdit_contact")
        self.verticalLayout_4.addWidget(self.lineEdit_contact)
        self.layoutWidget1 = QtWidgets.QWidget(self.AddStudentFrame)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 45, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.layoutWidget2 = QtWidgets.QWidget(self.AddStudentFrame)
        self.layoutWidget2.setGeometry(QtCore.QRect(260, 0, 54, 91))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.layoutWidget3 = QtWidgets.QWidget(self.AddStudentFrame)
        self.layoutWidget3.setGeometry(QtCore.QRect(330, 0, 139, 88))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_surname = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.verticalLayout_6.addWidget(self.lineEdit_surname)
        self.lineEdit_class = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_class.setObjectName("lineEdit_class")
        self.verticalLayout_6.addWidget(self.lineEdit_class)
        self.lineEdit_dob = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_dob.setObjectName("lineEdit_dob")
        self.verticalLayout_6.addWidget(self.lineEdit_dob)
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(30, 140, 481, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget4 = QtWidgets.QWidget(self.frame)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 10, 471, 30))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_2.addWidget(self.pushButton_12)
        self.updatebutton = QtWidgets.QPushButton(self.layoutWidget4)
        self.updatebutton.setObjectName("updatebutton")
        self.horizontalLayout_2.addWidget(self.updatebutton)
        self.deletebutton = QtWidgets.QPushButton(self.layoutWidget4)
        self.deletebutton.setObjectName("deletebutton")
        self.horizontalLayout_2.addWidget(self.deletebutton)
        self.selectbutton = QtWidgets.QPushButton(self.layoutWidget4)
        self.selectbutton.setObjectName("selectbutton")
        self.horizontalLayout_2.addWidget(self.selectbutton)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton_10 = QtWidgets.QPushButton(self.Main)
        self.pushButton_10.setGeometry(QtCore.QRect(440, 10, 61, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Sidebar"))
        self.pushButton_2.setText(_translate("MainWindow", "Dashboard"))
        self.pushButton_7.setText(_translate("MainWindow", "Learner Management"))
        self.pushButton_8.setText(_translate("MainWindow", "Class Management"))
        self.pushButton_9.setText(_translate("MainWindow", "Reports"))
        self.pushButton_14.setText(_translate("MainWindow", "Settings"))
        self.pushButton_13.setText(_translate("MainWindow", "Sign Out"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))
        self.header.setText(_translate("MainWindow", "Learners"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Surname"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Grade"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DOB"))
        self.label_4.setText(_translate("MainWindow", "Name"))
        self.label_5.setText(_translate("MainWindow", "Grade"))
        self.label_6.setText(_translate("MainWindow", "Contact"))
        self.label_7.setText(_translate("MainWindow", "Surname"))
        self.label_8.setText(_translate("MainWindow", "Class"))
        self.label_9.setText(_translate("MainWindow", "DOB"))
        self.pushButton_12.setText(_translate("MainWindow", "Add"))
        self.updatebutton.setText(_translate("MainWindow", "Update"))
        self.deletebutton.setText(_translate("MainWindow", "Delete"))
        self.selectbutton.setText(_translate("MainWindow", "Select"))
        self.pushButton_10.setText(_translate("MainWindow", "S"))
