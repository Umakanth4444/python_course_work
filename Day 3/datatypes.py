Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Data Types
>>> #int float complex (numeric daa types)
>>> a = 12
>>> type(a)
<class 'int'>
>>> b = 13.4
>>> type(b)
<class 'float'>
>>> c =13+4j
>>> type(c)
<class 'complex'>
>>> j = J
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    j = J
NameError: name 'J' is not defined
>>> #str list tuple
>>> #string is a collection of characters and used beteen '' and ""cannot change in its object reference: immutable
>>> s = "codegnan"
>>> id(s)
2810980181168
>>> s+= "gnan"
>>> s
'codegnangnan'
>>> id(s)
2810980138736
>>> #so immutable
>>> #list is a collection of elements and it is mutable
>>> l = [1,2,3,4]
>>> type(l)
<class 'list'>
>>> id(l)
2810980012608
>>> l.append(5)
>>> l
[1, 2, 3, 4, 5]
>>> id(l)
2810980012608
>>> #heterogeneous(can contain different data types, dynamically sized,dupliacete exists, mutable, ordered
>>> #dynamically sized means we can not have limited size if we wish we can increase its size
>>> i = [1,2.1,'str',[1,23]]
>>> type(i)
<class 'list'>
>>> #tuple:immutable,ordered,heterogeneous,fixed size,allows duplicates
>>> #collection of elements enclosed with paranthesis '()'
t = (1,2,3,4)
type(t)
<class 'tuple'>
t = (1,1,1,1)
t
(1, 1, 1, 1)
t = (1,2.3,'str')
t
(1, 2.3, 'str')
#Sequential data types: str,list,tuple
#mapping:set,dict
#set is a collection of elements enclosed with curly brackets
#mutable, doesnt allow duplicates, dynamically sized, heterogenous, Unordered
s = {1, 2, 3, 4, 5}
type(s)
<class 'set'>
id(s)
2810979688384
s.add(21)
s
{1, 2, 3, 4, 5, 21}
s
{1, 2, 3, 4, 5, 21}
a = {1,'a',2.1}
a
{1, 'a', 2.1}
#dictionary is a collection of key value pairs enclosed with curly brackets '{}'
d = {'pro':'XYZ','pric':876,'stock':True}
d
{'pro': 'XYZ', 'pric': 876, 'stock': True}
#Mutable, Ordered, Dynamically sized, Heterogeneous,
#frozen set:fixed size,immutable
s = frozen set{1,1,1,115,18,2,3}
SyntaxError: invalid syntax
s = frozenset{1,1,1,116,18,2,3}
SyntaxError: invalid syntax
#({})
a = True
b =True
type(a)
<class 'bool'>
a = {}
l =[]
t = ()
a = ''
s = None
type(s)
<class 'NoneType'>
type(a)
<class 'str'>
type(t)
<class 'tuple'>
type(a)
<class 'str'>
b = {}
type(b)
<class 'dict'>
