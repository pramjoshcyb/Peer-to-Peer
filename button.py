from PyQt5.QtWidgets import QPushButton

class Button(QPushButton):
    """Create a button based on a QPushButton"""

    def __init__(self, text, x, y):
        super().__init__(text)

        self.x = x
        self.y = y

        # set up a click handler for this button
        self.clicked.connect(self.click_handler)


    def click_handler(self):

        print(self.x, ",", self.y)

