'''A function is a block of reusable code used to perform a specific task.
Key features of functions are:
1. Reusability : code once and use it multiple times.
2. Modularity : Divide a large program into smaller parts.
3. Parameters : Functions can accept input values.
4. Return Value : A function can return a result using return.
5.Code Reduction : Avoids writing the same code repeatedly.
6. Readability : Makes programs easier to understand.
7. Easy Debugging : Errors can be isolated to a particular function.
8. Easy Maintenance : Changes can be made in one place.
9. Default Arguments : Parameters can have default values.
10. Variable Arguments : Functions can accept a flexible number of arguments.
11. Multiple Return Values : A function can return more than one value.
12. Nested Functions : A function can be defined inside another function.
13. Recursion : A function can call itself.
14. Built-in Functions : Python provides functions such as print(), len(), and input().
15. User-Defined Functions : Programmers can create functions for their own requirements.
16. Scope : Variables created inside a function can have local scope.
17. Abstraction : Users can use a function without knowing all its internal details.
18. Testing : Individual functions can be tested separately.
19. Organization : Functions help organize a program logically.
20. Improved Efficiency : Reusable functions can make development faster.

-Build-in function: Predefined functuions
-user-defined function: user created..


'''
'''
def functionname(args):
    #statmnt
    return  (opt)

functionname(para)


def gst(price):
    print("Original price:",price)
    print("Final price:",price+price*0.18)

gst(1000)
gst(500)
gst(15000)
gst(10000)
gst(5000)

def table(n):
    print(f"{n} Table")
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

table(0)
#to get upto 20 tables
for i in range(1,21):
    table(i)

def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap year"
    else:
        return "Not a leap year"

print(isleap(2026))
print(isleap(2016))
print(isleap(2012))

def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return "Not a prime"
    
    return "Prime"

print(prime(17))
print(prime(18))
print(prime(2))
print(prime(80))'''
'''
#Positinal Arguments
def display(name,email,password):
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)

display("AB","ab@gmail.com","ab@123")
display("ab@gmail.com","ab@123","AB")
display("AB","ab@123","ab@gmail.com")#it doesnt change the details to ur preferred category even if the details or swapped between them it just prints the values occording to its positions
'''
'''
#Keyword Arguments
def display(name,email,password):
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)

display(name="AB",email="ab@gmail.com",password="ab@123")
display(email="ab@gmail.com",password="ab@123",name="AB")
display(name="AB",password="ab@123",email="ab@gmail.com")#the keyswor argument represents the variable containing the coorect values by mentioning in the print statements


#Default Arguments
def display(name,email,password=None):#None will act as the default parameter in case of no password value found in the print statements
                                    #also the default parameter can only be shown in the last of the args 
                                    # for eg if we want none as default for the name we need to keep the name arg in the last of arguments like(email,password,name=None)
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)

display(name="AB",email="ab@gmail.com")
display(email="ab@gmail.com",password="ab@123",name="AB")
'''
'''
#Variable name argument
def display(*names):#By using the *(Asterick) mark before a arg it helps us 
                    #printing the names in the tuple in each of the line as per print statements given
    print(names)

display("Dinesh")
display("Dinesh","Teja")
display("Dinesh","Teja","dipak")
display("Dinesh","Teja","dipak","Anil")'''

def display(**names):#By using the **(Asterick) mark before a arg it helps us 
                    #printing the keys and values in the dictionary in each of the line as per print statements given
    print(names)

display(n1 = "Dinesh")
display(n1="Dinesh",n2="Teja")
display(n1="Dinesh",n2="Teja",n3="dipak")
display(n1="Dinesh",n2="Teja",n3="dipak",n4="Anil")
