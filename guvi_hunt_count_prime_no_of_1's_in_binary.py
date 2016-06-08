first,last = map(int,raw_input().split())
kount = 0
for i in range(first,last+1):
    count = 0
    k = bin(i)[2:].count("1")
    for i in range(1,k+1):
        if k%i == 0 :
            count+=1
    if count == 2 :
        kount+=1
print "Total number of numbers are:\t", kount
    
