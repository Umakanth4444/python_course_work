Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = "codegnan"
s
'codegnan'
t = "institution"
s+t
'codegnaninstitution'
#concatination('+')

#repetition:
a = "Metal"
a*10
'MetalMetalMetalMetalMetalMetalMetalMetalMetalMetal'
#repeated string
b = !
SyntaxError: invalid syntax
b = "!"
b*4
'!!!!'
'!'*5
'!!!!!'
#slicing
names= "anu janu mani ali sam liam"
a = "codegnan"
a[1]
'o'
a[-1]
'n'
a[-4]
'g'
names
'anu janu mani ali sam liam'
names[:4]
'anu '
names[:3]
'anu'
names[4:8]
'janu'
names[9:13]
'mani'
names[14:17]
'ali'
names[18:21]
'sam'
names[22:26]
'liam'
names[1:14:1]
'nu janu mani '
names[:14:1]
'anu janu mani '
names[:13:1]
'anu janu mani'
names[4::1]
'janu mani ali sam liam'
names[-1:-9:-1]
'mail mas'
names[-1:-27:-1]
'mail mas ila inam unaj una'
names[-6:-24:-1]
'mas ila inam unaj '
names[-6:-23:-1]
'mas ila inam unaj'
names[-4::1]
'liam'
#[index starting, len(+1), step):
len(names)
26
ord('a')
97
ord('a,b')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    ord('a,b')
TypeError: ord() expected a character, but string of length 3 found
ord(f"{a,b}")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    ord(f"{a,b}")
TypeError: ord() expected a character, but string of length 17 found
ord("A")
65
ord(1)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ord(1)
TypeError: ord() expected string of length 1, but int found
ord("!")
33
ord("1")
49
chr(10)
'\n'
chr(9)
'\t'
chr(100)
'd'
chr(20)
'\x14'
chr(30)
'\x1e'
sorted(names)
[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'i', 'i', 'i', 'j', 'l', 'l', 'm', 'm', 'm', 'n', 'n', 'n', 's', 'u', 'u']
count(sorted(names))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    count(sorted(names))
NameError: name 'count' is not defined. Did you mean: 'round'?
max(names)
'u'
min(names)
' '
#order,character,sorted,maximum,minimum



#case conversion
s = 'python Programming language'
s.upper()
'PYTHON PROGRAMMING LANGUAGE'
s.lower()
'python programming language'
s.swap()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s.swap()
AttributeError: 'str' object has no attribute 'swap'
s.swapcase()
'PYTHON pROGRAMMING LANGUAGE'
s.swapcase()
'PYTHON pROGRAMMING LANGUAGE'
s.capitalize()
'Python programming language'
s.title()
'Python Programming Language'
text = "Hello, Python World!"
print(text.casefold())
hello, python world!
s
'python Programming language'
s.center(50,'-')
'-----------python Programming language------------'
s.ljust(50,'-')
'python Programming language-----------------------'
s.rjust(50,'-')
'-----------------------python Programming language'
'123'.zfill(4)#4digit
'0123'
'65'.zfill(5)
'00065'
'8'.zfill(2)
'08'
'8765432'.zfill(2)
'8765432'
#center,ljust,rjust,zfill
s
'python Programming language'
s.find('python')
0
>>> s.find('p')
0
>>> s.find('r')
8
>>> s.rfind('g')
25
>>> s.rfind('n')
21
>>> s.find('z')
-1
>>> s.index('a')
12
>>> s.rindex('r')
11
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> #find is prefered because the value that isnt there in string give -1 instead of error which gives in index(#z)
>>> s.count(3)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s.count(3)
TypeError: count() argument 1 must be str, not int
>>> s.count('a')
3
>>> s.count('p')
1
>>> s.count('ng')
2
>>> #frequence of the given string
>>> s.replace('o','1')
'pyth1n Pr1gramming language'
>>> s.replace('m','code')
'python Progracodecodeing language'
>>> s.maketrans('aeiou','!@#$%')
{97: 33, 101: 64, 105: 35, 111: 36, 117: 37}
>>> s.translate(s.maketrans('aeiou','!@#$%'))
'pyth$n Pr$gr!mm#ng l!ng%!g@'
>>> #Encode and Decode
>>> text = 'Python 🐍 is super fast 🚀 and fun!'
>>> text.encode()
b'Python \xf0\x9f\x90\x8d is super fast \xf0\x9f\x9a\x80 and fun!'
>>> b'Python \xf0\x9f\x90\x8d is super fast \xf0\x9f\x9a\x80 and fun!'.decode()
'Python 🐍 is super fast 🚀 and fun!'
