L = map(str,raw_input().split())
k = ''.join(L)
if k == k[::-1] :
    print "Yes, it's a palindrome...."
else:
    print "No, this is not a palindrome...."
