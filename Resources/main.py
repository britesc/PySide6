#!/usr/bin/env python3
# coding: utf-8

import sys
import traceback
import resources.buttons.buttons as vButtons
import actions.actions as vActions


def main():
    try:
        retval = vButtons.DefineButtons()        
        if retval:
           print(f"Returned True = {retval}")
        else:
           print(f"Returned False = {retval}")

        retval = vActions.DefineActions()
        if retval:
           print(f"Returned True = {retval}")
        else:
           print(f"Returned False = {retval}")

    except Exception as err:
        print("Unfortunately TabTest has encountered an error \
and is unable to continue.")
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception()

    finally:
        sys.exit()


if __name__ == '__main__':
    main()