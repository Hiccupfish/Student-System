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
