'''
=================================
Name       : Tristan Douville
V-number   : V00820003
Date       : March 8, 2019
Assignment : CSC 361 Lab 2
File Name  : pingserver.py
=================================
'''

#we will need the following module to generate randomized lost packets
import random
from socket import *

#create a UDP socket 
#notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

#assign IP address and port number to socket
serverSocket.bind(('', 12000))

print "Server is running..."

while True:
	#generate random number in the range of 0 to 10
	rand = random.randint(0, 10)    

	#receive the client packet along with the address it is coming from 
	message, address = serverSocket.recvfrom(1024)

	#capitalize the message from the client
	message = message.upper()

	#if rand is less is than 4, we consider the packet lost and do not respond
	if rand < 4:
		continue
        
	#otherwise, the server responds    
	serverSocket.sendto(message, address)