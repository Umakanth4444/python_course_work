Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 5
b = 2.4
c = 'str'
print(a,b,c)
5 2.4 str
print("a=",a,"b=",b,"c=",c)
a= 5 b= 2.4 c= str
print("a=",a,"b=",b,"c=",sep='')
a=5b=2.4c=
print("a=",a,"b=",b,"c=",sep='', end = '\n\n')
a=5b=2.4c=

print("a=",a,"b=",b,"c=",sep='\n')
a=
5
b=
2.4
c=
print("a=",a,"b=",b,"c=",sep='\t')
a=	5	b=	2.4	c=
print("a=",a,"b=",b,"c=",sep='\t', end='@')
a=	5	b=	2.4	c=@
print("a=",a,"b=",b,"c=",c,sep='\t', end='@')
a=	5	b=	2.4	c=	str@
print("a=",a,"b=",b,"c=",c,sep='\t', end='/t')
a=	5	b=	2.4	c=	str/t
>>> print("a=",a,"b=",b,"c=",sep='\t', end='\t\t')
a=	5	b=	2.4	c=		
>>> print(f'a = (a) b = (b) c = (c)')
a = (a) b = (b) c = (c)
>>> print(f'a = [a] b = [b] c = [c]')
a = [a] b = [b] c = [c]
>>> print(f'a = {a} b = {b} c = {c}')
a = 5 b = 2.4 c = str
>>> print('a = %d b = %f c = %e'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print('a = %d b = %f c = %e'%(a,b,c))
TypeError: must be real number, not str
>>> c = 10
>>> print('a = %d b = %f c = %e'%(a,b,c))
a = 5 b = 2.400000 c = 1.000000e+01
>>> print('a = %d b = %f c = %s'%(a,b,c))
a = 5 b = 2.400000 c = 10
>>> c = 'str'
>>> print('a = %d b = %f c = %s'%(a,b,c))
a = 5 b = 2.400000 c = str
>>> print('a = [] b = [] c = []',format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print('a = [] b = [] c = []',format(a,b,c))
TypeError: format expected at most 2 arguments, got 3
>>> print('a = () b = () c = ()',format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print('a = () b = () c = ()',format(a,b,c))
TypeError: format expected at most 2 arguments, got 3
>>> print('a=[] b=[] c=[]',format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print('a=[] b=[] c=[]',format(a,b,c))
TypeError: format expected at most 2 arguments, got 3
>>> print('a = () b = () c = ()'.format(a,b,c))
a = () b = () c = ()
>>> print('a = () b = () c = ()',format(b,c,a))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print('a = () b = () c = ()',format(b,c,a))
TypeError: format expected at most 2 arguments, got 3
>>> print('a = () b = () c = ()'.format(b,c,a))
a = () b = () c = ()
