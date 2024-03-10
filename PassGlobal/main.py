#!/usr/bin/env python3
# coding: utf-8

import sys
import qdarktheme
import traceback

from classes import call0
from classes import call123
from classes import call456

"""
Declaration of Global Variables for this Python Applications
"""

gWallet = int(123)
gTerminate = False

def main():
    global gWallet
    global gTerminate

    try:
        while gTerminate is False:
            input("")
            match gWallet:
                case 0:
#                    print(f"gWallet should be 0 and is {gWallet}")
                    gTerminate = call0.Call0(gWallet)
                    gWallet = int(456)
                    
                case 123:
#                    print(f"gWallet should be 123 and is {gWallet}")
                    gTerminate = call123.Call123(gWallet)
                    gWallet = int(0)    
                    
                case 456:
#                    print(f"gWallet should be 456 and is {gWallet}")
                    gTerminate = call456.Call456(gWallet)
                    gWallet = int(123) 
                    
                case _:
                    print(f"gWallet should be ? and is {gWallet}")
                    gWallet = int(0)             
                                                            


        
    except Exception as err:
        print("Unfortunately PassGlobal has encountered an error \
and is unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception()
        
#    finally:
#        sys.exit(app.exec())


if __name__ == '__main__':
    print(f"1. __name__ = {__name__}")
    print("")
    main()