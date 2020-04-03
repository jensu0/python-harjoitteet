# -*- coding: cp1252 -*-

def mastermind_logiikka(numero,arvaus):
    numero_lista=[] #numerot listassa
    arvaus_lista=[] #arvaukset listassa


    
    for arvaus_n in range(0,len(arvaus)):
        numero_lista.append(numero[arvaus_n]) #tallenna listaan stringin merkit
        arvaus_lista.append(arvaus[arvaus_n])


    #testaa 1:1 oikein osuneet
    for numero_n in range(0,len(numero)):
        if numero[numero_n] == arvaus[numero_n]:
            print "Symbol in correct position" #1:1 luku l�ydetty tulosta info ja merkkaa l�ydetyksi
            numero_lista[numero_n]=7 #merkkaa numero listaan ett� l�ydetty
            arvaus_lista[numero_n]=8 #merkkaa arvaus listaan

    #testaa j�ljell� olevat arvaamattomat numerot arvauksen perusteella
    for numero_n in range(0,len(numero)):
        for arvaus_n in range (0,len(arvaus)):
            if numero_lista[numero_n]==arvaus_lista[arvaus_n]:
                print "Correct symbol" #huti mennyt oikea luku l�ytyi merkkaa pari "k�ytetyksi"
                numero_lista[numero_n]=7
                arvaus_lista[arvaus_n]=8


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
