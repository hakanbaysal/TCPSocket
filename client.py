#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

hostname, sld, tld, port = 'www', 'hakanbaysal', 'com', 80
target = '{}.{}.{}'.format(hostname, sld, tld)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 9999))
# client.send('GET /index.html HTTP/1.1\r\nHost: {}.{}\r\n\r\n'.format(sld, tld))
client.send('client1')
response = client.recv(4096)

print response