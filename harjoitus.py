# -*- coding: cp1252 -*-
x='x'
t=' '

lauta=[[t,t,t,x,x,x,t,t,t],\
       [t,t,t,x,x,x,t,t,t],\
       [t,t,t,x,x,x,t,t,t],\
       [x,x,x,x,x,x,x,x,x],\
       [x,x,x,x,0,x,x,x,x],\
       [x,x,x,x,x,x,x,x,x],\
       [t,t,t,x,x,x,t,t,t],\
       [t,t,t,x,x,x,t,t,t],\
       [t,t,t,x,x,x,t,t,t]]


#Funktio, joka tulostaa pelilaudan
def tulostalauta(lautaf):
    print "  0 1 2 3 4 5 6 7 8"     #printtaa ylös sarakenumerot
    for i in range(0,9):            #i:n eli rivin arvoilla 0-8
        print i,                    #printtaa sivuun rivinumerot
        for j in range(0,9):        #j:n eli sarakkeen arvoilla 0-8
            print lautaf[i][j],     #printtaa laudalta i:nnen listan j:nnen alkion
        print '\n',                 #printtaa uuden rivin


#tarkastaa, että annetut rivin ja sarakkeen arvot ovat ok
def tarkastasiirto(rivif,sarakef,lautaf): 
    if rivif.isdigit() == True:                                         #onhan rivin arvo numero
        if (int(rivif) >= 0) and (int(rivif) <= 8):                     #ja välillä 0-8
            if sarakef.isdigit() == True:                               #onhan sarakkeen arvo numero
                if (int(sarakef) >= 0) and (int(sarakef) <= 8):         #ja välillä 0-8
                    if lautaf[int(rivif)][int(sarakef)] != t:           #laudan alkio (rivif,sarakef) ei
                        return True                                     #jos kaikki ok, funktion arvo True
                           
                    else:                                               #jos alkio on t, funktio False
                        print "Et ole pelilaudalla"
                        return False
                else:                                                   #jos sarake ei ole välillä 0-8
                   print "Sarakkeen täytyy olla numero väliltä 0-8!"    #funktio False
                   return False
            else:                                                       #jos sarake ei ole numero
               print "Sarakkeen täytyy olla numero väliltä 0-8!"        #funktio False
               return False
        else:                                                           #jos rivi ei ole välillä 0-8
            print "Rivin täytyy olla numero väliltä 0-8!"               #funktio False
            return False
    else:                                                               #jos rivi ei ole numero
        print "Rivin täytyy olla numero väliltä 0-8!"
        return False


#Tarkastaa, että annettu suunnan arvo on ok
#Tarkoitus käyttää numpadin näppäimiä
def tarkastasuunta(rivif,sarakef,suuntaf,lautaf):
    if suuntaf.isdigit() == True:                                       #onhan suunnan arvo numero
        if (int(suuntaf)==1) or (int(suuntaf)==2) or (int(suuntaf)==3) or(int(suuntaf)==5):
            return True                                                 #jos suunta on 1,2,3,tai 5
        else:                                                           #funktio True 
            print "Suunta ei kelpaa!"                                   #muuten ei hyvä
    else:                                                               #jos suunnaksi annetaan kirjaimia
        print "Suunta ei kelpaa!"                                       #funktion arvo False
        return False


