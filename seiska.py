import sys

print "Ajettavan koodin nimi on", sys.argv[0]
print "Annoit", len(sys.argv), "komentoriviparametria."

print "Ne olivat"
for i in sys.argv:
    print i

print "sys.argv on kuin normaali lista:"
print sys.argv
