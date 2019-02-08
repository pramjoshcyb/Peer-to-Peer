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

        for i in range(3):
            rowWidget = QWidget()
            layout.addWidget(rowWidget)     # A

            rowLayout = QHBoxLayout()
            rowWidget.setLayout(rowLayout)  # B

            button_row = []
            for j in range(3):
                button = Button(' ', self.choice_send, j, i) #self.game_over
                rowLayout.addWidget(button) # C
                button_row.append(button)
            buttons.append(button_row)

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


    def game_over(self):
        for button_row in self.buttons:
            for button in button_row:
                button.explode()

    def reveal(self, x, y):

        counter = 0

        # work out how many mines are adjacent
        for my_y in range(y-1, y+2):
            for my_x in range(x-1, x+2):

                if (my_y >= 0 and my_y < 3
                and my_x >= 0 and my_x < 3):
    
                    if self.buttons[my_y][my_x].mine:
                        counter += 1

        # might be 0, if so then open surrounding buttons
        if counter == 0:
            for my_y in range(y-1, y+2):
                for my_x in range(x-1, x+2):

                    if (my_y >= 0 and my_y < 3
                    and my_x >= 0 and my_x < 3):     
                        self.buttons[my_y][my_x].click_handler()
        
        return counter

    def run(self):
        """Call this method to run the app (starts the event loop)"""
        self.app.exec_()

    def choice_send(self): # a new method made by me for the noughts app where it sends the coordinates to the other person
        self.connection.send(self.x, self.y)
    choice_send()