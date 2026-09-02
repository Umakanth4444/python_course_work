'''l = [i for i in range(1,11)]
print(l)

even = [i for i in range(2,11,2)]
print(even)

n = int(input())
factor = [i for i in range(1,n+1) if n%i==0]
print(factor)

list = [1,2,3,4,5,6,7,8,9]
evenlist = [i if i%2==0 else 0 for i in list]
print(evenlist)'''

#l = [[1,2,3],[1,2,3],[1,2,3]]
'''l = []
for i in range(3):
    temp=[]
    for j in range(1,4):
        temp.append(j)
    l.append(temp)
print(l)

l = [[j for j in range(1,4)]for i in range(3)]
print(l)'''

#l = [[1,2,3],[4,5,6],[7,8,9]]
l = []
for i in range(3):
    temp = []
    for j in range(1,4):
        temp.append(j)
    temp1 = []
    for k in range(4,7):
        temp1.append(k)
    temp2 = []
    for o in range(7,10):
       temp2.append(o)
l.append(temp)
l.append(temp1)
l.append(temp2)
print(l)
'''

#set of 1-10
s = {i for i in range(1,11)}
print(s)
#dict
s={i:i*i for i in range(1,11)}
print(s)'''