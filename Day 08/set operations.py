Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#mju unordered unique dyn he
#mu unordered unique dyn he
s = {}
type(s)
<class 'dict'>
s = set()
type(s)
<class 'set'>
s = {1,1,1,1}
s
{1}
s = {1,2,3,4,5,6,23,34,443,542,889}
s
{1, 2, 3, 4, 5, 6, 34, 23, 889, 443, 542}
s = set()
s.add(1)
s.add(2.3)
s.add("strt")
s.add(1+2j)
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add((1,2,3))
s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.add({1,2,3})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add({1:1,2:2})
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.add({1:1,2:2})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add(True)
s
{1, 2.3, 'strt', (1+2j), (1, 2, 3)}
a = {1,2,3,4,5}
b = {3,5,7,8,9}
2 in a
True
4 in b
False
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
#union
a & b #intersection(commpon elements)
{3, 5}
a - b #the values presented in a removing same values in a,b
{1, 2, 4}
b - a
{8, 9, 7}
a ^ b #removes the common values and gives all the combined of a and b
{1, 2, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5}
#{1}{1,2}{1,2,3}{1,2,3,4}{1,2,3,4,5}{4,5}{}(subsets)
{1,2,3}<=a #subset to a
True
{1,7,8,9}<=a
False
a>={1,2,3}#superset
True
a>={1,2}
True
m = {1,2,3}
n = {4,5,6}
n.isdisjoint(m)
True
m.isdisjoint(n)
True
a.isdisjoint(b)
False
#disjoint:not having the same values of a,b or m,n
a = {12,23,34,45,22,31,56,79,84,11}
osrted(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    osrted(a)
NameError: name 'osrted' is not defined. Did you mean: 'sorted'?
sorted(a)
[11, 12, 22, 23, 31, 34, 45, 56, 79, 84]
max(a)
84
reversed(a)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    reversed(a)
TypeError: 'set' object is not reversible
reverse(a)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    reverse(a)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
len(a)
10
a.index(12)#cannot find index bcoz it is unordered
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.index(12)#cannot find index bcoz it is unordered
AttributeError: 'set' object has no attribute 'index'
a.find(12)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.find(12)
AttributeError: 'set' object has no attribute 'find'
a.count(11)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.count(11)
AttributeError: 'set' object has no attribute 'count'
all({1,2,3,4,5,44})
True
any({0,'')
    
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
any({0,""})
    
False
any({0,'',1})
    
True
sum(a)
    
397

a
    
{34, 11, 12, 45, 79, 84, 22, 23, 56, 31}
a = {1,2,3}
    
b = a
    
b.add(4)
    
b
    
{1, 2, 3, 4}
a
    
{1, 2, 3, 4}
b = a.copy()
    
b.add(5)
    
b
    
{1, 2, 3, 4, 5}
a
    
{1, 2, 3, 4}
a,add(101)
    
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a,add(101)
NameError: name 'add' is not defined
a = {1,2,3,4,5}
...     
>>> a.add(101)
...     
>>> a
...     
{1, 2, 3, 4, 5, 101}
>>> a.update({10,20,30,40})
...     
>>> a
...     
{1, 2, 3, 4, 5, 101, 40, 10, 20, 30}
>>> a.pop()
...     
1
>>> a.pop()
...     
2
>>> a
...     
{3, 4, 5, 101, 40, 10, 20, 30}
>>> a.remove(101)
...     
>>> a
...     
{3, 4, 5, 40, 10, 20, 30}
>>> a.discard(101)
...     
>>> a.discard(4)
...     
>>> a
...     
{3, 5, 40, 10, 20, 30}
>>> a.clear()
...     
>>> a
...     
set()
>>> #frozenset
...     
>>> a = frozenset({1,2,3,4})
...     
>>> a
...     
frozenset({1, 2, 3, 4})
>>> #cannot be changed always stays constant
...     
