import sys
from PySide6.QtWidgets import (
    QMainWindow,
    QWidgetAction,
    QMenuBar
)

from PySide6.QtGui import  (
    QAction,
    QIcon,
    QKeySequence,
    QPixmap
)

import buttons_rc

class J2_FileMenu1(QMenuBar):

    def __init__(self, menubar):
        super().__init__()

        menu_bar = menubar
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("E&xit")
        quit_action.triggered.connect(self.actionExit)



    def actionExit() -> None:
        sys.exit()

