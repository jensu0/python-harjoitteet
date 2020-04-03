

tehtavat = []
while True:
    try:
        print file('todo.txt').read()   #lue ja tulosta
    except:
        pass
    print "----"
    print "1. add\n2. do"
    print "enter quits"
    paatos = raw_input("Give choice: ")

    if paatos == "":
        break


    elif int(paatos) == 1:
        tehtava = raw_input("Give todo: ")   
        tehtavat.append(tehtava)            #lisaa listaan tehtavat
        for i in range(len(tehtavat)):      #printtaa numero + tehtava
            print str(i) + ' ' + tehtavat[i]
        todolista = open('todo.txt' , 'a')
        todolista.write(tehtava + '\n')
        todolista.close()
   
    elif int(paatos) == 2:
        index = int(raw_input("Give index: "))
        lista = open('todo.txt' , 'r')
        rivi = lista.readline(index)
        

