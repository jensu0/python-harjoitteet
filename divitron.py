a = int(raw_input("Give first integer: "))
b = int(raw_input("Give second integer: "))
if b == 0:
    print "Zero division error!"
else:
    c=float(a)/float(b)
    print "Result is " + str("%.2f" %c) +"."
