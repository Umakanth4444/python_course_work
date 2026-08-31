'''10...1
initalising =1
base
'''
'''
def display(n):
    if n==11:
        return
    print(11-n)
    display(n+1)


display(1)

or  

def display(n):
    if n==11:
        return
    
    display(n+1)
    print(n)


display(1)'''

'''def display(n,i):
    if i== len(n):
        return
    print(n[i])
    display(n,i+1)

display("Codegnan",0)'''

#reverse
'''def display(n,i):
    if i== len(n):
        return
    
    display(n,i+1)
    print(n[i],end=" ")
    
display("Codegnan",0)'''

'''def display(s,i,w):
    if len(s)-w+1 == i : #eg python:len = 8-4+1=3==0 not equal so no need to stop and checks[0:0+4]-0,1,2,3=pyth,ytho,thon 
        return
    print(s[i:i+w])
    display(s,i+1,w)

s= input("Enter the string")
w = int(input("Enter the width"))
display(s,0,w)'''

#using the while
'''def display(s,i,w):
    while len(s)-(w+1)<len(s)-w0:
        
    

s= input("Enter the string")
w = int(input("Enter the width"))
display(s,0,w)'''

#sum of list
'''def display(l,i):
    if i==len(l):
        return 0
    return l[i]+display(l,i+1)

l = [4,23,2,34,28,90]
print(display(l,0))'''

#sum of digits of a num in recursion

'''def display(l, i):
    k = str(l)
    if i == len(k):
        return 0
    return int(k[i]) + display(k, i + 1)

l = 43567
print(display(l, 0))

#or

def display(n):
    if n==0:
        return 0
    return n%10 + display(n//10)
n = 43567
print(display(n))'''

#for product us for above by *

#factorial of a num by ecursion
'''def factorial(n):
    if n==1: #or also use n==0 both gives return 1 so multiplying with 1 doesnt change anything anytime
        return 1
    return n*factorial(n-1)


n = int(input("enter a num"))
print(factorial(n))'''

#fibonacci
'''a,b=0,1
for i in range(8):
    print(a,end=" ")
    a,b=b,a+b
'''
'''
n = int(input("enter the number: "))
if n ==1:
    print(0)
elif n==2:
    print(0,1)
else:
    a,b = 0,1
    print(a,b,end=" ")
    for i in range(n-2):
        a,b=b,a+b
        print(b,end=" ")'''

#using def getting value instead of order of a fib(n)
'''def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
        

n = int(input("enter a number"))
print(fib(n))#this gives the exacct number we get at the fibonacci of it like eg:fib 5 gets five in order of 0,1,1,2,3,5'''
'''
fib(5) = fib(4)+fib(3)=3+1=5
fib(4) = fib(3)+fib(2)=2+1=3
fib(3) = fib(2)+fib(1)=1+1=2
fib(2) = fib(1)+fib(1)=1+0=1
fib(1) = 1
fib(0) = 0

'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")