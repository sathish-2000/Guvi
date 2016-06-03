k = list(raw_input())
k = map(int,k)
temp = str(sum(k))
if temp == temp[::-1] :
    print "palindrome"
else:
    print "not palindrome"
