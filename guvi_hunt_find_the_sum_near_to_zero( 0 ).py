L = map(int,raw_input().split())
tot = 99999
for i in range(0,len(L)):
    for j in range(0,len(L)):
        if i == j:
            break
        if abs(L[i]+L[j]) < abs(tot) :
            tot = L[i] + L[j]
            ans1 = L[i]
            ans2 = L[j]
print "Sum is: -->",tot
print "Elements are: -->",ans1,ans2
