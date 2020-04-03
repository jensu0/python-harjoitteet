a = float(raw_input("Give first number: "))
b = float(raw_input("Give second number: "))
o = int(raw_input("Give operation\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n"))
if o==1:
    print "%.3f" %(a + b)
elif o==2:
    print "%.3f" %(a-b)
elif o==3:
    print "%.3f" %(a*b)
elif o==4:
    if b == 0:
        print None
    else:
        print "%.3f" %(float(a)/float(b))
