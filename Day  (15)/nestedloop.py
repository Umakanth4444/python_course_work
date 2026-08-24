'''for i in range(5):
    print(i)
for i in range(5):
    print(i,end=" ")
for j in range(3):
    print(j,end=' ')


for i in range(10):#rows
    for j in range(5):#columns
        print(j,end=' ')
    print() #prints new line by default not usin /n

for i in range(5):
    for j in range(5):
        print('*',end="")
    print()

for i in range(5):
    for j in range(5):
        print(j%2,end="")
    print()


for i in range(5):
    for j in range(5):
        print(i%2,end="")
    print()

for i in range(5):
    for j in range(5):
        print((i+j)%2,end='')
    print()

for i in range(5):
    for j in range(5):
        print(i+j,end='')
    print()

count = 1
for i in range(5):
    for j in range(5):
        print(count,end='  ')
        count+=1
    print()

for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()

for i in range(5):
    for j in range(5-i):
        print('*',end='')
    print()'''


'''12345
   109876
   1112131415
   2019181716
   2122232425'''

'''
    *
   **
  ***
 ****
*****    
'''
'''n = int(input("Enter the size"))
for i in range(n):
    for sp in range(5-i-1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()'''


'''
*****
 ****
  ***
   **
    *
'''
'''n = int(input("Enter the size: "))
for i in range(5):
    for sp in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end='')
    print()'''

'''
*
**
***
****
*****
****
***
**
*
'''
'''n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print("*",end="")
    else:
        for k in range(n-i):
            print("*",end="")
    print()
'''
'''
#the optimized version of above pattern problem
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i<=m:
        print("*"*(i+1),end="")
    else:
        print("*"*(n-i),end="")
    print()
'''

'''
0    *
1   **
2  ***
3 ****
4*****
5 ****
6  ***
7   **
8    *

9-5=4
9-6=3
9-7=2
9-8=1
'''

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i<=m:
        print(" "*(m-i),'*'*(i+1),end=' ',sep=' ')
    else:
        print(' '*(i-m),'*'*(n-i),end=' ',sep=' ')
    print()
