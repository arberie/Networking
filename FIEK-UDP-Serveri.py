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
    def KONVERTO():
        if(opsioni=="CelsiusToKelvin"):
              shkalla = 273.16+int(numer)
              serverSocket.sendto(str(str(numer)+" Celsius = "+ str(shkalla)+" Kelvin").encode('utf-8'), clientAddress)
        elif(opsioni=="CelsiusToFahrenheit"):
              shkalla = (9*float(numer)/5)+32
              serverSocket.sendto(str(str(numer)+" Celsius = "+ str(shkalla)+" Farenhajt").encode('utf-8'), clientAddress)
        elif(opsioni=="KelvinToFarenheit"):
              shkalla = 1.8*(float(numer)-273)+32
              serverSocket.sendto(str(str(numer)+" Kelvin = "+ str(shkalla)+" Farenhajt").encode('utf-8'), clientAddress)
        elif(opsioni=="KelvinToCelsius"):
              shkalla = float(numer)-273.15
              serverSocket.sendto(str(str(numer)+" Kelvin = "+ str(shkalla)+" Celsius").encode('utf-8'), clientAddress)
        elif(opsioni=="FahrenheitToCelsius"):
              shkalla = 5*(float(numer)-32)/9 
              serverSocket.sendto(str(str(numer)+" Farenhight = "+ str(shkalla)+" Celsius").encode('utf-8'), clientAddress)
        elif(opsioni=="FahrenheitToKelvin"):
              shkalla = 5*(float(numer)-32)/9
              serverSocket.sendto(str(str(numer)+" Farenhight = "+ str(shkalla)+" Kelvin").encode('utf-8'), clientAddress)
        elif(opsioni=="PoundToKilogram"):
              shkalla= float(numer)*0.45359237
              serverSocket.sendto(str(str(numer)+" Pound = "+ str(shkalla)+" Kilogram").encode('utf-8'), clientAddress)
        elif(opsioni=="KilogramToPound"):
              shkalla = float(numer)*2.204622621
              serverSocket.sendto(str(str(numer)+" Kilogram = "+ str(shkalla)+" Pound").encode('utf-8'), clientAddress)
