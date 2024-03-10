import sys
import traceback

from PySide6.QtCore import (
    QSize,
    QObject
)    

from PySide6.QtGui import (
    QAction,
    QIcon
)    
from PySide6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QPushButton,
    QStatusBar,
    QWidget,
    QTabWidget,
    QLabel,
    QMessageBox,
    QPushButton,
    QDialog
)    

import buttonsglassround_rc


from tabs import (
    tab1,
    tab2
)


class FirstClass():
    def __init__(self, mainWindow: QMainWindow, tb, tw) -> None:
        
        # print("\n\n   FirstClass Class")
        # print(mainWindow.menuBar)
        # print(mainWindow.statusBar)
        self.toolBarPrimary = tb
        self.toolBarPrimary.setObjectName(u"toolBarPrimary")
        self.toolBarPrimary.setMinimumSize(QSize(0, 48))
        self.toolBarPrimary.setBaseSize(QSize(0, 0))
        self.toolBarPrimary.setMovable(False)
        self.toolBarPrimary.setIconSize(QSize(48, 48))
        self.toolBarPrimary.setFloatable(False)
        # print(self.toolBarPrimary)
        self.tabWidget = tw
        
        
        
#        mainWindow.setWindowTitle("Class Test - First Class")  # Sets the main window's title, if that's what you're trying to do

#        print(dir(self))
#        print(self.parent)
#        print(self.objectName)
        menubar = mainWindow.menuBar
        file_menu = menubar.addMenu("&File")
        edit_menu = menubar.addMenu("&Edit")
        help_menu = menubar.addMenu("&Help")
        
        
        
        action_exit = QAction(QIcon(u"resources/buttons/glassButtonExit.png"), "E&xit", mainWindow)
        action_exit.setStatusTip("Exit the Application")
        action_exit.setShortcut("Alt+X")
        self.toolBarPrimary.addAction(action_exit)
        file_menu.addSeparator()
        file_menu.addAction(action_exit)
        action_exit.triggered.connect(FirstClass.Response_Exit)


        taba1 = tab1.Tab1()
        tw.addTab(taba1, "Information")

        taba2 = tab2.Tab2()
        tw.addTab(taba2, "Configuration")


    def Response_Exit():
        dlg = QMessageBox()
        dlg.setWindowTitle("Exit the Application")
        dlg.setText("Do you wish to exit the Applications?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Warning)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            sys.exit()
        else:
            pass
