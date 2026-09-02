'''def reels():
    data = ["1..100","101..200","201...300","301..400"]
    for i in data:
        yield i
res = reels()
print(next(res))
print(next(res))
print(next(res))
print(next(res))

def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1
res = countdown()
for i in res:
    print(i)#no need to use print(res(i)) just use print(i)j'''
'''
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
res=factors(16)
for i in res:
    print(i,end=" ")'''

def prime(n):
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
                yield i
res = prime(100)
for i in res:
    print(i,end=" ")

print()
def prime(n,m):
    for i in range(n,m+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
                yield i
res = prime(50,100)
for i in res:
    print(i,end=" ")