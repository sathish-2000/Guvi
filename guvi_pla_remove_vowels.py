k = raw_input()[::-1]
L = ['a' , 'e' , 'i' , 'o' , 'u']
K = []
for i in k:
    if i not in L:
        K.append(i)
print ''.join(K)
