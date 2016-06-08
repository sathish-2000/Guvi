L = map(int,raw_input().split())
P = []
maxi = -99999
for i in range(0,len(L)):
    for j in range(i+1,len(L)+1):
        temp = reduce(lambda x, y: x*y, L[i:j])
        if temp > maxi :
            maxi = temp
            P = L[i:j]
print P
