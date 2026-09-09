''''
pub -> inclass,child class,outside the class
pri -> inclass
pri -> inclass,child class,outside the class(not recommended)


'''


class Instagram:
    def __init__(self,username,password):#constructor is a special method that can be automatically called when creating an object(__init__)
        self.username = username #self.variable represents the public
        self.__password = password #self.__variable represents the private
        self._post = [] #self._variable represents the protected

    def getpassword(self):#we cannot directly accesed on password which is a private so use this method
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

    @property#need to use a property to able to access the protected self._post if using 
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)


    
lohitha = Instagram("Lohitha","1234567")

print(lohitha.username)
print(lohitha.getpassword())#cant use lohitha.__password bcoz it is a private one
print(lohitha.accesspost)#we can use this if a property used like 19 line or directly the below one for protected
print(lohitha._post)

lohitha.setpassword = "lohitha@12321"
print(lohitha.setpassword)

lohitha.accesspost = "python"
lohitha.accesspost = "sql"
lohitha.accesspost = "halamadrid"
print(lohitha.accesspost)

