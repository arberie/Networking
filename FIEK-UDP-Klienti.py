import socket
serverName = '192.168.0.15'
serverPort = 9000

print('Serveri eshte ne linje...')
print('')
print('Metodat e mundshme: ')
print('IP - \t\tkthen  IP adresen e klientit')
print('PORT - \t\tkthen protin e klientit') 
print('ZANORE - \tkthen numrin e zanoreve ne nje fjale') 
print('PRINTO - \tkthen fjaline e derguar') 
print('HOST - \t\tkthen emrin e hostit') 
print('TIME- \t\tkthen kohen aktuale ne server') 
print('KENO - \t\tkthen 20 numra nga rangu[1,80]') 
print('FAKTORIEL - \tgjen faktorielin e parametrit hyres')
print('KONVERTO - \tkthen si rezultat konvertimin e opioneve varesisht opsionit te zgjedhur: \n\t\t\tCelsiusToKelvin\n\t\t\tCelsiusToFarenheit\n\t\t\tKelvinToFarenheit\n\t\t\tKelvinToCelsius\n\t\t\tFarenheitToCelcius\n\t\t\tFarenheitToKelvin\n\t\t\tPoundToKilogram\n\t\t\tKilogramToPound')
print('KODI - \t\tenkripton fjaline e shenuar sipas kodit te Cezarit')
print('PRIMAR - \ttregon nese numri i shenuar eshte numer i thjeshte')
print('Siperfaqja - \tkalkulon siperfaqen e rrethit me rrezen e dhene')
print('Perimetri - \tkalkulon perimetrin e rrethit me rrezen e dhene')
print('ASTRO - \ttregon shenjen e horoskopit ne baze te datelindjes')
print('GJATESIA - \ttregon gjatesine e tekstit te dhene')
print('ODD - \t\tshtyp shkronjat me index cift')
print('BINARY - \tkthen numrin e dhene binar ne numer decimal')
print('INDEX - \ttregon indeksat dhe shkronjat perkatese te nje teksti te dhene')
print('DEGREES -\tshnderron shkallet e dhena ne radian')


while True:
    sentence= input('Shkruani njeren nga komandat e larteshenuara!')
    if sentence=="":
        print('There is nothing here')
    else:
        clientS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientS.sendto(sentence.encode("ASCII"),(serverName, serverPort))
        ReturnedText = clientS.recv(128).decode("UTF-8")
        print (ReturnedText)
