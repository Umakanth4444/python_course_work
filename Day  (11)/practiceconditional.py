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

year = int(input("Enter the year: "))
if year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")