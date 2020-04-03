# -*- coding: cp1252 -*-
import sys

if len(sys.argv) == 1:
    print "Give secret code"
    
elif len(sys.argv[1]) != 4:
    print "Use 4 symbols!"


#elif True:
 #   for i in range(0,4):
  #      if int(sys.argv[i]) > 6:
   #         print "Invalid symbol! Use numbers between 1-6!"
    #        break
     #   else:
      #      continue


while True:
    
    arvaus = raw_input("Give guess: ")

    if len(arvaus) != 4:
        print "Use 4 symbols!"

    if arvaus == "lopu":
        break

    elif arvaus.isdigit() != True:
        print "Invalid symbol! Use numbers between 1-6!"
    
    elif True:
        for i in range(0,4):
            if int(arvaus[i]) > 6:
              print "Invalid symbol! Use numbers between 1-6!"
                
            else:
                pass

    
    elif arvaus == sys.argv[1]:
        print "You win!"
        print "the correct answer was " + arvaus
        break

    else:
        #print "kukkuu"
        for i in range(0,4): #i=0 
            if arvaus[i] == sys.argv[1][i]: #ekat samat
                print "Symbol in correct position"
                
            for j in range(0,4): #j=0 #j=1
                if j == i: #pass, j->j=1
                    pass
                elif arvaus[i] == sys.argv[1][j]: #i=0,j=1 #
                    print "Correct symbol"
    