#funktio, joka muuntaa tarvittavat alkiot x:ksi tai 0:ksi
def siirra(rivif,sarakef,suuntaf,lautaf):
    if (int(suuntaf) == 5):                                         #jos suunta=5 eli ylös
        if lautaf[int(rivif)-2][int(sarakef)]==0:                   #jos lopussa(=kaksi riviä ylempänä) on 0
            if lautaf[int(rivif)][int(sarakef)]==x:                 #ja alussa(=samassa kohdassa) x
                if lautaf[int(rivif)-1][int(sarakef)]==x:           #ja välissä(=riviä ylempänä) x
                    lautaf[int(rivif)-2][int(sarakef)]=x            #muutetaan loppu x:ksi
                    lautaf[int(rivif)][int(sarakef)]=0              #ja alku 0:ksi
                    lautaf[int(rivif)-1][int(sarakef)]=0            #ja välissä oleva 0:ksi
                else:
                    print "Ei pysty siirtämään"                     #muuten virhe
            else:
               print "Ei pysty siirtämään"
        else:
            print "Ei pysty siirtämään"
        
    elif (int(suuntaf) == 2):                                       #jos suunta=2 eli alas
        if lautaf[int(rivif)+2][int(sarakef)]==0:
            if lautaf[int(rivif)][int(sarakef)]==x:     
                if lautaf[int(rivif)+1][int(sarakef)]==x:
                    lautaf[int(rivif)+2][int(sarakef)]=x
                    lautaf[int(rivif)][int(sarakef)]=0  
                    lautaf[int(rivif)+1][int(sarakef)]=0
                else:
                    print "Ei pysty siirtämään"                                        
            else:
                print "Ei pysty siirtämään"
        else:
            print "Ei pysty siirtämään"
       
    elif (int(suuntaf) == 3):                                       #jos suunta=3 eli oikelle
        if lautaf[int(rivif)][int(sarakef)+2]==0:
            if lautaf[int(rivif)][int(sarakef)]==x:
                if lautaf[int(rivif)][int(sarakef)+1]==x:
                   lautaf[int(rivif)][int(sarakef)+2]=x
                   lautaf[int(rivif)][int(sarakef)]=0
                   lautaf[int(rivif)][int(sarakef)+1]=0
                else:
                    print "Ei pysty siirtämään"
            else:
               print "Ei pysty siirtämään"
        else:
           print "Ei pysty siirtämään"
        

    elif (int(suuntaf) == 1):                                       #jos suunta=1 eli vasemmalle
        if lautaf[int(rivif)][int(sarakef)-2]==0:
            if lautaf[int(rivif)][int(sarakef)]==x:
                if lautaf[int(rivif)][int(sarakef)-1]==x:
                    lautaf[int(rivif)][int(sarakef)-2]=x
                    lautaf[int(rivif)][int(sarakef)]=0
                    lautaf[int(rivif)][int(sarakef)-1]=0
                else:
                    print "Ei pysty siirtämään"
            else:
                print "Ei pysty siirtämään"
        else:
            print "Ei pysty siirtämään"

#Funktio tarkistaa, onko jäljellä siirtoja.
#Käy läpi kaikki alkiot yksitellen, ja tarkastaa, onko ylös,alas,vasemmalle
#tai oikealle päin yhdistelmää xx0.
#Ehdot i<7, i>2, j<7 ja j>2 estävät IndexErroria.
#Jos ainakin yhdestä alkiosta löytyy ainakin yksi siirto, funktion arvoksi tulee True.
def onkosiirtoja(lautaf):
    for i in range(0,9):                                             
        for j in range(0,9):                                        
            if ((i<7) and lautaf[i][j]==x) and (lautaf[i+1][j]==x) and (lautaf[i+2][j]==0): 
                return True                                         
            elif ((i>2) and lautaf[i][j]==x) and (lautaf[i-1][j]==x) and (lautaf[i-2][j]==0): 
                return True
            elif ((j<7) and lautaf[i][j]==x) and (lautaf[i][j+1]==x) and (lautaf[i][j+2]==0):
                return True
            elif ((j>2) and lautaf[i][j]==x) and (lautaf[i][j-1]==x) and (lautaf[i][j-2]==0):               
                return True
            else:
                continue

#Pelin suoritus               
while True:
    tulostalauta(lauta)                                             #Tulostaa laudan    
    rivi=raw_input('Anna rivi: ')                                   #Kysyy riviä
    sarake=raw_input('Anna sarake: ')                               #Kysyy saraketta
    suunta=raw_input('Ylös:5, Alas:2, Oikealle:3, Vasemmalle:1. ')  #Kysyy suuntaa
    if tarkastasiirto(rivi,sarake,lauta)==True:                     #jos rivin ja sarakkeen arvot ok
        if tarkastasuunta(rivi,sarake,suunta,lauta)==True:          #ja suunnan arvo ok
            try:                                                    #suorittaa siirra-funktio
                siirra(rivi,sarake,suunta,lauta)
            except IndexError:                                      #paitsi jos menee laudan yli
                print "Ei pysty siirtämään"                         #tulee virhe
        else:                                                       
            pass                                                    #jos suunta ei ole ok, jatka
    else:                                                           #jos rivin ja sarakkeen arvot ei ok
        pass                                                        #jatka
    if onkosiirtoja(lauta)==True:                                   #testaa, onko siirtoja jäljellä    
        continue                                                    #jos on, aloita while alusta
    else:                                                           #jos ei, lopeta peli
        break

tulostalauta(lauta)                                                 #tulosta lauta vielä kerran
print "Peli loppui"

