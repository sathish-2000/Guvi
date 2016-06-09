L = map(int,raw_input().split())
P = []
for i in L:
    k = bin(i)[2:].count("1")
    P.append( [ k , i ] )
#P = map(int,P)
P = sorted(P)[::-1]
for i in range(0,len(P)):
    print P[i][1],
