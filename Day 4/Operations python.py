Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Python Operators:
#Arithematic Operator:
a = 10
b = 5
a+b
15
a-b
5
a*b
50
a/b
2.0
a//b
2
a%b
0
a = 9
a/2
4.5
a**5
59049
a*3
27
#Comparison Operators
a<b
False
a>b
True
a<=b
False
a>=b
True
a>=10
False
a==b
False
a!=b
True
a=b
a==b
True
#Assignment operators
a =50
a += 30
a
80
a -= 20
a
60
a *= 2
a
120
a .= 2
SyntaxError: invalid syntax
a **= 2
a
14400
#*=multiplication
#**= power
a /=2
a
7200.0
a//=3
a
2400.0
a = 7200
a //= 3
a
2400
a %= 9
a
6
a==1
False
a
6
#Reltion Operator
#Reltional Operator
email = True
pswrd = false
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    pswrd = false
NameError: name 'false' is not defined. Did you mean: 'False'?
pswrd = false
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    pswrd = false
NameError: name 'false' is not defined. Did you mean: 'False'?
email and pswrd
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    email and pswrd
NameError: name 'pswrd' is not defined
pswrd = False
email and pswrd
False
login = True
seen = false
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    seen = false
NameError: name 'false' is not defined. Did you mean: 'False'?
seen = False
login or seen
True
login and seen
False
'a' in 'a,e,i,o,u'
True
'a' not in 'a,i,e,o,u'
False
22%3==0
False
not 22%3==0
True
#Membership operations
#str list tuple set dict
#whether its in there or not(in)
a = 'python programming'
python in a
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    python in a
NameError: name 'python' is not defined
'python' in a
True
'program' in a
True
'p' not in a
False
l = [1,2,3,4]
2 in l
True
2,4 in l
(2, True)
1 not in l
False
0 in l
False
t = (1,2,33)
1 in t
True
33 not in t
False
s = {1,22,33,44}
2 in s
False
22 not in s
False
33 in s
True
d = {'t':'titanic','b' : 'batman'}
'b' in d
True
'batman' in d
False
#only the keys will be shown not the values
#Identity operator
l = [1,2,3,4]
m = [1,2,3,4]
l==m
True
id(l)
1824840978240
id(m)
1824841205696
#both ids to be same for identical ones
n = m
n
[1, 2, 3, 4]
id(n)
1824841205696
>>> l in m
False
>>> m in l
False
>>> l in n
False
>>> m in n
False
>>> n in m
False
>>> n == m
True
>>> n == l
True
>>> n is m
True
>>> n is l
False
>>> m is n
True
>>> m is l
False
>>> # is / == to be differentiated is can only be true if the identical;i same and == will be same in appearance
>>> #bitwise operator
>>> ''' '''
' '
>>> ''' 0 = 0000
... 1 = 0001
... 2 = 0010
... 3 = 0011
... 4 = 0100
... 5 = 0101
... 6= 0110
... 7 = 0111
... 8 = 1000
... 9 = 1001
... 10 = 1010
... 11 = 1011
... 12 = 1100
... 13 = 1101
... 14 = 1110
... 15 = 1111 '''
' 0 = 0000\n1 = 0001\n2 = 0010\n3 = 0011\n4 = 0100\n5 = 0101\n6= 0110\n7 = 0111\n8 = 1000\n9 = 1001\n10 = 1010\n11 = 1011\n12 = 1100\n13 = 1101\n14 = 1110\n15 = 1111 '
>>> #& / ^ << >>
>>> 12 & 13
12
