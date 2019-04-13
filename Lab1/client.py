'''
=================================
Name       : Tristan Douville
V-number   : V00820003
Date       : February 5, 2019
Assignment : CSC 361 Lab 1
File Name  : client.py
=================================
'''

#import socket module
from socket import *
import sys

#creating a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#prepare a client socket
host = str(sys.argv[1])
port = int(sys.argv[2])
filename = str(sys.argv[3])

#just printer things
print 'host: ' + host
print 'port:', port
print 'filename: ' + filename

#establish the connection via the given host and port
clientSocket.connect((host, port))

#create and send HTTP request to the server
message = 'GET ' + '/' + filename + ' HTTP/1.1\n\r\n'
clientSocket.sendall(message)
reply = clientSocket.recv(4096)

print 'reply: ' + reply