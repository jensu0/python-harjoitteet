
import sys

lopputulos = ""

if len(sys.argv) == 2 :

        sana = sys.argv[1]
        sanaon = []
        nimion=[]

        for i in range(len(sana) - 1, -1, -1):
                kirjain = sana[i]
                sanaon.append(kirjain)

        for a in range(0, len(sana)):
               lopputulos=lopputulos+str(sanaon[a])
        print lopputulos

else:
        print "Wrong amount of parameters!"
