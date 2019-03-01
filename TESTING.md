# Testing of the peer to peer application
-	Design One test procedure a human can follow to check the basic behaviour of the application:

When the user listens and the other side connects, the Graphical User Interface with the loading graphic is meant to load up. Once the connection is established the loading graphic should disappear.
User must select a button on the client side that marks the button with a x or o. If this is the case the other side of the connection should be able to see the correct input. 
If the user sees the output of x and o that means they are playing the game correctly.


-	Design at least TWO test procedures a human can follow that provide unusual input that may cause the application to behave undesirably:

If **the user accidentally clicks waiting for connection** on the client and server side then they will be left with just the client side of the Graphical User Interface. The program is meant to be played by two players hence if they click connect to the same port for both sides the error will appear as port is already in use. 
To avoid this issue the user must to assume that the other side is active and must click wait for connection and the other side will connect to the correct port so they can start playing.

**Another test procedure** a human can follow if the application behaves differently with unusual input is if they try to connect twice. 
If this is the case then the user will have to restart the application because they are trying to connect to the server plus connect to the client. 
The application is not designed to handle this, the client must either listen or wait for the connection which lets a port to be free and then the server side can choose to connect to the client’s IP address through the same port. 

- Outcome of each test: 

**Test procedure** to check basic behaviour: works if one side clicks the button it appears as x and the other side is automatically filled with o. It then sends the coordinates of the client’s clicked button to the server side to ensure that they don’t choose the same one and override it.

**Waiting for connection:** throws an error that the port is already in use

**Connect twice:** throws a connection refused error because the user is trying to connect twice.




