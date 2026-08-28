#local variable: the declaration of variable inside a function
#global variable: the declaration of variable outside the function
'''def display():
    n=10#local variable
    print("Inside function,n")

display()
print("Outside function",n)#cannot be defined by the variable which is inside the function


def display():
    print("Inside function:",n)#n be defined from global variable outside the function
n=10#global variable
print("Outside function",n)#can be defined from global variable

def display():
    global n#it is a local variable named global which helps in accessing of the variable outside the function too
    n=10
    print("Inside function",n)
display()
print("Outside function",n)

def display():#display(n) no need of n paraameter or any parameter mentioning if we use the global 
    global n
    n+=10
    print("Inside function",n)#inside function gets 20 becoz global var given n=10 and inside we taken n+=10
n=10
display()
print("Outside function",n)#here also gives 20 bcoz global n gives acces to the global var outside the function

def display():
    course = "PFS"
    def update():
        course = "JFS"
        print("Inner function",course)#gives jfs
    update()
    print("Outer function",course)#gives pfs

display()

def display():
    course = "PFS"
    def update():#scope
        nonlocal course#this makes the course variable be used in boyh inside the function and outside too
        course = "JFS"
        print("Inner function",course)#jfs
    update()
    print("Outer function",course)#jfs

display()
l = [1,2,3,4,5]
print(sum(l))

sum = 1
print(sum(l))#if we print this it only give the first sum(l) as 15 not the second sum(l)
#because we mentioned in the next line as sum as a variable sum=1 so it acts as a variable and gives the next sum(l) as int error
#gives 'int' object is not callable

l = [1,2,3,4,5]
print(sum(l))

sum = 10
print(sum)#here the first sum(l) gives 15 and next sum gives as 10 because we mentioned the sum as a variable given a integer'''
