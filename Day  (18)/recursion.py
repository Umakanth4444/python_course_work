#Recursion: function calling itself
'''
def fun(args):
    if base:
       return
    fun(update arg)
fun(par)

#1-10
def display(n):
    if n==11:#if 1==11 or not,2
        return
    print(n)#if 11=11 it prints n->1,2
    display(n+1)#n+1=1+1=2,2+1
display(1)

#10-1
def display(n):
    if n==0:
        return
    print(n)
    display(n-1)
display(10)'''

#string
def display(s, i):
    if i == len(s):
        return

    print(s[i])
    display(s, i + 1)

display("python",0)