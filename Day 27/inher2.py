'''class Whatsappv1:
    def status(self):
        print("You can upload a story for 24hr")
class Whatsappv2(Whatsappv1):
    def status(self):
        super().status()#this super method makes to access the same method used in parent class and print it 
        #this is only applicable if the method is same
        print("You add music and you can react")
a = Whatsappv1()
a.status()

b = Whatsappv2()
b.status()#if we dont use super then we can only get v2 print even bcoz of same method(status)'''
'''if we use the super the output will be
You can upload a story for 24hr 
You can upload a story for 24hr 
You add music and you can react'''

class Whatsappv1:
    def status(self):
        print("You can upload a story for 24hr")

class Whatsappv2:
    def status(self):
        print("You add music and you can react")

class Whatsappv3(Whatsappv1,Whatsappv2):
    def status(self):
        Whatsappv1.status(self)#class method to get access of status method in parents classes bcoz super method can be only used for single parent
        Whatsappv2.status(self)
        print("You can add cross platforms")

a = Whatsappv3()
a.status()
