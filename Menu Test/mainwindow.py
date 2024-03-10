from PySide6.QtWidgets import (
    QMainWindow
)
from ui_mainwindow import Ui_MainWindow
from classes._j2_menooptions1 import J2_MenuOptions1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Menu Test")
            
        vJ2M = J2_MenuOptions1(self.menubar)
     
        

        
        
