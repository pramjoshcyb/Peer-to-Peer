import socket

import select


class Network():
    class Connection():
        """Encapsulates a connection to a remote host"""
        """method to initialise the self attribute, host, port and socket"""
        def __init__(self, host = None, port = None, socket_ = None):
            if socket_ is not None:
                self.socket = socket_
                self.connected = True
            elif host is not None:
                self.host = host
                self.port = port

                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.setblocking(0)


                self.try_connect()
                self.connected = False

            else:
                raise TypeError()

        def try_connect(self):
            """tries to connect to the host and port specified in the constructor
            and sets self.connected to True if successful"""

            try:
                self.socket.connect((self.host, int(self.port)))
                self.connected = True
            except BlockingIOError as e:
                pass


        def send(self, bytes):
            """sends some data (a bytes object) to the other host"""
            self.socket.send(bytes) # calls the send method on a Python socket (see socket docs)

        def try_receive(self):
            """receives and returns some data (a bytes object) from the other host"""
            (inputs_ready, dontcare, dontcare) = select.select([self.socket], [], [], 0)

            # inputs_ready == [] if no connection available
            # inputs_ready == [self.socket] if a connection is available

            if len(inputs_ready) == 0:
                return None

            # DECRYPT THE BYTES HERE BEFORE RETURNING

            return self.socket.recv(1024)
    class Listener():
        """Encapsulates a thing listening for connections"""

        def __init__(self, port):
            """ method to initialise the ports and the self attributes"""
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind(('0.0.0.0', port))
            self.socket.listen()

        def try_get_connection(self):
            """Tries to get an incoming Connection, returning it or None"""

            (inputs_ready, dontcare, dontcare) = select.select([self.socket], [], [], 0)

            # inputs_ready == [] if no connection available
            # inputs_ready == [self.socket] if a connection is available

            if len(inputs_ready) == 0:
                return None

            (client_socket, dontcare) = self.socket.accept()

            return Network.Connection(socket_ = client_socket)

    def get_ip():
        """ method to get the ip address from the address of internets"""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            ip_address = s.getsockname()[0]
        except:
            ip_address = '127.0.0.1'
        finally:
            s.close()
        return ip_address
