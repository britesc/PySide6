#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import traceback

from PyQt6.QtCore import (
    QSettings,
    QCoreApplication
)    

from PySide6.QtWidgets import (
    QApplication,
    QWidget
) 

def Main() -> None:

self.vApplicationName = os.path.splitext(os.path.basename(__file__))[0]
try:
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    
    
except Exception as err:
    print(f"Unfortunately {self.vApplicationName} has encountered an error \
and is unable to continue.")
    print(f"Exception {err=}, {type(err)=}")
    traceback.print_exc()
    traceback.print_exception()

finally:
    sys.exit(app.exec())


if __name__ == '__main__':
    Main()  