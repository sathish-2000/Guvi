def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

num = input()
if num == 0 :
    print "0"
elif num == 1 :
    print "1"
else:
    print fib(num)
