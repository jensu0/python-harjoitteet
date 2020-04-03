# -*- coding: cp1252 -*-

def mastermind_logiikka(numero,arvaus):
    numero_maski=[] #maski arvattuja numeroita varten
    arvaus_maski=[] #maski arvattuja arvauksia varten wut?
    
    #muuta numero listaksi... (oma rautalanka patentti)
    #toimii jos osaat päivittää
    #ton numeron numeroita jotenki kätevästi
    for arvaus_n in range(0,len(arvaus)):
        numero_maski.append(numero[arvaus_n])
        arvaus_maski.append(arvaus[arvaus_n])


    #testaa 1:1 oikein osuneet
    for numero_n in range(0,len(numero)):
        if numero[numero_n] == arvaus[numero_n]:
            print "Symbol in correct position"
            numero_maski[numero_n]=7 #päivitä numeron maski
            arvaus_maski[numero_n]=8 #päivitä arvattu maski

    #testaa jäljellä olevat arvaamattomat numerot arvauksen perusteella
    for numero_n in range(0,len(numero)):
        for arvaus_n in range (0,len(arvaus)):
            if numero_maski[numero_n]==arvaus_maski[arvaus_n]: #jos arvaamaton luku == arvaamaton arvaus? WUT :D noh kuitenki
                print "Correct symbol"
                numero_maski[numero_n]=7
                arvaus_maski[arvaus_n]=8
        

print "1253 & 1234"
mastermind_logiikka("1253","1234")
print "1253 & 1255"
mastermind_logiikka("1253","1255")
print "1253 & 1252"
mastermind_logiikka("1253","1252")
print "5445 & 4554"
mastermind_logiikka("5445","4554")
print "5445 & 4545"
mastermind_logiikka("5445","4545")
print "5445 & 5454"
mastermind_logiikka("5445","5454")
print "5554 & 1121"
mastermind_logiikka("5554","1121")
print "5554 & 2345"
mastermind_logiikka("5554","2345")
print "5554 & 2345"
mastermind_logiikka("5554","2345")
print "5554 & 1154"
mastermind_logiikka("5554","1154")
