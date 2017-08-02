import socket
import threading
import sys
import ChatUI
import select


class Client:
    def __init__(self, username):
        self.username = username
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.chat = ChatUI.Chat(username)
            self.thread_wait_server = threading.Thread(
                target=self.wait_server)
            self.thread_wait_server.start()
            self.chat.init_UI()

        except socket.error:
            print('Could not connect')
            sys.exit()

    def wait_server(self):
        self.connect()
        while (True):
            if self.chat.upload_pressed():
                self.send(self.chat.get_path())

    def connect(self):
        self.s_client.connect((self.host, self.port))
        self.listener = threading.Thread(target=self.listen, args=())
        self.listener.daemon = True
        self.listener.start()

    def listen(self):
        while True:
            data = self.s_client.recv(1024)
            with open('./client_photo.jpg', 'wb+') as f:
                while data:
                    f.write(data)
                    ready = select.select([self.s_client], [], [], 0)
                    if (ready[0]):
                        data = self.s_client.recv(1024)
                    else:
                        data = b''
                        self.chat.update_image('./client_photo.jpg')

    def send(self, path):
        with open(path, 'rb') as f:
            data = f.read()
            self.s_client.send(data)
        self.chat.update_image(path)


class Server:
    def __init__(self, username):
        self.username = username
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_server.bind((self.host, self.port))
        self.s_server.listen(1)
        self.client = None

        self.chat = ChatUI.Chat(username)
        self.thread_wait_client = threading.Thread(
            target=self.wait_client)
        self.thread_wait_client.start()
        self.chat.init_UI()

    def wait_client(self):
        self.accept()
        while (True):
            if self.chat.upload_pressed():
                self.send(self.chat.get_path())

    def accept(self):
        new_client, address = self.s_server.accept()
        self.client = new_client
        thread_client = threading.Thread(target=self.listen)
        thread_client.daemon = True
        thread_client.start()

    def listen(self):
        while True:
            data = self.client.recv(1024)
            with open('./server_photo.jpg', 'wb+') as f:
                while data:
                    f.write(data)
                    ready = select.select([self.client], [], [], 0)
                    if (ready[0]):
                        data = self.client.recv(1024)
                    else:
                        data = b''
                        self.chat.update_image('./server_photo.jpg')

    def send(self, path):
        with open(path, 'rb') as f:
            data = f.read()
            self.client.send(data)
        self.chat.update_image(path)


if __name__ == '__main__':

    pick = input('Select Server (S) or Client (C):')
    if (pick == 'S' or pick == 's'):
        server = Server('Server')

    elif (pick == 'C' or pick == 'c'):
        username = input('Client username: ')
        client = Client(username)
