# -*- coding: cp1252 -*-

print "Numbers"

tiedot = {}

while True:
        nimi=raw_input("Give name: ")
        if nimi == "": #jos nimi on tyhjä, lopeta
            break
        else:
            numero=int(raw_input("Give number: "))
            tiedot[nimi] = numero            
            print "Numbers"
            for avain, arvo in tiedot.items():
                print "%s %s" %(avain, arvo) 
                jutut = nimi + str(numero)
               
