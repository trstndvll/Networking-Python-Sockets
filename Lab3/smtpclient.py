'''
=================================
Name       : Tristan Douville
V-number   : V00820003
Date       : March 26, 2019
Assignment : CSC 361 Lab 3
File Name  : smtpclient.py
=================================
'''

from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

#choose a mail server and call it mailserver
mailserver = "smtp.uvic.ca"
port = 25

#create a socket called clientSocket and establish a TCP connection with the mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

#send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

#send MAIL FROM command and print server response
print "Send email from..."
sender = raw_input()
MAILFROM = "MAIL FROM: <" + sender + ">\r\n"
clientSocket.send(MAILFROM.encode()) 
recv2 = clientSocket.recv(1024).decode()
print recv2
if recv2[:3] != '250':
    print('250 reply not received from server.')

#send RCPT TO command and print server response
print "Send email to..."
receiver = raw_input()
RCPTO = "RCPT TO: " + receiver + "\r\n"
clientSocket.send(RCPTO.encode())
recv3 = clientSocket.recv(1024).decode()
print recv3
if recv3[:3] != '250':
    print('250 reply not received from server.')

#send DATA command and print server response
DATA = "DATA\r\n"
clientSocket.send(DATA.encode())
recv4 = clientSocket.recv(1024).decode()
print recv4
if recv4[:3] != '354':
    print('353 reply not received from server.')

#send message data
clientSocket.send(msg.encode())

#message ends with a single period
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print recv5.decode()
if recv5[:3] != '250':
    print('250 reply not received from server.')

#send QUIT command and get server response.
QUIT = "QUIT\r\n"
clientSocket.send(QUIT.encode())
recv6 = clientSocket.recv(1024).decode()
print recv6
if recv6[:3] != '221':
    print('221 reply not received from server.')

#close socket
clientSocket.close()