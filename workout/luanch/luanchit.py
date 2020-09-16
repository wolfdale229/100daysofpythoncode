#! /usr/bin/env python3

"""This is a script that automates the luanching of applications
from the system'
s terminal
"""

import os
import sys
from typing import List

def luanch_apps(process: List) -> None:
    """Loops through a list of applications and pass
    them to the os.system's module
    """

    # loop through each applications in the list
    for app in process:
        os.system(app) # open each app:

def get_app() -> List:
    """This function gets applications to
    luanch as command line variables and appends them to a list"""

    apps = []  # empty list to hold the command in variables
    if len(sys.argv) > 1:
        apps = sys.argv[1:]
    else:
        print('No application stated')
    return apps # return the list of all app

def main():
    """Main program"""
    apps = get_app()
    luanch_apps(apps)

if __name__ == '__main__':
    main()
