Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary: collection of key value pairs enclosed in a curly bracket
#mut ord het dyn unidu
d = {}
type(d)
<class 'dict'>
d = {1:4,2:3,5:3}
d
{1: 4, 2: 3, 5: 3}
d = {}
d[1] = 1
d[2.3] =1
d[2+3j] = 1
d[True] = 1
d[(1,) = 1
  
SyntaxError: invalid syntax
d[(1,)] = 1
  
d["str"] = 1
  
d[[1,2,3]]
  
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d[[1,2,3]]
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[{1,3,2}]
  
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d[{1,3,2}]
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[{1:2,2:3}] = 1
  
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d[{1:2,2:3}] = 1
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
d
  
{1: 1, 2.3: 1, (2+3j): 1, (1,): 1, 'str': 1}
#list,set,dictionary cannot be kept because those are mutable
  
d = {}
  
d[1] = 1
  
d[1] = 2
  
d[2] = 4
  
d[0] = 8
  
d
  
{1: 2, 2: 4, 0: 8}
#in the place of the keys they cannot be same for other keys within the dict but can be same at the place of the values
  
d[1] = 1
  
d[2] = 2.3
  
d[3] = 'str'
  
d[4] = 2+3j
  
d[5] = True
  
d[6] = [1,2,3]
  
d[7] = (1,)
  
d[8] = {1,2,3}
  
d[9] = {1:2,2:3,3:4}
  
d[10] = Frozenset({1,2,3})
  
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d[10] = Frozenset({1,2,3})
NameError: name 'Frozenset' is not defined. Did you mean: 'frozenset'?
d[10] = frozenset({1,2,3})
  
d[11] = None
  
d
  
{1: 1, 2: 2.3, 0: 8, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1,), 8: {1, 2, 3}, 9: {1: 2, 2: 3, 3: 4}, 10: frozenset({1, 2, 3}), 11: None}
#membership only works on the keys not the values
  
d = {"name": "dinesh","course":"Python","marks":45}
  
"dinesh" in d
  
False
"65" in d
  
False
"marks" in d
  
True
d["name"]
  
'dinesh'
d["course"]
  
'Python'
d["age"]
  
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    d["age"]
KeyError: 'age'
#if the key isnt there it shows the error to error handle we need to use the get
  
d.get("name")
  
'dinesh'
d.("name")
  
SyntaxError: invalid syntax
d.get("course")
  
'Python'
d.get("marks")
  
45
d.get("age","age doesn't exists")
  
"age doesn't exists"
data[age] = 21
  
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    data[age] = 21
NameError: name 'data' is not defined
d[age] = 21
  
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    d[age] = 21
NameError: name 'age' is not defined
d["age"] = 21
  
d
  
{'name': 'dinesh', 'course': 'Python', 'marks': 45, 'age': 21}
d["phone"] = 9877653424
  
d
  
{'name': 'dinesh', 'course': 'Python', 'marks': 45, 'age': 21, 'phone': 9877653424}
d.update("id" : 11, "time": "12pm")
  
SyntaxError: invalid syntax
d.update("id": 11, "time": "12pm")
  
SyntaxError: invalid syntax
d.update("id" = 11, "time" = "12pm")
  
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
d.update({"id" : 11, "time": "12pm"})
  
d
  
{'name': 'dinesh', 'course': 'Python', 'marks': 45, 'age': 21, 'phone': 9877653424, 'id': 11, 'time': '12pm'}
d.update("id": 12)
  
SyntaxError: invalid syntax
d.update({"id": 9008647})
  
d
  
{'name': 'dinesh', 'course': 'Python', 'marks': 45, 'age': 21, 'phone': 9877653424, 'id': 9008647, 'time': '12pm'}
d.pop()
  
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
pop()
  
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    pop()
NameError: name 'pop' is not defined. Did you mean: 'pow'?
id(d)
  
2930230748992
d["python"]
  
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d["python"]
KeyError: 'python'
d['time']
  
'12pm'
d.popitem()
  
('time', '12pm')
d.popitem()
  
('id', 9008647)
d.popitem("marks")
  
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    d.popitem("marks")
TypeError: dict.popitem() takes no arguments (1 given)
d.pop("marks")
  
45
d
  
{'name': 'dinesh', 'course': 'Python', 'age': 21, 'phone': 9877653424}
d = {'name': 'dinesh', 'course': 'Python', 'marks': 45, 'age': 21, 'phone': 9877653424, 'id': 9008647, 'time': '12pm'}
  
len(data)
  
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    len(data)
NameError: name 'data' is not defined
len(d)
  
7
data.keys()
  
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    data.keys()
NameError: name 'data' is not defined
d.keys()
  
dict_keys(['name', 'course', 'marks', 'age', 'phone', 'id', 'time'])
d.values()
  
dict_values(['dinesh', 'Python', 45, 21, 9877653424, 9008647, '12pm'])
d.items()
  
dict_items([('name', 'dinesh'), ('course', 'Python'), ('marks', 45), ('age', 21), ('phone', 9877653424), ('id', 9008647), ('time', '12pm')])
sorted(d)
  
['age', 'course', 'id', 'marks', 'name', 'phone', 'time']
max(d)
  
'time'
min(d)
  
'age'
a = {1:!,2:2}
  
SyntaxError: invalid syntax
m = {1:1,2:2}
  
m=n
  
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    m=n
NameError: name 'n' is not defined
n=m
  
n[3] = 3
  
n
  
{1: 1, 2: 2, 3: 3}
m
  
{1: 1, 2: 2, 3: 3}
#so
  
a
  
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a
NameError: name 'a' is not defined
m
  
{1: 1, 2: 2, 3: 3}
n = m.copy()
...   
>>> n[4] = 4
...   
>>> n
...   
{1: 1, 2: 2, 3: 3, 4: 4}
>>> m
...   
{1: 1, 2: 2, 3: 3}
>>> d
...   
{'name': 'dinesh', 'course': 'Python', 'marks': 45, 'age': 21, 'phone': 9877653424, 'id': 9008647, 'time': '12pm'}
>>> d.setdefault("keys",2022)
...   
2022
>>> d
...   
{'name': 'dinesh', 'course': 'Python', 'marks': 45, 'age': 21, 'phone': 9877653424, 'id': 9008647, 'time': '12pm', 'keys': 2022}
>>> d.setdefault("top",bottom)
...   
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    d.setdefault("top",bottom)
NameError: name 'bottom' is not defined
>>> d.setdefault("top",'bottom")
...              
SyntaxError: unterminated string literal (detected at line 1)
>>> d.setdefault("top",'bottom')
...              
'bottom'
>>> d
...              
{'name': 'dinesh', 'course': 'Python', 'marks': 45, 'age': 21, 'phone': 9877653424, 'id': 9008647, 'time': '12pm', 'keys': 2022, 'top': 'bottom'}
>>> data = d.copy()
...              
>>> d.clear()
...              
>>> d
...              
{}
>>> data
...              
{'name': 'dinesh', 'course': 'Python', 'marks': 45, 'age': 21, 'phone': 9877653424, 'id': 9008647, 'time': '12pm', 'keys': 2022, 'top': 'bottom'}
>>> dict.fromkeys(["python","mysql","java"],0)
...              
{'python': 0, 'mysql': 0, 'java': 0}
