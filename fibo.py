# -*- coding: cp1252 -*-
a=int(raw_input("Give amount: "))

if a==1:
    print [0]
elif a==2:
    print [0,1]

else:
    luvut = [0,1] #kaksi ekaa lukua
    i=2 #kolmas luku
    while i < a: #luvun järjestysnumero pienempi kuin raw_input
        lisattava = luvut[i-2]+luvut[i-1] #uusi numero on kahen edellisen summa
        luvut.append(lisattava)
        i=i+1

    print luvut
