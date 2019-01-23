from PyQt5.QtWidgets import QPushButton

import random

class Button(QPushButton):
    """Create a button based on a QPushButton"""

    def __init__(self, text, game_over_fn, reveal_fn, x, y):
        super().__init__(text)

        random_number = random.randint(0, 101)
        if random_number < 20:
            self.mine = True
        else:
            self.mine = False

        self.setFixedSize(20, 20)
        self.x = x
        self.y = y
        self.reveal_fn = reveal_fn
        self.game_over_fn = game_over_fn
        self.revealed = False

        # set up a click handler for this button
        self.clicked.connect(self.click_handler)


    def click_handler(self):

        if not self.revealed:
            self.revealed = True
            if self.mine:
                self.game_over_fn()
                self.setText('x')

            else:
                self.setDisabled(True)
                count = self.reveal_fn(self.x, self.y)
                if count > 0:
                    self.setText(str(count))
                else:
                    self.setText('☑')

        

    def explode(self):
        if self.mine:
            self.setText('@')

