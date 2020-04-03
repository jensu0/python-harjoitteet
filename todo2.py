tehtavat = []
try:
    tiedosto = open('todo.txt' , 'r')
    while True:
        rivi = tiedosto.readline()
        if len(rivi)==0:
            break
        lisays = rivi.strip()
        tehtavat.append(lisays)  #nyt tehtavat=['rivi1' , 'rivi2',..]
        tiedosto.close
except IOError:
    pass



for i in range(0,len(tehtavat)):
        print str(i) + ' ' + tehtavat[i]

while True:
    tehtavat = []
    try:
        tiedosto = open('todo.txt' , 'r')
        while True:
            rivi = tiedosto.readline()
            if len(rivi)==0:
                break
            lisays = rivi.strip()
            tehtavat.append(lisays)  #nyt tehtavat=['rivi1' , 'rivi2',..]
            tiedosto.close
    except IOError:
        pass

    

    print '----'
    print '1. add'
    print '2. do'
    print 'enter quits'

    paatos=raw_input('Give choice: ')
    if paatos == '':
        break

    elif int(paatos) == 1:
        homma = raw_input('Give todo: ')
        tehtavat.append(homma)
        #print tehtavat
        tiedosto = open('todo.txt' , 'w')
        for i in range(0,len(tehtavat)):
            kirjoita = tehtavat[i] + '\n'
            tiedosto.write(kirjoita)
        tiedosto.close()
        for i in range(0,len(tehtavat)):
            print str(i) + ' ' + tehtavat[i]




    elif int(paatos) == 2:
        numero = raw_input('Give index: ')
        if numero.isdigit() != True:
            print "Give an index!"
            for i in range(0,len(tehtavat)):
                print str(i) + ' ' + tehtavat[i]
            
        elif int(numero) > len(tehtavat):
            print "No such index " + numero
            for i in range(0,len(tehtavat)):
                print str(i) + ' ' + tehtavat[i]
            
        else:
            poistettava = tehtavat[int(numero)]
            tehtavat.remove(poistettava)
            for i in range(0,len(tehtavat)):
                print str(i) + ' ' + tehtavat[i]
            tiedosto = open('todo.txt' , 'w')
            for i in range(0,len(tehtavat)):
                kirjoita = tehtavat[i] + '\n'
                tiedosto.write(kirjoita)
