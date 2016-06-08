L = map(int,raw_input("Enter the array\n").split())
maxi = -999999
for i in range(0,len(L)-1):
    if L[i]-L[i+1] > maxi :
        maxi = L[i]-L[i+1]
        ans = i
        
print ans
