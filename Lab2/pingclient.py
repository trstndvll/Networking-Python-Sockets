'''
=================================
Name       : Tristan Douville
V-number   : V00820003
Date       : March 8, 2019
Assignment : CSC 361 Lab 2
File Name  : pingclient.py
=================================
'''

#import socket modules
from socket import *
import sys
import time

#create a UDP socket
clientSocket = socket(AF_INET,SOCK_DGRAM)

#prepare a client socket
host = str(sys.argv[1]) #current IP address
port = int(sys.argv[2]) #12000

#send 10 pings
for i in range(1,11):
	
	#find the start time
	start = time.time()

	#send our server the message
	message = 'Ping ' + str(i) + ' from ' + str(host) + ' @ ' + str(time.strftime('%H:%M:%S'))
	clientSocket.sendto(message, (host,port))

    #wait for 1 second
	clientSocket.settimeout(1)

	#if we receive the data, print it along with the round trip time
	try:
		data, addr = clientSocket.recvfrom(1024)
		receive = time.time()
		rtt = receive - start
		print(data + ' WITH RTT ' + str(rtt))

    #if not, print a request timeout
	except timeout:
		print('Request timed out')
		continue

clientSocket.close()
