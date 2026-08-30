#possitive or negative
'''nmbr = int(input("Enter the number: "))
if nmbr>0:
    print("Positive number")
else:
    print("Negative number")'''

#even or odd
'''n = int(input("Enter the number: "))
if n>0 and n%2==0:
    print("Even number")
elif n%2!=0:
    print("Odd number")
else:
    print("Not a even or odd")'''

#divisible by 5
'''n = int(input("Enter a number:"))
if n%5==0:
    print("Divisible by 5")
else:
    print("Not divisible")'''

#divisible by 3 and 7

'''n = int(input("Enter a number:"))
if n%3==0 and n%7==0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible")'''

#Check for leap year

'''year = int(input("Enter the year: "))
if year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#check pass or fail
marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")'''

#check if a number is 3-digit
'''num = input("Enter a number: ")
if len(num)==3:
    print("3-digit number")
else:
    print("Not a 3-digit number

#check if ch is a vowel
letter = input("Enter a letter: ")
vowel = ["a","e","i","o","u"]
if letter in vowel:
    print("Vowel")
else:
    print("Constant")

#check greatest of two num
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if a>b:
    print(f"{a} is greater")
elif b>a:
    print(f"{b} is greater")
else:
    print(f"{a},{b} are equal")

#check smallest of 2
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if a<b:
    print(f"{a} is smaller")
elif b<a:
    print(f"{b} is smaller")
else:
    print(f"{a},{b} are equal")

a,b = map(int,input("Enter two numbers: ").split())
if a>b:
    print("a is greater")
else:
    print("b is greater")

#check if number is zero
num = int(input("Enetr a number: "))
if num==0:
    print("Number is zero")
else:
    print("Number is not a zero")

#check if number is multiple of 10
num = int(input("Enter a number: "))
if num%10==0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")

#check if age is eligible to vote(18+)
age = int(input("Enter age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not Eligible")

#check if num is btw 1 and 100

num = int(input("Enter a number: "))
if 1<num<100:
    print("In range")
else:
    print("Not in range")

#check if num is aq of another
sq,num = map(int,input("Enter a number: ").split(","))
if num**2 == sq:
    print(f"{sq} is square of {num}")
else:
    print(f"{sq} is not a square of {num}")

#check if two strings are equal
a,b = input("Enter two strings: ").split(",")
if a==b:
    print("strings are equal")
else:
    print("Not equal")

#check if a num is prime
num = int(input("Enter a number: "))
if num<2:
    print("Not a prime")
else:
    for i in range(2,num//2+1):
        if num%i==0:
            print("Not a prime")
            break
    else:
        print("prime")

#check if ch is uppercase
l = input("Enter a character: ")
if l is l.capitalize:
    print("Uppercase letter")
else:
    print("Not a uppercase")'''

#check if temperature is hot (>30c)

temp = int(input("Enter temperature: "))
if temp>30:
    print(f"{temp}°C is Hot ")
else:
    print("Not hot")