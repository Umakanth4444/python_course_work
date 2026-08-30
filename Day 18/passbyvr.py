#int float complex str list tuple set dict bool

#list dict set mutables-changes inside and outside
#remaining doesnt change with inside
#int
'''def display(n):
    n+=10
    print("Inside the function",n)

n=10
display(n)
print("Outside functon",n)

#float
def display(n):
    n+=10.3
    print("Inside the function",n)

n=10.3
display(n)
print("Outside functon",n)

#str
def display(n):
    n+="lang"
    print("Inside the function",n)

n="python"
display(n)
print("Outside functon",n)

#complex
def display(n):
    n+=10
    print("Inside the function",n)

n=10+3j
display(n)
print("Outside functon",n)

#tuple
def display(n):
    n+=(1,2,3)
    print("Inside the function",n)

n=(1,2,3,4)
display(n)
print("Outside functon",n)

#bool
def display(n):
    n=False
    print("Inside the function",n)

n=True
display(n)
print("Outside functon",n)

#mutable gives same answers for both inside and outside
#List
def display(n):
    n+=[1,2,3,4,5]
    print("Inside the function",n)

n=[1,2,3]
display(n)
print("Outside functon",n)

def display(n):
    n.append(5)
    print("Inside the function",n)

n=[1,2,3,4]
display(n)
print("Outside functon",n)
#set
def display(n):
    n.add(10)
    print("Inside the function",n)

n={4,5,6}
display(n)
print("Outside functon",n)#both as {10,4,5,6}-diff order

#dict
def display(n):
    n[4]=5
    print("Inside the function",n)

n={1:2,2:3}
display(n)
print("Outside functon",n)'''

