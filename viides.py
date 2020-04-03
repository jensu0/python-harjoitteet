# -*- coding: cp1252 -*-
class Ihminen:
    etunimi = ""
    sukunimi = ""
    ika = 0
    ammatti = ""

    def kerroIka(self):
        print "Ikä on", self.ika

# Luodaan uusi ihminen nimeltään mies ja
# annetaan hänelle henkilötiedot
mies = Ihminen()
mies.etunimi = "Kalevi"
mies.sukunimi = "Karvajalka"
mies.ika = 42
mies.ammatti = "pommikoneen rahastaja"

# Tulostetaan miehen tiedot
print mies.etunimi, mies.sukunimi,"on", mies.ika
print "vuotta vanha",mies.ammatti

# Ja vielä ikä erikseen
mies.kerroIka()
