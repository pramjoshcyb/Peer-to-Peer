from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton


class App():
    """The App class encapsulates our application"""

    def __init__(self):
        app = QApplication([])

        window = QWidget()
        layout = QVBoxLayout()

        label = QLabel('There are 50 cookies in the cookie jar')
        layout.addWidget(label)
        button = QPushButton('Eat cookie')
        layout.addWidget(button)

        self.cookies = 50

        # connect a handler to the 'clicked' signal of the button
        button.clicked.connect(self.button_clicked)

        window.setLayout(layout)
        window.show()

        # store the variables we will need later in attributes
        self.app = app
        self.window = window
        self.layout = layout
        self.label = label
        self.button = button

    def button_clicked(self):
        self.cookies -= 1
        self.label.setText('There are ' + str(self.cookies) + ' cookies in the cookie jar')

    def run(self):
        """Call this method to run the app (starts the event loop)"""
        self.app.exec_()
