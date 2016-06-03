k = raw_input("Enter a number\n")
tot = 0
for i in k :
    tot+=(int(i)**3)
if str(tot) == k :
    print "Armstrong Number"
else:
    print "Not an Armstrong Number"
