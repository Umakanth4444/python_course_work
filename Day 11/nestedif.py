#if inside the if
#fa=following account and cf=close friends
'''fa = eval(input("Follows account: "))
if fa:
    cf = eval(input("Close friends: "))
    if cf:
        print("Story visible")
    else:
        print("Not in close friends list")
else:
    print("Follow the account first")'''

'''reg = eval(input("Registered: "))
if reg:
    fee = eval(input("Fee paid: "))
    if fee:
        print("Tournament entry confirmed")
    else:
        print("Entry fee pending")
else:
    print("Registration required")'''

'''l_status = eval(input("Is Active: "))
if l_status:
    a_permission = eval(input("Permission Granted: "))
    if a_permission:
        print("File opened successfully")
    else:
        print("File not opened")
else:
    print("File not opened")'''

data = {
    "A":{"Status":True,"python":90,"mysql":96,"flask":91}, 
    "B":{"Status":False,"python":None,"mysql":None,"flask":None},
    "C":{"Status":True,"python":70,"mysql":87,"flask":45},
    "D":{"Status":True,"python":65,"mysql":34,"flask":19},
    "E":{"Status":True,"python":9,"mysql":6,"flask":56},
    "F":{"Status":True,"python":20,"mysql":16,"flask":100},
}

name = input("Enter the name: ")
if name in data:
    if data[name]["Status"]:
        sum = data[name]["python"] + data[name]["mysql"] + data[name]["flask"]
        avg = sum/3
        print(f"Hello {name}")
        print(f"Your average score in {avg}")
        if avg >= 90:
            print("Outstanding performance")
        elif avg>=80:
            print("Very Good job")
        elif avg>=70:
            print("Well done, work hard")
        elif avg>=35:
            print("Better luck next time")
        elif avg>100:
            print("Invalid marks")
        else:
            print("You failled the exam, try hard")
    else:
        print(f"{name} is absent")
else:
    print(f"{name} not in the list")
