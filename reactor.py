#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

class reactor():

    def __init__(self, client_socket):
        self.client_socket = client_socket
        self.handle_client_connection()

    def handle_client_connection(self):
        request = self.client_socket.recv(1024)
        print 'Received {}'.format(request)

        if (request == 'client1'):
            print("while başla")
            t1 = datetime.now()
            while (datetime.now() - t1).seconds <= 10:
                print(datetime.now())

        self.client_socket.send(request + ' iletildi')
        self.client_socket.close()
        print '\n\n'