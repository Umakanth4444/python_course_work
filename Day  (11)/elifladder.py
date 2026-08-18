#whenever u have more than 1 condition use elif ladder
'''budget = int(input("Enter the budget: "))
if budget > 10000:
    print("Trip")
elif budget > 5000:
    print("Resort stay")
elif budget > 3000:
    print("Movie and shopping")
elif budget>1000:
    print("Restaurant")
elif budget>500:
    print("Icecream")
else:
    print("Stay home")'''

'''hour = int(input("Enter the time: "))

if 5<=hour<=11:
    print("Good morning!")
elif 12<=hour<=16:
    print("Good afternoon!")
elif 17<=hour<=20:
    print("Good evening!")
elif 21<=hour<24:
    print("Good night!")
else: 
    print("Midnight sleep well")'''

'''above>10000= cloud hosting
above>5000=business hosting
>2000 = premium hosting
otherwise='''

budget = int(input("Enter the budget: "))
if budget>10000:
    print("Cloud hosting")
elif budget>5000:
    print("Business hosting")
elif budget>2000:
    print("Premium hosting")
else:
    print("Single hosting")