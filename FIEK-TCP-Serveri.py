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
         nrZ = 0
         zanoret = ['A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y']
            for i in opsioni:
                 if i in zanoret:
                    nrZ+=1
                    conS.send(str(str(nrZ)).encode("ASCII"))
                    conS.close()         
    def PRINTO(teksti):
         conS.send(str(opsioni).encode("ASCII"))
    def HOST():
         hosti = gethostbyname(gethostname())
         conS.send(str("Hosti " + hosti).encode("ASCII"))
         conS.close()
    def TIME():
         date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
         conS.send(str(str(date)).encode("ASCII"))
         conS.close()
                    
    def KONVERTO():        
          if(opsioni=="CelsiusToKelvin"):
                 shkalla = 273.16+int(numri)
                 conS.send(str(str(numri)+" Celsius = "+ str(shkalla)+" Kelvin").encode("ASCII"))
                 conS.close()
            elif(opsioni=="CelsiusToFahrenheit"):
                 shkalla = (9*float(numri)/5)+32
                 conS.send(str(str(numri)+"Celsius "+ str(shkalla)+" Farenhajt").encode("ASCII"))
                 conS.close()
            elif(opsioni=="KelvinToFarenheit"):
                 shkalla = 1.8*(float(numri)-273)+32
                 conS.send(str(str(numri)+"Kelvin "+ str(shkalla)+" Farenhajt").encode("ASCII"))
                 conS.close()
            elif(opsioni=="KelvinToCelsius"):
                 shkalla = float(numri)-273.15
                 conS.send(str(str(numri)+"Kelvin "+ str(shkalla)+" Celsius").encode("ASCII"))
                 conS.close()
            elif(opsioni=="FahrenheitToCelsius"):
                 shkalla = 5*(float(numri)-32)/9
                 conS.send(str(str(numri)+"Farenhight "+ str(shkalla)+" Celsius").encode("ASCII"))
                 conS.close()
            elif(opsioni=="FahrenheitToKelvin"):
                 shkalla = 5*(float(numri)-32)/9
                 conS.send(str(str(numri)+"Farenhight "+ str(shkalla)+" Kelvin").encode("ASCII"))
                 conS.close()
            elif(opsioni=="PoundToKilogram"):
                 shkalla= float(numri)*0.45359237
                 conS.send(str(str(numri)+"Pound "+ str(shkalla)+" Kilogram").encode("ASCII"))
                 conS.close()
            elif(opsioni=="KilogramToPound"):
                 shkalla = float(numri)*2.2046226218
                 conS.send(str(str(numri)+"Kilogram "+ str(shkalla)+" Pound").encode("ASCII"))
            else:
                 conS.send("Shkruaj ne formen : KONVERTO llojikonvertimit numri ".encode('ASCII'))
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
        conS.send(str(tekstiEnkriptuar).encode('ASCII'))
        
    def PRIMAR(p) :
        n = int(p)
        if (n == 1):
            return conS.send(("Nuk eshte numer i thjeshte.").encode('ASCII'))
        elif (n == 2):
            return conS.send(("Eshte numer i thjeshte.").encode('ASCII'))
        else:
            for x in range (2,n):
                if (n%x == 0):
                     return conS.send(("Nuk eshte numer i thjeshte.").encode('ASCII'))
            return conS.send(("Eshte numer i thjeshte.").encode('ASCII'))
    def INDEX(str1):
        stringu = ""
        for index, char in enumerate(str1):  
            stringu += ("Karakteri: " + str(char) + " indexi " + str(index) + "\n")
        conS.send((stringu).encode('ASCII'))
    def DEGREES()
           radian = float(opsioni)*(pi/180)
           conS.send(str(str(radian)).encode('ASCII'))
