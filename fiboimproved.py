# -*- coding: cp1252 -*-
a=raw_input("Give amount: ")


if a.isdigit() == False:
    print "Give an integer!"

elif int(a) <= 0:
    print "Nothing to do!"

elif int(a) == 1:
    print [0]
    
else:
    luvut = [0,1] #kaksi ekaa lukua
    i=2 #kolmas luku
    while i < int(a): #luvun järjestysnumero pienempi kuin raw_input
        lisattava = luvut[i-2]+luvut[i-1] #uusi numero on kahen edellisen summa
        luvut.append(lisattava)
        i=i+1


    print luvut
