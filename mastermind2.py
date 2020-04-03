# -*- coding: cp1252 -*-
import sys

def onkiva(lukujono):
    oliko=True
    for i in range(0,4):
        if int(lukujono[i]) > 6:
            oliko=False
    return oliko



argumenttiok = False
if len(sys.argv) == 2:
    if sys.argv[1].isdigit() == True:
        if len(sys.argv[1]) == 4:
            if onkiva(sys.argv[1]):
                argumenttiok = True
            
            else:
                print "Invalid symbol! Use numbers between 1-6!"

    

        else:
            print "Use 4 symbols!"
    else:
        print "Invalid symbol! Use numbers between 1-6!"

else:
    print "Give secret code" #"Invalid symbol! Use numbers between 1-6!"



def tarkistus(parametri,arvaus):
    parametrit=[]
    arvaukset=[]

    for i in range(0,4):
        parametrit.append(parametri[i])
        arvaukset.append(arvaus[i])

    for j in range(0,4):
        if parametri[j] == arvaus[j]:
            print "Symbol in correct position"
            parametrit[j]=7
            arvaukset[j]=8

    for j in range(0,4):
        for i in range(0,4):
            if parametrit[j] == arvaukset[i]:
                print "Correct symbol"
                parametrit[j]=7
                arvaukset[i]=8


        
while argumenttiok:
    
    arvaus = raw_input("Give guess: ")
    if arvaus == "lopu":
        break
        
    
    if arvaus.isdigit() == True:
        if len(arvaus) == 4:
            if onkiva(arvaus):
                
                if arvaus == sys.argv[1]:
                    print "You win!"
                    print "the correct answer was " + arvaus
                    break
                
                else:
                    tarkistus(sys.argv[1],arvaus)
                                
                            
    
                                
            else:
                print "Invalid symbol! Use numbers between 1-6!"

        else:
            print "Use 4 symbols!"
    else:
        print "Invalid symbol! Use numbers between 1-6!"
