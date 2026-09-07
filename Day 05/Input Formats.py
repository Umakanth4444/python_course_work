Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#input format
#int float complex str bool list set tuple dict
a = input()
code
a
'code'
#if using input() it gives the string values
a = input("Enter a value:")
Enter a value:1234dk
a
'1234dk'
a = input("Enter a value:")
Enter a value:22
a
'22'
int(a)
22
marks = int(input("Enter marks: "))
Enter marks: 22
marks
22
cgpa = float(input("Enter cgpa: "))
Enter cgpa: 9.8
cgpa
9.8
names : "john, abraham, malik"
list(names)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    list(names)
NameError: name 'names' is not defined
names
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    names
NameError: name 'names' is not defined
names = "john, abraham, malik"
list(names)
['j', 'o', 'h', 'n', ',', ' ', 'a', 'b', 'r', 'a', 'h', 'a', 'm', ',', ' ', 'm', 'a', 'l', 'i', 'k']
names.split()
['john,', 'abraham,', 'malik']
#.split is a default for list no need to mention list as se,tuple
course = input("python-css-jave-javscript")split("-")
SyntaxError: invalid syntax
course = input("python-css-jave-javscript").split("-")
python-css-jave-javscript
course
['']
course = input(("python-css-jave-javscript").split("-"))
['python', 'css', 'jave', 'javscript']
course = set(input(("python-css-jave-javscript").split("-")))
['python', 'css', 'jave', 'javscript']
course = set(input(("python-css-jave-javscript-java").split("-")))
['python', 'css', 'jave', 'javscript', 'java']
course = set(input(("python-css-java-java").split("-")))
['python', 'css', 'java', 'java']
course = set(input("python-css-java-java").split("-"))
python-css-java-java
course = tuple(input(("python-css-java-java").split("-")))
['python', 'css', 'java', 'java']
course = tuple(input("Enter the names: ").split())
Enter the names: haliya anumula nalgonda
course
('haliya', 'anumula', 'nalgonda')
cities = set(input("Enter the names: ").split())
Enter the names: Haliya Anumula Haliya Mlg
cities
{'Haliya', 'Mlg', 'Anumula'}
#list of integers
marks = input().split()
12 34 56 7 8 9
marks
['12', '34', '56', '7', '8', '9']
['12', '34', '56', '7', '8', '9']
['12', '34', '56', '7', '8', '9']
map(int,marks)
<map object at 0x000001FAC435BE00>
list(map(int,marks))
[12, 34, 56, 7, 8, 9]
cities = list(map(int,input("Enter the city codes: ").split()))
Enter the city codes: 12 22 23 33 34 44 45
cities
[12, 22, 23, 33, 34, 44, 45]
cities = list(map(float,input("Enter the city codes: ").split()))
Enter the city codes: 1.2 2.2 2.3 3.3 3.4 4.4
cities
[1.2, 2.2, 2.3, 3.3, 3.4, 4.4]
rankings = tuple(map(int,input("Enter the rankings: ").split()))
Enter the rankings: 1 2 3 4 5 6 7
rankings
(1, 2, 3, 4, 5, 6, 7)
runners = set(map(int,input("Enter the runners codes: ").split()))
Enter the runners codes: 1 2 3 4 5 6 7 8 1 2 4 5
runners
{1, 2, 3, 4, 5, 6, 7, 8}
rankings = tuple(map(float,input("Enter the rankings: ").split()))
Enter the rankings: 2.2 1 3.4 2.2 13.5
rankings
(2.2, 1.0, 3.4, 2.2, 13.5)
runners = set(map(float,input("Enter the runners codes: ").split()))
Enter the runners codes: 1.1 1.1 2.2 3.3 4.4 7.7 4.4 2

runners
{1.1, 2.2, 3.3, 4.4, 2.0, 7.7}
#map(to change the data type into, input choosen)
#eg: map(int,marks) or marks = list(map(int,input("").split()))
'''cities = list(map(float,input("Enter the city codes: ").split()))
the above statement represents the list as converting entire data and map is used for how should we convert(float) and the input values or format(input() or marks above that statement)'''
'cities = list(map(float,input("Enter the city codes: ").split()))\nthe above statement represents the list as converting entire data and map is used for how should we convert(float) and the input values or format(input() or marks above that statement)'
a,b = [1,2]
a
1
b
2
a,b,c = [1,2,3]
a
1
b
2
c
3
a,b,c = [1,2.4,'str']
a
1
b
2.4
c
'str'
email,password = input("Enter the email,password: ").split()
Enter the email,password: john@gmail.com 112233
email,password
('john@gmail.com', '112233')
email
'john@gmail.com'
passsword
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    passsword
NameError: name 'passsword' is not defined. Did you mean: 'password'?
password
'112233'
name, marsk = input("enter name,marks: ").split(',')
enter name,marks: kanth,20
name
'kanth'
marsk
'20'
name, marks = int(input("Enter name, marks: ").split())
Enter name, marks: kanth 20
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    name, marks = int(input("Enter name, marks: ").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
int(marsk)
20
a,b,c = list(map(int,input().split()))
12 34 56
a,b,c
(12, 34, 56)
a
12
b
34
c
56
a,b,c = list(map(int,input("Enter the city codes: ").split()))
Enter the city codes: a b c
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a,b,c = list(map(int,input("Enter the city codes: ").split()))
ValueError: invalid literal for int() with base 10: 'a'
a,b,c = list(map(int,input("Enter the city codes: ").split()))
Enter the city codes: 12 34 56
a,b,c
(12, 34, 56)
a
12
b
34
>>> c
56
>>> type(a)
<class 'int'>
>>> status = eval(input())
True
>>> status
True
>>> type(status)
<class 'bool'>
>>> status = eval(input())
2+3j
>>> status
(2+3j)
>>> type(status)
<class 'complex'>
>>> status = eval(input())

Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    status = eval(input())
  File "<string>", line 0
    
SyntaxError: invalid syntax
>>> status = eval(input())
[1,2,3,4]
>>> staatus
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    staatus
NameError: name 'staatus' is not defined. Did you mean: 'status'?
>>> status
[1, 2, 3, 4]
>>> status = eval(input())
(1,2,3,4)
>>> status
(1, 2, 3, 4)
>>> type(status)
<class 'tuple'>
