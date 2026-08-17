#username and pswrd login
'''username = input("Enter the uername: ")
password = input("password: ")

if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Invalid credentials")

products = ["apple", "ball", "bat", "wheat"]
search = input("Enter the product: ")

if search in products:
    print(f"{search} found")
else:
    print(f"{search} not found")'''

#delivery charges
bill = int(input("Enter the charges: "))
if bill > 99:
    print(f"Bill = {bill}")
else:
    print(f"Bill + Extra charges: {bill + 30}")