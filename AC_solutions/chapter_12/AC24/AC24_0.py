import socket
import threading
import sys


class Client:
    def __init__(self, username):
        self.username = username
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s_client.connect((self.host, self.port))
        except socket.error:
            print('Could not connect')
            sys.exit()

    def listen(self):
        while (True):
            data = self.s_client.recv(1024)
            print(data.decode('ascii'))

    def send(self, message):
        message = self.username + ': ' + message
        self.s_client.send(message.encode('ascii'))


class Server:
    def __init__(self, username):
        self.username = username
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_server.bind((self.host, self.port))
        self.s_server.listen(1)
        self.client = None

    def listen(self, client):
        while (True):
            data = client.recv(1024)
            message = data.decode('ascii')
            print(message)

    def accept(self):
        new_client, address = self.s_server.accept()
        self.client = new_client
        client_thread = threading.Thread(target=self.listen,
                                         args=(new_client,))
        client_thread.daemon = True
        client_thread.start()

    def send(self, message):
        mensaje = self.username + ': ' + message
        self.client.send(mensaje.encode('ascii'))


if __name__ == '__main__':

    pick = input('Select Server (S) or Client (C): ')
    if (pick == 'S' or pick == 's'):
        username = input('Your username: ')
        server = Server(username)
        server.accept()
        while (True):
            message = input()
            server.send(message)

    elif (pick == 'C'):
        username = input('Your username: ')
        client = Client(username)
        listener = threading.Thread(target=client.listen, args=())
        listener.daemon = True
        listener.start()
        while (True):
            message = input()
            client.send(message)
