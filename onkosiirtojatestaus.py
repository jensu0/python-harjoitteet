# -*- coding: cp1252 -*-

x='x'
t=' '
lautaf=[[t,t,t,x,x,x,t,t,t],\
       [t,t,t,x,x,x,t,t,t],\
       [t,t,t,x,x,x,t,t,t],\
       [x,x,x,x,x,x,x,x,x],\
       [x,x,x,x,0,x,x,x,x],\
       [x,x,x,x,x,x,x,x,x],\
       [t,t,t,x,x,x,t,t,t],\
       [t,t,t,x,x,x,t,t,t],\
       [t,t,t,x,x,x,t,t,t]]


def tarkista(uusix,uusiy,merkki,kartta):
    kartanleveys=9-1
    kartankorkeus=9-1
    if uusix > kartanleveys:
        return False
    if uusix < 0:
        return False
    if uusiy > kartankorkeus:
        return False
    if uusiy < 0:
        return False
    if (kartta[uusiy][uusix]==merkki):
        return True
    

siirtoja = 0
for i in range(0,9):
    for j in range(0,9):
        if ((i<7) and lautaf[i][j]==x) and (lautaf[i+1][j]==x) and (lautaf[i+2][j]==0):
            
            print "on siirtoja a rivi"+ str(i) + 'sarake' + str(j)
            siirtoja = siirtoja + 1 
            
        elif ((i>2) and lautaf[i][j]==x) and (lautaf[i-1][j]==x) and (lautaf[i-2][j]==0):
            
            print "on siirtoja y rivi"+ str(i) + 'sarake' + str(j)
            siirtoja = siirtoja + 1 
            
        elif ((j<7) and lautaf[i][j]==x) and (lautaf[i][j+1]==x) and (lautaf[i][j+2]==0):
            
            print "on siirtoja o rivi"+ str(i) + 'sarake' + str(j)
            siirtoja = siirtoja + 1 
            
        elif ((j>2) and lautaf[i][j]==x) and (lautaf[i][j-1]==x) and (lautaf[i][j-2]==0):
            
            print "on siirtoja v rivi"+ str(i) + 'sarake' + str(j)
            siirtoja = siirtoja + 1 
            
        else:
            
            print "ei siirtoja" + str(i) + str(j)

print "siirtoja jäljellä " + str(siirtoja) +" kpl"
