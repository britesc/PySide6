#!/usr/bin/env python3
# coding: utf-8

""" Application Main Script File """

""" Standard Python Imports """
import sys
import traceback

""" Specialised Python Imports"""
import qdarktheme

""" PySide6 Python Imports """
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)    

from mainwindow import MainWindow   
""" Load the QT Designer Window """

def main():
    """ Main Function """
    try:
        """ Try """
        app = QApplication(sys.argv)
        window = MainWindow(app)

        window.show()
            
    except Exception as err:
        """ Exception """
        print("Unfortunately Class Test has encountered an error \
and is unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception()

    finally:
        """ Finally close it all down whatever happens """
        sys.exit(app.exec())

""" Call the main function """
if __name__ == '__main__':
    main()    