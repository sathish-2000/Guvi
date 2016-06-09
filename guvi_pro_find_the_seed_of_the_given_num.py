num = input()
flag = 0
for i in range(1,num+1):
    if num%i == 0 :
        temp = i
        pro = i
        while(temp!=0):
            pro*= (temp%10)
            temp/=10
        if pro == num :
            flag = 1
            print "The seed number for the given number is: -->",i


if flag == 0:
    print "No possible seed for the given number: -->",num
