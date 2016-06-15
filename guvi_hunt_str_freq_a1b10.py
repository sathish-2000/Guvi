import re

k = raw_input()
L = re.findall(r'\d+', k)
P = re.findall("[a-zA-Z]+", k)
j = 0
s = ''

for i in range(0,len(L)):
    s+=str(P[i])*int(L[i])

print s
