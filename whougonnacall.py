# -*- coding: cp1252 -*-


print "Numbers"

nimet=[]
numerot=[]

while True:
    nimi=raw_input("Give name: ")
    if nimi == "": #jos nimi on tyhj�, lopeta
        break
    else:
        nimet.append(nimi) #lis�� nimi listaan nimet
        numero=raw_input("Give number: ")
        numerot.append(numero) #lis�� numero listaaan numerot
        print "Numbers"
        for i in range(len(nimet)-1,-1,-1): #1:len=1, i=1
            #print i-1
        
            print nimet[i] + " " + numerot[i]
