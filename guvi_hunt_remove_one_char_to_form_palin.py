# Hi Mr.Arun Prakash,  We can able to remove make the string "racecar" as Palindrome by removing 'e' also. The following solution will
# give the output in that manner. I hope this method and output is also correct.



k = raw_input()
if k == k[::-1]:
    print "Already Palindrome"
else:
    flag = 0
    for i in range(0,len(k)):
        L = k[:i]+k[i+1:]
        if L == L[::-1]:
            print "Remove this element to convert the string to Palindrome: -->",k[i]
            print "And the index is: -->",i
            flag = 1
            break
    if flag == 0 :
        print "Not possible to convert as a palindrome"
