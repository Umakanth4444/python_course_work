'''i = 1
while i<=10:
    print(i)
    i+=1

i = 10
while i>0:
    print(i)
    i-=1

i = 5
while i<=50:
    print(i)
    i+=5

s = 'while loop'
i = 0
while i<len(s):
    print(s[i])
    i+=1
    ''''''

s = 'while loop'
i = len(s)-1
while i>=0:
    print(s[i])
    i-=1

l = [3456,5678,5678]
i = 0
while i<len(l):
    print(l[i])
    i+=1

n = 8665
while n>0:
    print(n%10)
    n//=10#8665//10=866(bcz of //(floor division) after the point there will be no value so it is 866 than 866.5('/'used))

n = 98765432456
sumofdigits = 0
while n>0:
    sumofdigits += n%10#(0+6,+5,+4,+2,+3,+4,+5,+6,+7,+8,+9)
    n//=10#(will be deleted:6,5,4,2,3,4,5,6,7,8,9)

print("sum of digits:",sumofdigits)

n = 98765432456
productofdigits = 1
while n>0:
    productofdigits *= n%10
    n//=10

print("sum of digits:",productofdigits)


n = 34567
res = 0
while n>0:
    rem = n%10
    res = res*10+rem
    n//=10

print(res)

n = 4532
res = 0
while n>0:
    rem = n%10#2,3,5
    res = res*10+rem#2,2*20+3,
    n//=10#453,45

#sum of even digits
n = 98765432123456789
s_even = 0
while n>0:
    rem = n%10
    if rem%2==0:
        s_even+=rem
    n//=10
print(s_even)

l = [7,9,23,0,0,0,12,0,2,3,4,0,0,2,8,0,25,1,0]

while 0 in l:
    l.remove(0)#remove is for value,pop is for element
print(l)

l = [2,3,6,76,12,4,1,5,61,4,5,2,23]
i = 0
j = len(l)-1
while i<len(l):
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1
    '''

l = [2,3,6,76,12,4,1,5,61,4,5,2,23]
i = 0
j = len(l)-1
while i<len(l):
    print(l[i]+l[j])
    i+=1
    j-=1



