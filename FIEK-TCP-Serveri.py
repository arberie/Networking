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
    
    def ZANORE(teksti):
        nrZ=0
        zanoret = ['A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y']
        for i in teksti:
            if i in zanoret:
                nrZ+=1
        serverSocket.sendto(str(str(nrZ)).encode('utf-8'), clientAddress)

    def PRINTO(teksti):
        serverSocket.sendto(str(teksti).encode('utf-8'), clientAddress)
    def HOST():
                  hosti = gethostbyname(gethostname())
                  conS.send(str("Hosti " + hosti).encode("ASCII"))
                  conS.close()
    def KENO():
                  keno=[random.randint(1,80) for i in range(20)]
                  conS.send(str(str(keno)).encode("ASCII"))
                  conS.close()
    def FAKTORIEL():
                f=1
                if(opsioni==""):
                   conS.send(str("Ju lutemi shtypni nje numri pas komandes.").encode('ASCII'))
                else:
                  numri = int(opsioni)
                if numri < 0:
                   conS.send(str("Faktorieli nuk i perkrah numrat negativ").encode('ASCII'))
                elif numri == 0:
                   conS.send(str("Faktorieli i numrit 0 eshte 1").encode('ASCII'))
                elif numri > 1:
                     f= 1
                while numri > 1:
                  f = f* numri
                  numri = numri - 1 
                  
                conS.send(str("Faktorieli i numrit " + str(opsioni) + " eshte " + str(f) + ".").encode('ASCII'))
                conS.close() 
