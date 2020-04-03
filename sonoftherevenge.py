# -*- coding: cp1252 -*-
luettelo=open("phonebook.txt" , "r")

print "Numbers"

tulostetaan = {}

while True:
    rivi = luettelo.readline()  #lukee rivit
    if len(rivi) == 0:             #jos rivi tyhj� lopetetaan 
        break
    else:
        valitpois = rivi.strip()  #poistaa v�lit
        pilkutpois = valitpois.split(',')  #muuttaa listaksi [nimi,numero]
        numero = int(pilkutpois[1]) 
        nimi = pilkutpois[0]
        tulostetaan[nimi] = numero  #lis�t��n sanakirjaan
for avain, arvo in tulostetaan.items(): #tulostetaan sanakirja
    print "%s %s" %(avain, arvo) 

luettelo.close()

luettelo=open("phonebook.txt" , "w") #avataan kirjoitettavaksi



while True:
        nimi=raw_input("Give name: ") #anna nimi
        if nimi == "": #jos nimi on tyhj�, lopeta
            break
        else:
            numero=raw_input("Give number: ")  #muuten anna numero
            tulostetaan[nimi] = numero   #lis�t��n nimi ja numero sanakirjaan
            print "Numbers"  
            for avain, arvo in tulostetaan.items(): #tulosta sanakirja
                print "%s %s" %(avain, arvo) 

for avain, arvo in tulostetaan.items():
    jutut = "%s, %s\n" %(avain,arvo) #tiedoston teksti
    luettelo.write(jutut)

luettelo.close()
