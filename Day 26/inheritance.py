#single inherutance
'''class Whatsappv1:
    def message(sef):
        print("You can send a message")
class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload a story for 24hr")

lohitha = Whatsappv1()
lohitha.message()

usha = Whatsappv2()
usha.status()
usha.message()'''

#multilevel:parent to child and another child
'''
Multilevel inheritance means a class inherits from another derived class, forming a chain of inheritance.

For example:

Class A → Class B → Class C

Class B inherits from Class A.
Class C inherits from Class B.
Therefore, Class C can access features inherited from both B and A.
''' '''
class Whatsappv1:
    def message(sef):
        print("You can send a message")
class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload a story for 24hr")

class Whatsappv3(Whatsappv2):#makes inheriting both the previous classes which already did take the 1st class
    def group(self):
        print("You can create a group")
        

lohitha = Whatsappv1()
lohitha.message()

usha = Whatsappv2()
usha.status()
usha.message()

mouna = Whatsappv3()
mouna.group()
mouna.message()
mouna.status()
'''
#multiple: manyparents single child
'''
class Whatsappv1:
    def message(sef):
        print("You can send a message")
class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload a story for 24hr")

class Whatsappv3:#makes inheriting both the previous classes which already did take the 1st class
    def group(self):
        print("You can create a group")

class Whatsappv4:
    def community(self):
        print("You can combine multiple groups")

class Whatsappv5(Whatsappv4,Whatsappv3,Whatsappv2):
    def channel(self):
        print("You can create channels")
        

lohitha = Whatsappv1()
lohitha.message()

usha = Whatsappv2()
usha.status()
usha.message()

mouna = Whatsappv3()
mouna.group()


janu = Whatsappv5()
janu.channel()
janu.community()
janu.group()
janu.status()
janu.message()
#this example can be multiple,multilevel and a hybrid inheritance example
#because v5 has inherited multiple parent classes:multiple
#also v5 has inerited v2 class which already inherited v1:multilevel
#having the inheritance of both multiple and multilevel inheritances makes this as a hybrid inheritance too

'''

#Hierarchy:single parent and multiple child
class Whatsappv1:
    def message(sef):
        print("You can send a message")
class Whatsappv2(Whatsappv1):
    def status(self):
        print("You can upload a story for 24hr")

class Whatsappv3(Whatsappv1):#makes inheriting both the previous classes which already did take the 1st class
    def group(self):
        print("You can create a group")

class Whatsappv4(Whatsappv1):
    def community(self):
        print("You can combine multiple groups")

class Whatsappv5(Whatsappv1):
    def channel(self):
        print("You can create channels")
        

lohitha = Whatsappv1()
lohitha.message()

a = Whatsappv2()
a.status()
a.message()

b = Whatsappv3()
b.group()
b.message()
c = Whatsappv4()
c.community()
c.message()

d = Whatsappv5()
d.channel()
d.message()