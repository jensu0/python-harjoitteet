# -*- coding: cp1252 -*-
try:
    luettelo=open("phonebook.txt" , "r")

    print "Numbers"

    tulostetaan = {}

    while True:
        rivi = luettelo.readline()  #lukee rivit
        if len(rivi) == 0:             #jos rivi tyhjä lopetetaan 
            break
        else:
            valitpois = rivi.strip( )  #poistaa välit
            pilkutpois = valitpois.split(',')  #muuttaa listaksi [nimi,numero]
            tulostetaan[pilkutpois[0]] = pilkutpois[1] 
    for avain, arvo in tulostetaan.items():
        print "%s %s" %(avain, arvo)     
    
        
    luettelo.close()

except:
    print "No file!"
