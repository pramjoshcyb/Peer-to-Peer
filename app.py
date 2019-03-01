from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QSpacerItem
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QTextEdit, QRadioButton
from PyQt5.QtGui import QMovie # import for the loading gif
from PyQt5.QtGui import QPalette


from network import Network

from button import Button

# NAMING CONVENTION we will use for PyQt widgets
# txt_ is a multi line text box
# inp_ is an input box
# btn_ is a button
# lbl_ is a label

   
# make sure you add the label to a layout



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
    




class App():
    """This class encapsulates out application"""
    # constructor
    def __init__(self):

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
        self.create_game_pane()

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
        rad_help = QRadioButton('HELP') # help button

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
        show_help = QTextEdit('Hi player, wait for connection means that the interface is actively listening for connections to the other side, connect to... means that it can connect to another player, here is a URL to help see the instructions for the game: https://github.com/pramjoshcyb/Peer-to-Peer/blob/master/README.md ')
        help_pane = make_container_widget([show_help])
        connection_pane = make_container_widget([rad_listen, rad_connect, rad_help, listen_pane, connect_pane, help_pane])
        # set up the radio buttons to control which pane is visible
        def show_listen_pane():
            connect_pane.hide()
            connection_pane.adjustSize()
            listen_pane.show()
            help_pane.hide()

        def show_client_pane():
            listen_pane.hide()
            connection_pane.adjustSize()
            connect_pane.show()
            help_pane.hide()
        
        def show_help_pane():
            listen_pane.hide()
            connection_pane.adjustSize()
            connect_pane.hide()
            help_pane.show()
        
        
        rad_listen.clicked.connect(show_listen_pane)
        rad_connect.clicked.connect(show_client_pane)
        rad_help.clicked.connect(show_help_pane)

        show_listen_pane()


        self.connection_pane = connection_pane
        self.inp_connect_address = inp_connect_address

    def create_game_pane(self):
        # Create the pane that allows the user to chat
        game_pane = QWidget()

        # Create a layout for the chat pane
        game_layout = QGridLayout()
        loading_label = QLabel()
        game_layout.addWidget(loading_label, 3, 0, 1, 4)
        movie = QMovie("Ellipsis.gif")
        loading_label.setMovie(movie)
        movie.start()

        buttons = []

        for i in range(3):
            button_row = []
            for j in range(3):
                button = Button(self.make_choice, j, i)
                game_layout.addWidget(button, i, j) # C
                button_row.append(button)
            buttons.append(button_row)

        game_pane.setLayout(game_layout)

        self.buttons = buttons
        self.game_layout = game_layout
        self.game_pane = game_pane
        self.loading_label = loading_label # hiding purposes


    def tick(self):
        """for accepting, receiving and connecting,
           tick method is called ten times a second
        """

        if self.accepting: # where its receiving a connection
            self.connection = self.listener.try_get_connection()
            if self.connection is not None:
                # connection has been established
                # loading_label = QLabel()
                #self.loading_label = loading_label # hide loading label
                self.loading_label.hide()
                self.game_pane.adjustSize()
                self.game_pane.updateGeometry()

                self.accepting = False
                self.receiving = True
                # self.txt_history.append('Connected!\n')
        
        elif self.receiving:
            they_sent = self.connection.try_receive()
            if they_sent is not None:
                display = 'Them: ' + str(they_sent, 'utf-8')
                print(they_sent)
                they_sent = str(they_sent, 'utf-8')
                x = int(they_sent[1])
                y = int(they_sent[0])
                print(x)
                print(y)
                self.buttons[x][y].set_handler_O()
                #self.txt_history.append(display)

        elif self.connection is not None:
            self.connection.try_connect()
            if self.connection.connected:
                # connection being established on the client
                # loading_label = QLabel()
                # self.loading_label = loading_label # hide loading label
                self.loading_label.hide() # to hide the loading gif once a conn has been made
                self.receiving = True
                #self.txt_history.append('Connected!\n')
        



    def btn_connect_clicked(self):
        # When connect button is clicked, show the chat pane
        self.window.setCentralWidget(self.game_pane)

        #self.txt_history.append('Connecting...')

        self.connection = Network.Connection(self.inp_connect_address.text(), 5000)



    def btn_listen_clicked(self):
        # Currently when listen button is clicked, show the chat pane
        self.window.setCentralWidget(self.game_pane)

        #self.txt_history.append('Waiting for connection...')

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

    def make_choice(self, x, y): # a new method made by me for the noughts app where it sends the coordinates to the other person
        to_send = str(x) + str(y) # these are the coord of x and y in a tuple, need to convert to str to send to server
        self.connection.send(bytes(to_send, 'utf-8'))
