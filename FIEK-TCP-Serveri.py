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
    
    def ZANORE():
    nrZ=0
    zanoret = ['A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y']
        for i in opsioni:
              if i in zanoret:
                  nrZ+=1
                  conS.send(str(str(nrZ)).encode("ASCII"))
                  conS.close()
    def PRINTO():
         conS.send(str(opsioni).encode("ASCII"))
    def HOST():
         hosti = gethostbyname(gethostname())
         conS.send(str("Hosti " + hosti).encode("ASCII"))
         conS.close()
