Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
i = 3
float(i)
3.0
complex(i)
(3+0j)
boolean(i)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    boolean(i)
NameError: name 'boolean' is not defined
bool(i)
True
list(i)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(i)
TypeError: 'int' object is not iterable
tuple(i)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(i)
TypeError: 'int' object is not iterable
set(i)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(i)
TypeError: 'int' object is not iterable
dict(i)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(i)
TypeError: 'int' object is not iterable
#float
f = 1.0
int(f)
1
complex(f)
(1+0j)
bool(f)
True
list(f)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
#complex
c = 1+2j
int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
bool(c)
True
list(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
#boolean
b = True
int(b)
1
float(b)
1.0
complex(b)
(1+0j)
list(b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    tuple(b)
TypeError: 'bool' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    set(b)
TypeError: 'bool' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict(b)
TypeError: 'bool' object is not iterable
#list
l = [1,2,3,4]
int(l)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
bool(l)
True
tuple(l)
(1, 2, 3, 4)
set(l)
{1, 2, 3, 4}
dict(l)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
#tuple
t = (1,2,3)
int(t)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
bool(t)
True
list(t)
[1, 2, 3]
set(t)
{1, 2, 3}
dict(t)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
#set
s = {1,2,3}
int(s)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    complex(s)
TypeError: complex() argument must be a string or a number, not set
bool(s)
True
list(s)
[1, 2, 3]
tuple(s)
(1, 2, 3)
dict(s)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
#dict
int(dict)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    int(dict)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'type'
d = {'a':1,'b':2}
int(d)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    complex(d)
TypeError: complex() argument must be a string or a number, not dict
bool(d)
True
list(d)
['a', 'b']
tuple(d)
('a', 'b')
set(d)
{'a', 'b'}
str(d)
"{'a': 1, 'b': 2}"
#string
s = '24'
str = 'abc'
int(s)
24
int(str)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    int(str)
ValueError: invalid literal for int() with base 10: 'abc'
float(s)
24.0
>>> float(str)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    float(str)
ValueError: could not convert string to float: 'abc'
>>> complex(s)
(24+0j)
>>> complex(str)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    complex(str)
ValueError: complex() arg is a malformed string
>>> bool(s)
True
>>> bool(str)
True
>>> list(s)
['2', '4']
>>> list(str)
['a', 'b', 'c']
>>> tuple(s)
('2', '4')
>>> tuple(str)
('a', 'b', 'c')
>>> set(s)
{'4', '2'}
>>> set(str)
{'a', 'b', 'c'}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> dict(str)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    dict(str)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> #Any data type can be converted into string
>>> #in boolean True is other than 0 and False is 0
>>> str(i)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    str(i)
TypeError: 'str' object is not callable
