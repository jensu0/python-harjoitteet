# -*- coding: cp1252 -*-
class Ihminen:
    etunimi = ""
    sukunimi = ""
    ika = 0
    ammatti = ""

    def kerroIka(self):
        print "Ik� on", self.ika

# Luodaan uusi ihminen nimelt��n mies ja
# annetaan h�nelle henkil�tiedot
mies = Ihminen()
mies.etunimi = "Kalevi"
mies.sukunimi = "Karvajalka"
mies.ika = 42
mies.ammatti = "pommikoneen rahastaja"

# Tulostetaan miehen tiedot
print mies.etunimi, mies.sukunimi,"on", mies.ika
print "vuotta vanha",mies.ammatti

# Ja viel� ik� erikseen
mies.kerroIka()
