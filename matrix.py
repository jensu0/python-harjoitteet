# -*- coding: cp1252 -*-
import sys



def lue_tiedosto(tiedosto):
    tietosto = open(tiedosto, 'r')
    matriisi = []
    while True:
        a = tietosto.readline() #lukee rivin tiedostosta 1
        rivit = a.strip('\n')
        if len(rivit) == 0:
            break
        #print ekanrivit
        else:
            matriisi.append(rivit) #ekamatriisi on lista [rivi1,rivi2,..]

    tietosto.close()
    


    loppumatriisi = []
    for j in range(0,len(matriisi)): #rivi arvoilla rivi1, j=0 ... 
        rivi = []
        b = matriisi[j].split(' ') #a on ekamatriisi[0] eli rivi1
        loppumatriisi.append(b)
        #for i in range(0,len(b)): #i arvoilla yhden rivin pituus, i=0
            #rivi.append = b[i]
        #print b
    
    #print loppumatriisi
    return loppumatriisi


try:
    eka = lue_tiedosto(sys.argv[1])
    toka = lue_tiedosto(sys.argv[2])
except IOError:
    print "Wrong amount of parameters!"
    

else:
    tulos = []


    if len(sys.argv) != 3:
        print "Wrong amount of parameters!"
        
    elif len(eka) != len(toka):
        print "Dimensions do not match!"

    elif len(eka[0]) != len(toka[0]):
       print "Dimensions do not match!"

    else:
        for rivi in range(0, len(eka)): #rivi 0-<
            tulosrivi = []
            for sarake in range(0,len(eka[0])):
                summa = int(eka[rivi][sarake]) + int(toka[rivi][sarake])
                tulosrivi.append(summa)
            tulos.append(tulosrivi)


        for rivi in range(0, len(tulos)):
            for sarake in range(0, len(tulos[0])):
                sys.stdout.write(str(tulos[rivi][sarake]))

                ##JAAKKO LISÄSI TUTKI VIELÄ ;D
                if sarake < len(tulos[0]) -1:
                    sys.stdout.write(" ")
                #print tulos[rivi][sarake],
            #print '\n',
            sys.stdout.write('\n')


        
