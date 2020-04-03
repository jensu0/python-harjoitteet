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


def tulostalauta(lautaf):
    print "  0 1 2 3 4 5 6 7 8"     #printtaa ylös sarakenumerot
    for i in range(0,9):            
        print i,                    #printtaa sivuun rivinumerot
        for j in range(0,9):
            print lautaf[i][j],
        print '\n',


#tarkastaa, että rivin ja sarakkeen arvot ovat ok
def tarkastasiirto(rivif,sarakef,lautaf,alkio): 
    if rivif.isdigit() == True:
        if (int(rivif) >= 0) and (int(rivif) <= 8):
            if sarakef.isdigit() == True: 
                if (int(sarakef) >= 0) and (int(sarakef) <= 8):
                    if lautaf[int(rivif)][int(sarakef)] != alkio:
                        return True
               
                    else:
                        print "Et ole pelilaudalla"
                        return False
                else:
                   print "Sarakkeen täytyy olla numero väliltä 0-8!"
                   return False
            else:
               print "Sarakkeen täytyy olla numero väliltä 0-8!"
               return False
        else:
            print "Rivin täytyy olla numero väliltä 0-8!"
            return False
    else:
        print "Rivin täytyy olla numero väliltä 0-8!"
        return False


#tarkastaa, että suunta ei ole höpönpöppöä
def tarkastasuunta(rivif,sarakef,suuntaf,lautaf):
    if suuntaf.isdigit() == True:
        if (int(suuntaf)==1) or (int(suuntaf)==2) or (int(suuntaf)==3) or(int(suuntaf)==5):
            return True
        else:
            print "Suunta ei kelpaa!"
    else:
        print "Suunta ei kelpaa!"
        return False



def siirra(rivif,sarakef,suuntaf,lautaf):
    if (int(suuntaf) == 5):
        if lautaf[int(rivif)-2][int(sarakef)]==0:                   #jos lopussa on 0
            if lautaf[int(rivif)][int(sarakef)]==x:                 #ja alussa x
                if lautaf[int(rivif)-1][int(sarakef)]==x:           #ja välissä x
                    lautaf[int(rivif)-2][int(sarakef)]=x            #muutetaan loppu x:ksi
                    lautaf[int(rivif)][int(sarakef)]=0              #ja alku 0:ksi
                    lautaf[int(rivif)-1][int(sarakef)]=0            #ja välissä oleva 0:ksi
                else:
                    print "Ei pysty siirtämään"
            else:
               print "Ei pysty siirtämään"
        else:
            print "Ei pysty siirtämään"
        


    elif (int(suuntaf) == 2):
        if lautaf[int(rivif)+2][int(sarakef)]==0:           #jos loppusiirto on 0
            if lautaf[int(rivif)][int(sarakef)]==x:         #jos alkukohta on x     
                if lautaf[int(rivif)+1][int(sarakef)]==x:
                    lautaf[int(rivif)+2][int(sarakef)]=x        #muutetaan loppu x:ksi
                    lautaf[int(rivif)][int(sarakef)]=0          #ja alku 0:ksi
                    lautaf[int(rivif)+1][int(sarakef)]=0
                else:
                    print "Ei pysty siirtämään"                                        
            else:
                print "Ei pysty siirtämään"
        else:
            print "Ei pysty siirtämään"
       
    elif (int(suuntaf) == 3):
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
        

    elif (int(suuntaf) == 1):
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
                
while True:
    tulostalauta(lauta)
    rivi=raw_input('Anna rivi: ')
    sarake=raw_input('Anna sarake: ')
    suunta=raw_input('Ylös:5, Alas:2, Oikealle:3, Vasemmalle:1. ')
    if tarkastasiirto(rivi,sarake,lauta,t)==True:
        if tarkastasuunta(rivi,sarake,suunta,lauta)==True:
            try:
                siirra(rivi,sarake,suunta,lauta)
            except IndexError:
                print "Jouduit ulos pelilaudalta"
        else:
            pass
    else:
        pass
    if onkosiirtoja(lauta)==True:
        continue
    else:
        break

tulostalauta(lauta)
print "Peli loppui"

