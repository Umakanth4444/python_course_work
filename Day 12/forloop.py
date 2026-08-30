'''
for var in seq:
    #statement
-----------------'''

'''a = "python programming"#string
for i in a:
    print(i)'''

'''l = [1,2,3,4,5]#list
for i in l:
    print(i)
    '''

'''t = (1,2,3,4,)#tuple
for i in t:
    print(i)'''

'''s = {100,263,"ab","man"}#set
for i in s:
    print(i)'''

''''d = {1:2,2:3,3:4,4:5}
for i in d:
    print(i,d[i])'''

#Range functions(range gives numerical values)
#range(start,end+1,step):(0,,1)
'''for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)
for i in range(5,101,12):
    print(i)

for i in range(5,0,-1):
    print(i)

for i in range(19,-10,-4):
    print(i)
'''
#for use of index use the range to iterate

'''s ="python programming"
for i in range(18):
    print(i,s[i])

for i in range(len(s)):
    print(i,s[i])'''

#for using the range functions on set,dictionary is not possible

'''n = (456,4567,543,4567,2345)
for i in range(len(n)):
    print(i,n[i])'''

'''n = {1,2,3,4}
for i in range(len(n)):
    print(i)#this only mentions indices not the values
    #print(i,n[i]) not posssible because we cant mention for the values with its indices

s = "python programming"
for i in enumerate(s):
    print(i)

n = [1,2,3,4,5]
for i in enumerate(n):
    #print(i)
    print(i[0],i[1])'''

'''d = {1:2,3:4,5:6,7:8}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])#output for three indices like sequence from 0,keys from d,values of keys

d = {1:2,3:4,5:6,7:8}
for i in enumerate(d):
    print(i[0],d[i[1]])#sequence,values

d = {1:2,3:4,5:6,7:8}
for i in enumerate(d):
    print(i,d[i[1]])#sequence with key in tuple and values

for i in range(1,11):
    if i==5:
        break#stops after getting to 5 but not printing the 5 value in either cases
    print(i)

for i in range(1,11):
    if i==5:
        continue#skips the 5 and prints remaining all
    print(i)

for i in range(1,11):
    if i==5:
        break
    print(i)
else:
    print("End of the loop")#in this if iteration gets 5 the else block doesnt work and using of break

for i in range(1,11):
    if i==15:
        break
    print(i)
else:
    print("End of the loop")#but in this the i is not gonna reach 15 bcoz of the limit of 11 so the else will be working where break doesnt be helpful

l = [12,13,14,15,16,17,18]
n=16
for i in l:
    if i == n:
        print(n,"found")#if we doesnt use the break it gives both found and not found
else:
    print(n,"Not found")

l = [12,13,14,15,16,17,18]
n=15
for i in l:
    if i == n:
        print(n,"found")
        break#it only gives if it is there as found if not as not found
else:
    (n,"Not found")

l = [12,13,14,15,16,17,18]
n=26
for i in l:
    if i == n:
        print(n,"found")
        break
else:
    print(n,"Not found")

pin = 1234

for i in range(5):
    epin = int(input("Enter pin: "))
    if epin == pin:
        print("Unlock phone")
    else:
        print("Invalid lock")#this code goes on giving to enter the pin even after entering pin correct or wrong it shows enterpin again
pin = 1234

for i in range(5):
    epin = int(input("Enter pin: "))
    if epin == pin:
        print("Unlock phone")
        break
    else:
        print("Invalid lock")#in this code we can get the same enter the pin only if we enter the wrong pins but after entering the right pin it shows phone unlocked and the output finishes it doesnt says to enter pin again
#because break is used after unlock phone print


pin = 1234

for i in range(5):
    epin = int(input("Enter pin: "))
    if epin == pin:
        print("Unlock phone")
        break
    else:
        print("Invalid lock")
else:
    print("Try after 30sec")
#in this code the else of for's used for giving the try after 30sec print value after getting the invalid code 
#after 5 attempts because of the taken range of 5

pin = 1234

for i in range(2):
    epin = int(input("Enter pin: "))
    if epin == pin:
        print("Unlock phone")
        break
    else:
        print("Invalid lock")
else:
    print("Try after 30sec")'''

#prime number

n = int(input("Enter a number: "))
for i in range(2,n//2+1):#the range is from 2 ,half of the n plus 1(n//2+1);ex:for 10(2,10//2+1(6))#6 is the limit
    if n%i==0:
        print(n,"is not a prime")
        break
else:
    print(n,"is a prime number")