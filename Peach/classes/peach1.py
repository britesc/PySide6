from PySide6.QtWidgets import (
    QMainWindow,
    QMenuBar,
    QStatusBar,
	QToolBar     
) 

from PySide6.QtCore import Qt, QObject

from PySide6.QtGui import (
    QAction,    
    QIcon
)

class Peach1(QMenuBar, QStatusBar, QToolBar):

    
    def __init__(self, Pearmenubar, Pearstatusbar, Peartoolbar):
        super().__init__()
        
        self.Grapemenubar = Pearmenubar
        
        
        print("peach1-1.py")
        print(dir(self))
        print("")
        print("")
        
        
        Grapetoolbar = QToolBar("My main toolbar")
        QMainWindow.addToolBar(Grapetoolbar)
  
        
        print("peach1-2.py")
        print(dir(self))
        print("")
        print("")
        
        button_action = QAction("Your button", self)
        ts = button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        
        Grapetoolbar.addAction(button_action)
        

#        self.Peachstatusbar.showMessage(ts)   
        
        file_menu = self.Grapemenubar.addMenu("&File")
        file_menu.addAction(button_action)                

        file_menu = self.Grapemenubar.addMenu("&Nudist")

        print("peach1-3.py")
        print(dir(self))
        print("")
        print("")
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)       
    