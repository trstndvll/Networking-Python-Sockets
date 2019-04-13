'''
=================================
Name       : Tristan Douville
V-number   : V00820003
Date       : February 5, 2019
Assignment : CSC 361 Lab 1
File Name  : server.py
=================================
'''

#import socket module
from socket import *
import sys #used to terminate the program

#creating a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare a server socket
host= ''
port= 6789
serverSocket.bind((host, port))
serverSocket.listen(5)

while True:
    #establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
            
    try:
        message = connectionSocket.recv(10000)    
        print 'message: ' + message
        filename = message.split()[1]    
        print 'filename: ' + filename[1:]
        f = open(filename[1:]) 

        outputdata = f.read()
        
        #send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\n' + 'Content-Type: text/html\n' + '\r\n' + outputdata)
        
        '''
        #send the content of the requested file to the client
        print 'data:'
        for i in range(0, len(outputdata)):   
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        '''
        
        connectionSocket.close()
        
    except IOError:
        #send response message for file not found
        print 'IOError...'
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n')
        connectionSocket.send('<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n')

        #close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit() #terminate the program after sending the corresponding data
