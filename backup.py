from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget, QMainWindow, QSpacerItem, QLabel, QPushButton, QLineEdit, QTextEdit, QRadioButton
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette


from button import Button
# from network import Network



def make_container_widget(widgets, vertical = True):
    """Takes a list of widgets and creates a vertical or horizontal kayout
       with the widgets in it."""

    new_widget = QWidget()

    if vertical:
        new_layout = QVBoxLayout()
    else:
        new_layout = QHBoxLayout()
    
    for widget in widgets:
        new_layout.addWidget(widget)
    
    new_widget.setLayout(new_layout)

    return new_widget
    
class ChatUI():
    """This class encapsulates out application"""
    # constructor


def __init__(self):
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

# window.setLayout(layout)
# window.show()
# NAMING CONVENTION we will use for PyQt widgets
# txt_ is a multi line text box
# inp_ is an input box
# btn_ is a button
# lbl_ is a label


# counter for number of clicks
self.button_clicks = 0

# Create a GUI application
app = QApplication([])

# Style app
app.setStyle('Fusion')
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)

# Create our root window
window = QMainWindow()

self.create_connection_pane()
self.create_chat_pane()

# Initially display the connection pane
window.setCentralWidget(self.connection_pane)

# Everything has been set up, create the window
window.show()

# Store the things we will need later in attributes
self.app = app
self.window = window

self.timer = QTimer()
self.timer.start(100)
self.timer.timeout.connect(self.tick)

self.accepting = False
self.receiving = False
self.connection = None

def run(self):
        # Enter the application's main loop
        # This method call doesn't end until the main window is closed
        self.app.exec_()

        print("Application was closed")

def create_connection_pane(self):
        # Create the pane that allows the user to initiate a connection

        # choose listener or client radio buttons
        rad_listen  = QRadioButton('Wait for a connection')
        rad_connect = QRadioButton('Connect to...')

        rad_listen.setChecked(True)

        # Hideable listen pane

        # displays the IP address of the user
        lbl_ip_address = QLabel(Network.get_ip())

        # for the user to listen for an incoming connection
        btn_listen = QPushButton('Wait for connection')
        btn_listen.clicked.connect(self.btn_listen_clicked)

        listen_pane = make_container_widget([lbl_ip_address, btn_listen])


        # for the user to type an IP address and connect to it
        lbl_connect_address = QLabel('IP address')
        inp_connect_address = QLineEdit()
        inp_connect_address.setText('localhost')

        btn_connect = QPushButton('Connect')
        btn_connect.clicked.connect(self.btn_connect_clicked)

        connect_pane = make_container_widget([lbl_connect_address, inp_connect_address, btn_connect])


        # assemble everything into a container
        connection_pane = make_container_widget([rad_listen, rad_connect, listen_pane, connect_pane])

        # set up the radio buttons to control which pane is visible
        def show_listen_pane():
            connect_pane.hide()
            connection_pane.adjustSize()
            listen_pane.show()

        def show_client_pane():
            listen_pane.hide()
            connection_pane.adjustSize()
            connect_pane.show()
        
        rad_listen.clicked.connect(show_listen_pane)
        rad_connect.clicked.connect(show_client_pane)

        show_listen_pane()


        self.connection_pane = connection_pane
        self.inp_connect_address = inp_connect_address

def create_chat_pane(self):
        # Create the pane that allows the user to chat
        chat_pane = QWidget()

        # Create a layout for the chat pane
        chat_layout = QVBoxLayout()
        buttons = []

        # Create the chat history box
        txt_history = QTextEdit()
        txt_history.setPlainText('')
        txt_history.setReadOnly(True)

        # Create a text display
        # lbl_message = QLabel('Type your message:')

        # Create an input box
        inp_message = QLineEdit()

        inp_message.returnPressed.connect(self.send)


        # Add widgets to the chat pane layout
        chat_layout.addWidget(txt_history)

        chat_layout.addWidget(lbl_message)
        chat_layout.addWidget(inp_message)

        chat_pane.setLayout(chat_layout)


        self.inp_message = inp_message
        self.txt_history = txt_history


        self.chat_layout = chat_layout
        self.chat_pane = chat_pane

def tick(self):

        if self.accepting:
            self.connection = self.listener.try_get_connection()
            if self.connection is not None:
                self.accepting = False
                self.receiving = True
                self.txt_history.append('Connected!\n')
        
        elif self.receiving:
            they_sent = self.connection.try_receive()
            if they_sent is not None:
                display = 'Them: ' + str(they_sent, 'utf-8')
                self.txt_history.append(display)

        elif self.connection is not None:
            self.connection.try_connect()
            if self.connection.connected:
                self.receiving = True
                self.txt_history.append('Connected!\n')
        



def btn_connect_clicked(self):
        # When connect button is clicked, show the chat pane
        self.window.setCentralWidget(self.chat_pane)

        self.txt_history.append('Connecting...')

        self.connection = Network.Connection(self.inp_connect_address.text(), 5000)



def btn_listen_clicked(self):
        # Currently when listen button is clicked, show the chat pane
        self.window.setCentralWidget(self.chat_pane)

        self.txt_history.append('Waiting for connection...')

        self.listener = Network.Listener(5000)

        self.accepting = True




def send(self):
        user_typed = self.inp_message.text()

        # add "You: " and put it in display window
        display = "You: " + user_typed
        self.txt_history.append(display)

        # make the input box blank again
        self.inp_message.setText(None)

        self.connection.send(bytes(user_typed, 'utf-8'))

        
def choice_send(self, x, y): # a new method made by me for the noughts app where it sends the coordinates to the other person
        self.connection.send(self.x, self.y)
    