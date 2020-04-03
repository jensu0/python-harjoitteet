# -*- coding: cp1252 -*-
import sys

ekatiedosto = open(sys.argv[1], 'r')
while True:
    ekamatriisi = []
    ekanrivit = ekatiedosto.readline() #lukee rivin tiedostosta 1
    if len(ekanrivit) == 0:
        break
    else:
        ekamatriisi.append(ekanrivit) #ekamatriisi on lista [rivi1,rivi2,..]

#pitäsi saada ekamatriisi on [[rivi1] , [rivi2], ...]

for j in range(0,len(ekamatriisi)): #rivi arvoilla rivi1, j=0 ... 
    rivi = []
    a = ekamatriisi[j] #a on ekamatriisi[0] eli rivi1
    for i in range(0,len(a)): #i arvoilla yhden rivin pituus, i=0
        rivi.append = a[i] #  rivi = ['rivi1:n eka numero'];rivi=['rivi1:n eka numero', 'rivi 1:n toka numero']

tokatiedosto = open(sys.argv[2], 'r')
while True:
    tokamatriisi = []
    tokanrivi = tokatiedosto.readline()
    if len(tokanrivi) == 0:
        break
    else:
        tokamatriisi.append(tokanrivi) #tokamatriisi on lista [rivi2,rivi2,..]

for j in range(0,len(tokamatriisi)):  
    rivi = []
    a = tokamatriisi[j] 
    for i in range(0,len(a)):
        rivi.append = a[i] 

# nyt pitäis olla matriisit [[a,b,c],[d,e,f], jne]
print ekamatriisi
print tokamatriisi

summamatriisi = []
for k in range(0,len(ekamatriisi)):
    ekarivi = intekamatriisi[k] #esim ekarivi=[1,2,3]
    tokarivi = tokamatriisi[k] #esim tokarivi=[4,5,6]
    summarivi = []
    for l in range(len(ekarivi)):
        ekalaskettava = int(ekarivi[l]) #esim 1
        tokalaskettava = int(tokarivi[l]) #esim 4
        summa = ekalaskettava + tokalaskettava
        summarivi.append(summa)
        #print summarivi
    summamatriisi.append(summarivi)

print summamatriisi
