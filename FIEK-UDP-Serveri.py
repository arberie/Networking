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
            def KODI(plaintexti, hapi):
        tekstiEnkriptuar = []
        uppercase =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  
        lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for shkronja in plaintexti:
            if shkronja in uppercase:
                indeksi = uppercase.index(shkronja)
                indeksiPlus = indeksi + int(hapi) % 26
                shkronjaRe = uppercase[indeksiPlus]
                tekstiEnkriptuar.append(shkronjaRe)
            elif shkronja in lowercase:
                indeksi = lowercase.index(shkronja)
                indeksiPlus = indeksi + int(hapi) % 26
                shkronjaRe = lowercase[indeksiPlus]
                tekstiEnkriptuar.append(shkronjaRe)
        serverSocket.sendto(str(tekstiEnkriptuar).encode('utf-8'), clientAddress)

    def PRIMAR(p) :
        n = int(p)
        if (n == 1):
            return serverSocket.sendto((str(n) + " nuk eshte numer i thjeshte.").encode('utf-8'), clientAddress)
        elif (n == 2):
            return serverSocket.sendto((str(n) +" eshte numer i thjeshte.").encode('utf-8'), clientAddress)
        else:
            for x in range (2,n):
                if (n%x == 0):
                     return serverSocket.sendto((str(n) + " nuk eshte numer i thjeshte.").encode('utf-8'), clientAddress)
            return serverSocket.sendto((str(n) + " eshte numer i thjeshte.").encode('utf-8'), clientAddress)
    def SIPERFAQJA (r):
        radius = float (r)
        sip = pi*radius*radius;
        serverSocket.sendto(str("Siperfaqja e rrethit eshte : " + str(sip)).encode('utf-8'), clientAddress)

    def PERIMETRI (r):
        radius = float(r)
        perimetri = 2*pi*radius;
        serverSocket.sendto(str("Perimetri i rrethit eshte : " + str(perimetri)).encode('utf-8'), clientAddress)
        
    def DEGREES (shkalla):
        radian = float(shkalla)* (pi/180)
        serverSocket.sendto(str(radian).encode('utf-8'), clientAddress)
    def INDEX(str1):
        stringu = ""
        for index, char in enumerate(str1):  
            stringu += ("Karakteri: " + str(char) + " indexi " + str(index) + "\n")
        serverSocket.sendto((stringu).encode('utf-8'), clientAddress)
    def ASTRO(o, t):   
        opsioni = str(o)
        teksti = int(t)
        if(opsioni=="dhjetor"):
                if(teksti < 22):
                    serverSocket.sendto(str("Shigjetari").encode('utf-8'), clientAddress)
                else:
                    serverSocket.sendto(str("Bricjapi").encode('utf-8'), clientAddress)
        elif(opsioni=="janar"):
                if(teksti<20):
                     serverSocket.sendto(str("Bricjapi").encode('utf-8'), clientAddress)
                else:
                     serverSocket.sendto(str("Ujori").encode('utf-8'), clientAddress)
        elif(opsioni=="shkurt"):
                if(teksti<19):
                     serverSocket.sendto(str("Ujori").encode('utf-8'), clientAddress)
                else:
                     serverSocket.sendto(str("Peshqit").encode('utf-8'), clientAddress)
        elif(opsioni=="mars"):
                if(teksti<21):
                     serverSocket.sendto(str("Peshqit").encode('utf-8'), clientAddress)
                else:
                     serverSocket.sendto(str("Dashi").encode('utf-8'), clientAddress)
        elif(opsioni=="prill"):
                if(teksti<20):
                     serverSocket.sendto(str("Dashi").encode('utf-8'), clientAddress)
                else:
                     serverSocket.sendto(str("Demi").encode('utf-8'), clientAddress)
        elif(opsioni=="maj"):
                if(teksti<21):
                     serverSocket.sendto(str("Demi").encode('utf-8'), clientAddress)
                else:
                     serverSocket.sendto(str("Binjaket").encode('utf-8'), clientAddress)
        elif(opsioni=="qeshor"):
                if(teksti<21):
                     serverSocket.sendto(str("Binjaket").encode('utf-8'), clientAddress)
                else:
                     serverSocket.sendto(str("Gaforrja").encode('utf-8'), clientAddress)
        elif(opsioni=="korrik"):
                if(teksti<23):
                     serverSocket.sendto(str("Gaforrja").encode('utf-8'), clientAddress)
                else:
                     serverSocket.sendto(str("Luani").encode('utf-8'), clientAddress)
        elif(opsioni=="gusht"):
                if(teksti<23):
                     serverSocket.sendto(str("Luani").encode('utf-8'), clientAddress)
                else:
                     serverSocket.sendto(str("Virgjeresha").encode('utf-8'), clientAddress)
        elif(opsioni=="shtator"):
                if(teksti<23):
                     serverSocket.sendto(str("Virgjeresha").encode('utf-8'), clientAddress)
                else:
                     serverSocket.sendto(str("Peshorja").encode('utf-8'), clientAddress)
        elif(opsioni=="tetor"):
                if(teksti<23):
                     serverSocket.sendto(str("Peshorja").encode('utf-8'), clientAddress)
                else:
                     serverSocket.sendto(str("Akrepi").encode('utf-8'), clientAddress)
        elif(opsioni=="nentor"):
                if(teksti<22):
                     serverSocket.sendto(str("Akrepi").encode('utf-8'), clientAddress)
                else:
                     serverSocket.sendto(str("Shigjetari").encode('utf-8'), clientAddress)
    def BINARY (teksti):
        value = 0
        for index, num in enumerate(teksti[::-1]):
            value += int(num)*pow(2,index)
        serverSocket.sendto(str(value).encode('utf-8'), clientAddress)
    if(len(mesazhi)==1):
        funks = mesazhi[0]
        if (funks=="IP"):
            IP()
        if (funks=="PORT"):
            PORT()
        if (funks=="HOST"):
            HOST()
        if (funks=="TIME"):
           TIME()
        if(funks=="KENO"):
           KENO()
    elif(len(mesazhi)==2):
        funks = mesazhi[0]
        teksti = mesazhi[1]
        if(funks=="PRINTO"):
            PRINTO(teksti)
        if(funks=="ZANORE"):
            ZANORE(teksti)
        if(funks=="FAKTORIEL"):
            FAKTORIEL(teksti)
        if(funks=="PRIMAR"):
            PRIMAR(teksti)
        if(funks=="SIPERFAQJA"):
            SIPERFAQJA(teksti)
        if(funks=="PERIMETRI"):
            PERIMETRI(teksti)
        if(funks=="REVERSE"):
            REVERSE(teksti)
        if(funks=="GJATESIA"):
            GJATESIA(teksti)
        if(funks=="BINARY"):
            BINARY(teksti)
        if(funks=="INDEX"):
            INDEX(teksti)
        if(funks=="DEGREES"):
            DEGREES(teksti)

    elif(len(mesazhi)==3):
        funks = mesazhi[0]
        opsioni = mesazhi[1]
        numer = mesazhi[2]
        if(funks=="KONVERTO"):
            KONVERTO()
        if(funks=="KODI"):
            KODI(opsioni,numer)
        if(funks=="ASTRO"):
            ASTRO(opsioni,numer)

