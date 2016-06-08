L = map(str,raw_input("Enter the a1 elements:\n\n").split())
P = map(str,raw_input("Enter the a2 elements:\n\n").split())
if P in L :
    print "a1 is a subset of a2"
else:
    print "a1 is not a subset of a2"
