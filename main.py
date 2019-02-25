#!/usr/bin/python3

import sys 

from app import App

if sys.version_info[0] < 3:
    print("Must use Python 3")
    exit()

# creates an app objecto
app = App()

# starts the app
app.run()





