from PyQt5.QtWidgets import QPushButton

import random


class Button(QPushButton):
    """Create a button based on a QPushButton"""

    def __init__(self, choice_fn, x, y):
        super().__init__(" ")

        random_number = random.randint(0, 101)
        if random_number < 20:
            self.mine = True
        else:
            self.mine = False

        self.setFixedSize(20, 20)
        self.x = x
        self.y = y
        self.choice_fn = choice_fn
        self.revealed = False

        # set up a click handler for this button
        self.clicked.connect(self.click_handler)


    def click_handler(self): # needs to have argument self, x and y position
        self.setText("X")
        self.setDisabled(True)
        self.choice_fn(self.x, self.y)

        # self.setText("O")

        # if not self.revealed:
        #     self.revealed = True
        #     if self.mine:
        #         self.game_over_fn()
        #         self.setText('X')

        #     else:
        #         self.setDisabled(True)
        #         count = self.reveal_fn(self.x, self.y)
        #         if count > 0:
        #             self.setText(str(count))
        #         else:
        #             self.setText('X')

    def set_handler_O(self): #method that calls an object and converts text to O
        self.setText("O")
        self.setDisabled(True)
        # self.choice_fn(self.x, self.y)

        

    # def explode(self):
       # if self.mine:
          #  self.setText('X')

