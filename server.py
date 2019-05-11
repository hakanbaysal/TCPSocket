#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading
from reactor import *
import multiprocessing

class Server():

    def __init__(self):
        bind_ip = '0.0.0.0'
        bind_port = 9999

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((bind_ip, bind_port))
        self.server.listen(5)  # max backlog of connections

        print 'Listening on {}:{}'.format(bind_ip, bind_port)
        self.listen()

    def listen(self):
        while True:
            client_sock, address = self.server.accept()
            print 'Accepted connection from {}:{}'.format(address[0], address[1])
            # reactor(client_sock)
            threading.Thread(target=reactor, args=(client_sock,)).start()
            multiprocessing.Process(target=reactor, args=(client_sock,)).start()

if __name__ == '__main__':
    Server()