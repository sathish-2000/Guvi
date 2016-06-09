L = map(int,raw_input().split())
for i in range(1,len(L)-1):
    temp1 =  reduce(lambda x, y: x*y, L[:i])
    temp2 =  reduce(lambda x, y: x*y, L[i+1:])
    print temp1*temp2,
