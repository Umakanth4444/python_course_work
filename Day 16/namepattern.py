'''ABCDEFGHIJKLMNOPQRSTUVWXYZ
  0 1 2 3 4
0 * * * * *
1 *       *
2 *       *
3 *       *
4 * * * * *


n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#B

  0 1 2 3 4
0 * * * * *
1 *       *
2 * * * * *     
3 *       *
4 * * * * *
'''
'''
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j == n-1 or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#E
  0 1 2 3 4
0 * * * * *
1 *       
2 * * * * *     
3 *       
4 * * * * *

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#F
  0 1 2 3 4
0 * * * * *
1 *       
2 * * * * *     
3 *       
4 * 
    

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==m :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#C

  0 1 2 3 4
0 * * * * *
1 *       
2 *      
3 *       
4 * * * * *

n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if i==0 or j ==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#G

  0 1 2 3 4
0 * * * * *
1 *       
2 *   * * *
3 *       *
4 * * * * *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or (j==n-1 and i>=m) or (i==m and j>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#H
  0 1 2 3 4
0 *       *
1 *       *
2 * * * * * 
3 *       *
4 *       *


n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#I

  0 1 2 3 4
0 * * * * *
1     *       
2     *      
3     *       
4 * * * * *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#J

  0 1 2 3 4
0 * * * * * 
1     *   
2 *   *  
3 *   *   
4 * * *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m or (i==n-1 and j<=m) or (j==0 and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
                                                 
#Z

  0 1 2 3 4
0 * * * * * 
1       *
2     *
3   *
4 * * * * *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:#if n=5,i+j==0+4=(n-1)=5-1=4,1+3=4,2+2=4,3+1=4,4+0=4
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#X

0 *       * 
1   *   *
2     *
3   *   *
4 *       * 

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:z#i==j=0.0,1.1,2.2,3.3,4.4 and i+j=0+4=4(n-1)
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#Y

  0 1 2 3 4 
0 *       * 
1   *   *
2     *
3   *   
4 *       

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i+j==n-1 or (i==j and j<=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#K

  0 1 2 3 4 
0 *       * 
1 *     * 
2 * * *
3 *     *
4 *       *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i==m and j<=m) or (i+j==n-1 and i<=m) or (i==j and j>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#R
  0 1 2 3 4 
0 * * * * *      
1 *     * 
2 * * *
3 *     *
4 *       *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i==m and j<=m) or (i+j==n-1 and i<=m) or (i==j and j>=m):  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#M

*       *
* *   * *
*   *   *
*       *
*       *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#W
*       *
*       *
*   *   *
* *   * *     
*       *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i>=m) or (i+j==n-1 and i>=m):  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#V
 0 1 2 3 4 5 6 
0*           *
1*           *
2*           *
3*           *
4  *       *
5    *   *
6      *    '''

'''
4.1,5.2,6.3 = *
4.5,5.4,6.3 = * 7+3=10-1


n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or (i-j==m) or ((i+j)==m+n-1) :  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


4.1,5.2,6.3 = *
4.5,5.4,6.3 = * 7+3=10-1

#Q
 0 1 2 3 4 
0* * * * *
1*       *
2*   *   *
3*     * *
4* * * * *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or (i==j and i>=m):  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#A
 0 1 2 3 4 5 6
0      *    
1    *   *
2  *       *
3* * * * * * *          
4*           *
5*           *
6*           *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==m or (j==0 and i>=m) or (j==n-1 and i>=m) or (i+j==m and i<=m) or (j-i==m and i<=m):  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#L
'''
*       *
* *     *
*   *   *
*     * *
*       *


n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#O
* * * * *
*       *
*       *
*       *
* * * * *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#P

* * * * *
*       *
* * * * *
*
*

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==m or (j==n-1 and i<=m):  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#
* * * * *
*
* * * * *
        *
* * * * *

n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==m or (j==0 and i<=m) or (j==n-1 and i>=m):  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#T
* * * * *
    * 
    *
    *
    *
n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m:  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#U
*       *
*       *
*       *
*       *
* * * * *
'''
n = int(input("Enter size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==n-1 or j==0 or j==n-1:  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()