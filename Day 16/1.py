'''
  *  
 * *
* * *
'''

n = int(input())
m = n//2
for i in range(n):
    for j in range(n+2):
        if i+j==m or i+j==2*(m) or i+j==3*(m):
            print("*",end="")
        else:
            print(" ",end="")
    print()