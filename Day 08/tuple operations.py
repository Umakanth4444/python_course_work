Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t = ()
t = tuple()
t = (1,2,3,4)
t
(1, 2, 3, 4)
t = (1)
t
1
#need to give comma
t = (1,)
t
(1,)
type(t)
<class 'tuple'>
t = (1,1,1,1)
t
(1, 1, 1, 1)
#ordered,heterogeneous,immutable
t = (1,2.3,"str",[1,2,3],(1,2),{1,2},{1:2,3:4})
t
(1, 2.3, 'str', [1, 2, 3], (1, 2), {1, 2}, {1: 2, 3: 4})
type(t)
<class 'tuple'>
a = (1,2,3)
b = (4,5,6)
a+b
(1, 2, 3, 4, 5, 6)
a*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 2.3, 'str', [1, 2, 3], (1, 2), {1, 2}, {1: 2, 3: 4})
t(1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t(1)
TypeError: 'tuple' object is not callable
t[1]
2.3
t[-3]
(1, 2)
t[0]
1
#slicing : accesing group of elements
t(:3)
SyntaxError: invalid syntax
t[:3]
(1, 2.3, 'str')
t[-1:-4:-1]
({1: 2, 3: 4}, {1, 2}, (1, 2))
t[2::2]
('str', (1, 2), {1: 2, 3: 4})
#membership
2.3 in t
True
[1,2] in t
False
[1,2,3] in t
True
p = (12,22,32,32,12,55,44,76,99,46)
sorted(p)
[12, 12, 22, 32, 32, 44, 46, 55, 76, 99]
max(t)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'str' and 'float'
min(t)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    min(t)
TypeError: '<' not supported between instances of 'str' and 'int'
max(p)
99
>>> min(p)
12
>>> len(p)
10
>>> t
(1, 2.3, 'str', [1, 2, 3], (1, 2), {1, 2}, {1: 2, 3: 4})
>>> t.index([1,2,3])
3
>>> p.index(32)
2
>>> t.count(32)
0
>>> all([1,2,3])
True
>>> any([1,2,3])
True
>>> sum(p)
430
>>> all(1,2,3,00,0)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    all(1,2,3,00,0)
TypeError: all() takes exactly one argument (5 given)
>>> all((1,2,3,00,0))
False
>>> t = 1,2,3
>>> t
(1, 2, 3)
>>> a,b,c t
SyntaxError: invalid syntax
>>> a,b,c = t
>>> t
(1, 2, 3)
>>> t = (1,2,3,4,[1,2,3],5)
>>> t[4]
[1, 2, 3]
>>> t[4].append(5)
>>> t
(1, 2, 3, 4, [1, 2, 3, 5], 5)
