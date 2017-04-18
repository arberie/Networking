from socket import *
from math import pi
import socket
import time
import datetime
import random
import string

serverPort = 9000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Serveri eshte ne linje...")
while True:
    message, clientAddress = serverSocket.recvfrom(128)
    print("Mesazhi i pranuar: " + message.decode("ASCII"))
    mesazhi = message.decode("ASCII").split(' ')

    def IP ():
        serverSocket.sendto(str(str(clientAddress[0])).encode('utf-8'), clientAddress)
    def PORT():
        serverSocket.sendto(str(str(clientAddress[1])).encode('utf-8'), clientAddress)
    def ZANORE(teksti):
        nrZ=0
        zanoret = ['A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y']
        for i in teksti:
            if i in zanoret:
                nrZ+=1
        serverSocket.sendto(str(str(nrZ)).encode('utf-8'), clientAddress)
    def PRINTO(teksti):
        serverSocket.sendto(str(teksti).encode('utf-8'), clientAddress)
    def KENO():
        keno=[random.randint(1,80) for i in range(20)]
        serverSocket.sendto(str(keno).encode('utf-8'), clientAddress)
   
    def FAKTORIEL(opsioni):
         f=1
        if(opsioni==""):
              serverSocket.sendto(str("Ju lutemi shtypni nje numri pas komandes.").encode('ASCII'), clientAddress)
        else:
              numri = int(opsioni)
        if numri < 0:
              serverSocket.sendto(str("Faktorieli nuk i perkrah numrat negativ").encode('ASCII'), clientAddress)
        elif numri == 0:
              serverSocket.sendto(str("Faktorieli i numrit 0 eshte 1").encode('ASCII'), clientAddress)
        elif numri > 1:
              f= 1
        while numri > 1:
              f = f* numri
              numri = numri - 1 
         serverSocket.sendto(str("Faktorieli i numrit " + str(opsioni) + " eshte " + str(f) + ".").encode('ASCII'), clientAddress)
           
