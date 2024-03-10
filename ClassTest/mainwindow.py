from PySide6.QtWidgets import (
    QMainWindow
)

from ui_mainwindow import Ui_MainWindow

from classes import firstclass

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.setupUi(self)
        self.app = app

        # self.setWindowTitle("Class Test - QMainWindow")
#        print(dir(self))
        # print("\n\n   MainWindow Class")
#        print(self.parent)
#        print(self.objectName)
        # print(self.toolBarPrimary)        
        firstclass.FirstClass(self, self.toolBarPrimary, self.tabWidget)
              
        
        
        
        
