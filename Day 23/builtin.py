'''import sys

print(sys.argv)
print(sys.version)
print(sys.path)
print("start")
sys.exit()
print("end")'''
'''
import platform

print(platform.system())
print(platform.release())
print(platform.processor())
print(platform.())'''

import math

'''print(math.pi)
print(math.e)

print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.gcd(8,12))
print(math.sqrt(36))
print(math.pow(2,3))

print(round(12.6666))#gives 13
print(round(12.9999999))#13
print(round(12.44))#12

print(math.ceil(12.00000001))#13
print(math.ceil(12.3))#13
print(math.ceil(12.6666))#13
print(math.ceil(12.99999999))#13

print(math.floor(12.00000001))#12
print(math.floor(12.3))#12
print(math.floor(12.6666))#12
print(math.floor(12.9999999))#12'''

'''
import random

random.seed()#using this makes giving the output same values 
#which we randomly get on first output which only gives if we given a value

print(random.random())#gives a random in btw 0-1 in decimal
print(random.randint(1,6))#gives a random in btw 1-6 
print(random.uniform(1,6))#gives a random in btw 1-6 in decimal

l = ['r','p','s']
print(random.choice(l))#gives random of r or p or s

lang = ['python','java','sql','flask','reactjs']
print(random.choices(lang,k=2))#k acts as how many to take

random.shuffle(lang)
print(lang)#it changes the shuffle after using sgufffle for the list
#then we need to print lang list bcoz the use function of shuffle make the list changed entirely.
'''
'''
from collections import Counter
s = "python programming"
res = Counter(s)
print(res)



d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)

from collections import Counter,defaultdict

s = "python programming"#same process like above frequency of each character
d = defaultdict(int)

for i in s:
    d[i]+=1
print(d)
products = ["sugar","salt","milk"]

res = defaultdict(list)

for i in products:
    res[i].append(['des','rev','com'])
print(res)
'''

from collections import Counter,defaultdict,deque
l = deque([])

l.append(10)#10
l.append(20)#10 20
l.append(30)#10 20 30
l.append(40)#10 20 30 40
l.pop()#10 20 30
l.pop()#10 20 
l.append(50)#10 20 50
l.append(60)#10 20 50 60
l.popleft()#20 50 60
l.popleft()#50 60
l.append(70)#50 60 70
l.popleft()#60 70
print(l)

l.appendleft(10)#10
l.appendleft(20)#20 10
l.appendleft(30)#30 20 10
l.appendleft(40)#40 30 20 10
l.pop()#40 30 20
l.pop()#40 30 
l.appendleft(50)#50 40 30
l.appendleft(60)#60 50 40 30
l.popleft()# 50 40 30
l.popleft()# 40 30
l.appendleft(70)#70 40 30
l.popleft()#40 30
print(l)