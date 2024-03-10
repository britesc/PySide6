from PySide6.QtCore import QSize
from PySide6.QtGui import QAction,QIcon
from PySide6.QtWidgets import (
    QMainWindow,
    QToolBar,
    QPushButton,
    QStatusBar,
    QMenuBar
)

from activity import Activity

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app member
        self.setWindowTitle("Custom MainWindow")
        

        vCD = Activity(MainWindow)
        vCD.show()