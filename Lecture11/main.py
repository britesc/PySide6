#!/usr/bin/env python3
# coding: utf-8

from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

sys.exit(app.exec())