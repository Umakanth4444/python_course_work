Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l = []
l = list()
type()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
type(l)
<class 'list'>
l = [1,2.3,"str",True,[1,2,3],(1,2,3,3),(1,2,3),{1:1,2:2,3:3},3+8j]
l
[1, 2.3, 'str', True, [1, 2, 3], (1, 2, 3, 3), (1, 2, 3), {1: 1, 2: 2, 3: 3}, (3+8j)]
l = [1,1,1,1]
l
[1, 1, 1, 1]
a =[1,2,3]
b = [4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a*b
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'list'
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a
[1, 2, 3]
a = [567, 33, 24, 77, 83, 44]
a[1]
33
a[4]
83
a[-1]
44
a[]
SyntaxError: invalid syntax
a[:6]
[567, 33, 24, 77, 83, 44]
a[1:4]
[33, 24, 77]
a[::-1]
[44, 83, 77, 24, 33, 567]
a[-1:-5:-1]
[44, 83, 77, 24]
a[:-4:-1]
[44, 83, 77]
a[::2]
[567, 24, 83]
a[::3]
[567, 77]
a[-1::-2]
[44, 77, 33]
a[2::3]
[24, 44]
76 in a:
    
SyntaxError: invalid syntax
76 in a
False
44 in a
True
l
[1, 1, 1, 1]
a
[567, 33, 24, 77, 83, 44]
max(a)
567
min(a)
24
sort(a)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    sort(a)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
sortd(a)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    sortd(a)
NameError: name 'sortd' is not defined. Did you mean: 'sorted'?
sorted(a)
[24, 33, 44, 77, 83, 567]
len(a)
6
id(a)
1864723982464
a[0] = 56
a
[56, 33, 24, 77, 83, 44]
id(a)
1864723982464
a.append(60)

a
[56, 33, 24, 77, 83, 44, 60]
a.insert(2,40)
a
[56, 33, 40, 24, 77, 83, 44, 60]
a.insert(3,70)
a
[56, 33, 40, 70, 24, 77, 83, 44, 60]
a,extend(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a,extend(1,2,3,4)
NameError: name 'extend' is not defined
a.extend([1,2,3,4])
a
[56, 33, 40, 70, 24, 77, 83, 44, 60, 1, 2, 3, 4]
a.pop()
4
a.pop()
3
a
[56, 33, 40, 70, 24, 77, 83, 44, 60, 1, 2]
a.pop(-3)
60
a
[56, 33, 40, 70, 24, 77, 83, 44, 1, 2]
a.pop(2)
40
a
[56, 33, 70, 24, 77, 83, 44, 1, 2]
a.remove(70)
a
[56, 33, 24, 77, 83, 44, 1, 2]
a.delete()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.delete()
AttributeError: 'list' object has no attribute 'delete'
del a[1]
a
[56, 24, 77, 83, 44, 1, 2]
a.clear()
a
[]
id(a)
1864723982464
#mutable,:modif
a = [56, 24, 77, 83, 44, 1, 2]
del a[:4]
a
[44, 1, 2]
a = [56, 24, 77, 83, 44, 1, 2]
a.index(1)
5
a
[56, 24, 77, 83, 44, 1, 2]
a.count(56)
1
a = [56, 24, 77, 83, 44, 1, 2, 24]
>>> a.count(24)
2
>>> a=b
>>> b
[4, 5, 6]
>>> a
[4, 5, 6]
>>> b.append(23)
>>> b
[4, 5, 6, 23]
>>> a
[4, 5, 6, 23]
>>> #after changig b the a is also effecting wiyth using methods on b
>>> #so use copy
>>> a
[4, 5, 6, 23]
>>> b = copy(a)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    b = copy(a)
NameError: name 'copy' is not defined. Did you forget to import 'copy'?
>>> b = a.copy()
>>> b.append(21)
>>> b
[4, 5, 6, 23, 21]
>>> a
[4, 5, 6, 23]
>>> any(a)
True
>>> all(a)
True
>>> any([1,'',False,[],(),{},set()])#true,false,false,false,false,false,false
True
>>> any([0,'',False,[],(),{},set()])#false,false,false,false,false,false,false
False
>>> #in any atleast one should be true so any be true
>>> all([0,'',False,[],(),{},set()])
False
>>> any([1,'',False,[],(),{},set()])
True
>>> a.sort()
>>> a
[4, 5, 6, 23]
>>> a.reverse()
>>> a
[23, 6, 5, 4]
