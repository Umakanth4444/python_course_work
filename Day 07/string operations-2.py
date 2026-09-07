Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = '    hello world    '
s.strip()
'hello world'
s.lstrip()
'hello world    '
s.rstrip()
'    hello world'
s.replace(' ','')
'helloworld'
s
'    hello world    '
s.replace(' ','-')
'----hello-world----'
s = 'python-java-c-c++-.net')
SyntaxError: unmatched ')'
s = 'python-java-c-c++-.net'
s.split('-')
['python', 'java', 'c', 'c++', '.net']
s.split('-',2)
['python', 'java', 'c-c++-.net']
s.rsplit('-',2)
['python-java-c', 'c++', '.net']

l = '''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
c
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    c
NameError: name 'c' is not defined
''.join(l)
'python\njava\nmysql\nflask\n'
c = ['python', 'java', 'mysql', 'flask']
''.join(c)
'pythonjavamysqlflask'
' '.join(c)
'python java mysql flask'
', '.join(c)
'python, java, mysql, flask'
'@'.join(c)
'python@java@mysql@flask'
'-'.join(('1','2','3'))
'1-2-3'
a = 'strings.py'
'-'.join({'1','2','3'})
'3-2-1'
a.partition(.)
SyntaxError: invalid syntax
a.partition('.')
('strings', '.', 'py')
a = 'string.py.java.png.txt'
a
'string.py.java.png.txt'
a.partition('.')
('string', '.', 'py.java.png.txt')
a.rpartition('.')
('string.py.java.png', '.', 'txt')
s = 'strings.png'
s,startswith('png')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s,startswith('png')
NameError: name 'startswith' is not defined
s.startswith('list')
False
s.endswith('.py')
False
s.endswith('png')
True
'python.13'.islower()
True
'Python.1223e'.isupper()
False
>>> 'Python.1223e'.iscapitalize()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    'Python.1223e'.iscapitalize()
AttributeError: 'str' object has no attribute 'iscapitalize'. Did you mean: 'capitalize'?
>>> 'Python.1223e'.isCapitalize()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    'Python.1223e'.isCapitalize()
AttributeError: 'str' object has no attribute 'isCapitalize'. Did you mean: 'capitalize'?
>>> 'python.122'.istitle()
False
>>> 'Python.1223e'.isalpha()
False
>>> 'python'.isalpha()
True
>>> '123'.isalnum()
True
>>> 'oyathind123'.isalnum()
True
>>> #both alphabates and numbers in the string
>>> '     '.isspace()
True
>>> '     Hallo'.isspace()
False
>>> #only containg space entirely is True not other than the space
>>> 'my_var'.isidentifier
<built-in method isidentifier of str object at 0x00000132F2637240>
>>> 'my_var'.is_identifier()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    'my_var'.is_identifier()
AttributeError: 'str' object has no attribute 'is_identifier'. Did you mean: 'isidentifier'?
>>> 'my_var'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> '12344'.isdecimal()
True
>>> '12jde'.isdecimal()
False
>>> '9876'.isdigit()
True
>>> '9876'.isnumeric()
True
