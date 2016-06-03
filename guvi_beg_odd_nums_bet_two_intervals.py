print "Enter the two intervals:"
m,n = map(int,raw_input().split())
for i in range(m+1,n):
    if i&1 :
        print i
