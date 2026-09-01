'''
var = lambda arg:exp
'''
'''wish = lambda name: print("Welcome to the course",name)
wish("Dolu")

gst = lambda price: price + price*0.18
print(gst(5000))
print(gst(50000))

avg = lambda a,b,c: (a+b+c)/3
print(avg(2,4,6))

largest = lambda a,b,c: a if a>b and a>c else (b if b>c else c)
print(largest(10,20,30))

iseven = lambda a: "even" if a%2==0 else  "odd"
print(iseven(999))

isvowel = lambda a: "vowel" if a in "aeiouAEIOU" else "cons"
print(isvowel("u"))
print(isvowel("k"))

#map
l = [1,2,3,4,5,6]
update = list(map(lambda i:i+10,l))
print(update)

t = (785,367,339,243,873)
discount= list(map(lambda i:i-i*0.3,t)) #30% discount
print(discount)

#filter
l = [1,2,3,4,5,6]
odd = list(filter(lambda i:i%2!=0,l))
print(odd)


t = (7851,367,339,243,8730,2000)
n = list(filter(lambda i:i>1000,t)) #30% discount
print(n)

l = ["sowmya@codegnan.com","sowmya@yahoo.com","sowmya@gmail.com","sowmya@outlook.com"]
domain = list(map(lambda i:i.split('@')[-1],l))
print(domain)

from functools import reduce
l = [4,2,3,5,2,1,444,2,4]
res = reduce(lambda sum,i: sum+i,l)
print(res)

res1 = reduce(lambda product,i: product*i,l)
print(res1)

seats = {
    's1':True,
    's2':False,
    's3':False,
    's4':False,
    's5':True,
    's6':True}

s = list(filter(lambda i: seats[i]!=True,seats))
print(s)

products = {
    'eggs':80,
    'sugar':60,
    'salt':40,
    'butter':40,
    'milk':30}

res = list(filter(lambda i: products[i]>50,products))
print(res)'''

products = {
    'eggs':80,
    'sugar':60,
    'salt':40,
    'butter':40,
    'milk':30}

print(dict(sorted(products.items(),key = lambda i:i[1])))#sorted in order of items order inincrease
print(dict(sorted(products.items(),key= lambda i:i[1],reverse = True)))#in reverse order from the values
print(dict(sorted(products.items())))#increasing order of dictionary where the keys followed in increasing order
print(sorted(products.items()))#followed a key,value in a tuple like(key,value) in a list like[(key1,value),(key2,val2)]
