def WritetoFile(todo):
    

    

 
    f = open('todo.txt', 'w')
    n=0
    for n in range (0,len(todo)):
        f.write(todo[n])
        f.write("\n")
        n = n+1
                
            
    f.close()        
    
         
def Add(wtodo,todo):
    todo.append(wtodo)
    WritetoFile(todo)
    return todo

def Do(n,todo):
    del todo [n]
    WritetoFile(todo)
    return todo




def Alku():
    f = open ("todo.txt", "r")
    todo = []
    n = 0
    
    while True:
        rivi = f.readline()
        rivi = rivi.strip("\n")
        if len(rivi) == 0:
            break
        todo.append(rivi)
    
    f.close()
    return todo


todo = []
try: todo = Alku()
except:
    oglimogli = 3
while True:
    m = 0
    if len (todo)>0:
        for m in range (0,len (todo)):
            print m, todo[m]
            m = m+1
    print "----"
    print "1. add"
    print "2. do"
    print "enter quits"
    choice = raw_input ("Give choice: ")
    if choice == "":
        break
    if choice == "1":
        wtodo = raw_input ("Give todo: ")
        todo = Add(wtodo,todo)
    if choice == "2":
        try:m = int (raw_input ("Give index: "))
        except: 
            print "Give an index!"
            continue
        try: abc = todo[m]
        except IndexError:
            print "No such index", m
            continue
        todo = Do(m,todo)



