f = open('file.txt', 'r')
count = 0
while True:
    rivi = f.readline()
    if rivi == '':
        break
    count += 1
f.close()
print count
