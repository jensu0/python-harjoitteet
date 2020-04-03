# -*- coding: cp1252 -*-
luettelo = open('phoneboook.txt', 'w')

print "Numbers"

tiedot = {}

while True:
        nimi=raw_input("Give name: ")
        if nimi == "": #jos nimi on tyhjä, lopeta
            break
        else:
            numero=raw_input("Give number: ")
            tiedot[nimi] = numero            
            print "Numbers"
            jutut = nimi + ", " + numero + "\n"
            luettelo.write(jutut)
            for avain, arvo in tiedot.items():
                print "%s %s" %(avain, arvo) 
                
                

luettelo.close

        
