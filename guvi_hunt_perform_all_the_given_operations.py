import re

k = raw_input("The original string is:\n\n")


L = list(k.split())
print k,"\n\n\n\n"


print "Removing the spaces in the string:\n\n",k.replace(" ",""),"\n\n\n\n"


print "The longest word in the string\n"
maxi = 0
for i in L:
    if len(i) > maxi :
        maxi = len(i)
        ans = i
print ans,"Length-->",len(ans),"\n\n\n\n"


print "Number of 'e's in the string: \n\n",k.count('e'),"\n\n\n\n"


print "Number of integers in a string:\n"
P = re.findall(r'\d+', k)
print len("".join(P)),"\n\n\n\n"


print "Number of doubles in a string:\n"
Q = re.findall(r'\d+\.*\d*', k)
print len("".join(Q)),"\n\n\n\n"


print "Number of words in a string: \n\n",len(L),"\n\n\n\n"


print "Number of sentences in string: \n\n",k.count('.'),"\n\n\n\n"
