L = map(int,raw_input().split())
P = []
maxi = -99999
for i in range(0,len(L)):
    for j in range(i+1,len(L)+1):
        if sum(L[i:j]) > maxi :
            maxi = sum(L[i:j])
            P = L[i:j]
print P
