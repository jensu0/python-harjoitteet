# -*- coding: cp1252 -*-
# Laivanupotus

# pasianssiversio
#
# 1. Ruudukko - Tehty
#  - tieto siitä, missä laivoja on
# Mihin ammutaan - Tehty
# - Mihin ammutaan

# Laivojen sijainnit
# - arvotaan
# Osuiko vai ei
# Pelin loppu
# - kaikki laivat uponnu
# Onnitteluviesti
# Uppoamisen tarkistus

# Rajatut ammukset?
# tekoäly?

#RUUDUKKO
# 10 x 10

def teeTaulukko():
    taulukko = []
    for i in range(10):
        rivi = []
        for j in range(10):
            rivi.append("_")
        taulukko.append(rivi)
    return taulukko

def tulostaTaulukko(taulukko):
    for rivi in taulukko:
        for alkio in rivi:
            print alkio,
        print

def kysyInput():
    '''kysyy niin kauan koordinaatteja kunnes ne ovat oikein'''
    while True:
        try:
            rivi = int(raw_input("anna rivi: "))
        except ValueError:
            print 'anna luku'
            continue

        if rivi < 0 or rivi > 9:
            print 'anna rivi väliltä 0-9'
            continue
        break

    while True:
        try:
            sarake = int(raw_input("anna sarake: "))
        except ValueError:
            print 'anna luku'
            continue

        if sarake < 0 or sarake > 9:
            print 'anna sarake väliltä 0-9'
            continue
        break
    return rivi, sarake


taulukko = teeTaulukko()
taulukko[0][2] = 'L'
taulukko[0][3] = 'L'
tulostaTaulukko(taulukko)

rivi, sarake = kysyInput()

if taulukko[rivi][sarake] == 'L':
    print 'osu'
    taulukko[rivi][sarake] = "X"
else:
    print 'huti'
    taulukko[rivi][sarake] = "o"

tulostaTaulukko(taulukko)
