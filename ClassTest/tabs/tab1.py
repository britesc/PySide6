import qdarktheme

from PySide6.QtWidgets import QWidget, QTabWidget

from tabs import (
    ui_tab1,
    ui_tab2
)


class Tab1(QWidget, Ui_Tab1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        