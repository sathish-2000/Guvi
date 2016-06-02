k = raw_input()
K = []
for i in range(0,len(k)-1):
    if k[i] == k[i+1] :
        K.append(k[i])
        K.append('*')
    else:
        K.append(k[i])
k = k[::-1]
K.append(k[0])
print ''.join(K)
