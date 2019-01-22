from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton


from button import Button

class App():
    """The App class encapsulates our application"""

    def __init__(self):
        app = QApplication([])

        window = QWidget()
        layout = QVBoxLayout()
        # layout ,----------------.
        #
        #            rowWidget  A
        #            rowWidget  A
        #            rowWidget  A
        #
        #        `----------------`

        # rowWidget [  rowLayout <- B  ]

        # rowLayout [  button <- C   button <- C   button <- C  ]

        #layout.addWidget(label)
        buttons = []

        for i in range(8):
            rowWidget = QWidget()
            layout.addWidget(rowWidget)     # A

            rowLayout = QHBoxLayout()
            rowWidget.setLayout(rowLayout)  # B
            for j in range(8):
                button = Button('x', j, i)
                rowLayout.addWidget(button) # C
                buttons.append(button)

        # connect a handler to the 'clicked' signal of the button
        #button.clicked.connect(self.button_clicked)

        window.setLayout(layout)
        window.show()

        # store the variables we will need later in attributes
        self.app = app
        self.window = window
        self.layout = layout
        self.buttons = buttons
        #self.label = label
        #self.button = button

    def button_clicked(self):
        self.cookies -= 1
        self.label.setText('There are ' + str(self.cookies) + ' cookies in the cookie jar')

    def run(self):
        """Call this method to run the app (starts the event loop)"""
        self.app.exec_()
