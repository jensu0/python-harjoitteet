
def kirjoitakirje(i):
    nimilista = open('potential-customers.txt' , 'r')
    nimet = []

    while True:
        a = nimilista.readline()

        if len(a) == 0:
            break

        else:
            name = []
            b = a.strip('\n ')
            nimi = b.split(' ')
            etunimi = nimi[0]
            sukunimi = nimi[1]  
            name.append(etunimi)
            name.append(sukunimi)
        nimet.append(name)   #nyt nimet=[['Erkki', 'Esimerkki'], ['Aimo', 'Assar..]

    nimilista.close()

    

    kirje = open('letter-template.txt' , 'r')
    letter = ""
    while True:
        b = kirje.readline()
        if len(b) == 0:
            break

        else:
            letter = letter + str(b)

    kirje.close()



    valmiskirje = open('letter000' + str(i+1) + '.txt' , "w")
    etunimi = nimet[i][0]
    sukunimi = nimet[i][1]
    letter=letter.replace('FIRST_NAME',etunimi)
    letter=letter.replace('LAST_NAME',sukunimi)
    valmiskirje.write(letter)
    valmiskirje.close()



nimilista = open('potential-customers.txt' , 'r')
nimet = []

while True:
    a = nimilista.readline()

    if len(a) == 0:
        break

    else:
        name = []
        b = a.strip('\n ')
        nimi = b.split(' ')
        etunimi = nimi[0]
        sukunimi = nimi[1]  
        name.append(etunimi)
        name.append(sukunimi)
    nimet.append(name)   #nyt nimet=[['Erkki', 'Esimerkki'], ['Aimo', 'Assar..]

nimilista.close()


for c in range(len(nimet)):
    kirjoitakirje(c)



    



