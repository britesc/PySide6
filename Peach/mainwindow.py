import qdarktheme

from PySide6.QtCore import Qt, QObject

from PySide6.QtWidgets import (
    QMainWindow,
    QTabWidget,
    QLabel
)    

from PySide6.QtGui import (
    QAction,    
    QIcon
)    

from ui_mainwindow import Ui_MainWindow

from classes import peach1

vVersion = "1.0.1.0"

class MainWindow(QMainWindow, Ui_MainWindow):
    

    
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.setWindowTitle("Peach")
        
        
        print("mainwindow.py")
        print(dir(self))
        print("")
        print("")
        
        label = QLabel(vVersion)
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label) 
        
        print("app")
        print(dir(app))
        print("")
        print("")       
        
        vMenuBar = self.Peachmenubar

        VStatusBar = self.Peachstatusbar
        
        vToolBar = self.PeachtoolBar    
        
        
        peach1.Peach1(vMenuBar, VStatusBar, vToolBar)    
      
"""     
        button_action = QAction("Your button", self)
        ts = button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        vToolBar.addAction(button_action)
        VStatusBar.showMessage(ts)
        
        file_menu = vMenuBar.addMenu("&File")
        file_menu.addAction(button_action)
"""
                
        
"""
    def onMyToolBarButtonClick(self, s):
        print("click", s)        
"""