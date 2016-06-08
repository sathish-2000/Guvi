num = input("Enter the number of inputs:\n\n")
L = []
K = []
for i in range(0,num):
    m,n = map(str,raw_input().split())
    L.append(m)
    K.append(n)
print "The number of grandchild(ren) for the given input is: -->",K.count(L[K.index(raw_input())])
