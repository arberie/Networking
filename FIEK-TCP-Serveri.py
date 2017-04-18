from socket import *
from math import pi
import sys
import time
import datetime
import random

print("TCP")
serverPort = 9000
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))
serverSocket.listen(1)


while 1:
    conS, clientAddress = serverSocket.accept()
    message = conS.recv(128)
    mesazhi = message.decode("ASCII").split(' ')
    
