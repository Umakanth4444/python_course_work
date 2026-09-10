#operator overloading :overloading the operators with objects
class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self,other):
        return self.n + other.n
    def __sub__(self,other):
        return self.n - other.n
    def __mul__(self,other):
        return self.n * other.n
    def __pow__(self,other):
        return self.n ** other.n
    def __truediv__(self,other):
        return self.n / other.n
    def __floordiv__(self,other):
        return self.n // other.n
    def __mod__(self,other):
        return self.n % other.n
    def __gt__(self,other):
        return self.n > other.n
    def __lt__(self,other):
        return self.n < other.n
    def __ge__(self,other):
        return self.n >= other.n
    def __le__(self,other):
        return self.n <= other.n
    def __eq__(self,other):
        return self.n == other.n
    def __ne__(self,other):
        return self.n != other.n
    def __str__(self):
        return str(self.n)

a = Number(5)
b = Number(10)

print(a,b)#<__main__.Number object at 0x00000142205186E0> <__main__.Number object at 0x0000014220508550> this shows if the below isnt used in class method
#def __str__(self):
        #return str(self.n)  by using this it shows in the output the values be in string
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)