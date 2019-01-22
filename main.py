#!/usr/bin/python3

import sys

if sys.version_info[0] < 3:
    print("Must use Python 3")
    exit()



from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

label = QLabel('There are 50 cookies in the cookie jar')
layout.addWidget(label)
button = QPushButton('Eat cookie')
layout.addWidget(button)

cookies = 50

def button_clicked():
    global cookies
    cookies -= 1
    label.setText('There are ' + str(cookies) + ' cookies in the cookie jar')

button.clicked.connect(button_clicked)

window.setLayout(layout)
window.show()

app.exec_()


