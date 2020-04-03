


def add(a,b):
    c = a + b
    return c
    #print "%.3f" %c
    
def subtract(a,b):
    c = a - b
    return c
    #print "%.3f" %c
    
def multiply(a,b):
    c = a*b
    return c
    #print "%.3f" %c
    
def divide(a,b):
    try:
        c = a/b
        return c
    except:
        return "None"

def main():

    a = float(raw_input("Give first number: "))
    b = float(raw_input("Give second number: "))
    o = int(raw_input("Give operation\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n"))

    if o==1:
        tulos = add(a,b)
        print "%.3f" %tulos
    elif o==2:
        tulos = subtract(a,b)
        print "%.3f" %tulos
    elif o==3:
        tulos = multiply(a,b)
        print "%.3f" %tulos
    elif o==4:
        tulos = divide(a,b)
        if tulos != "None":
            print "%.3f" %tulos
        else:
            print "None"

if __name__ == '__main__':
    main()
