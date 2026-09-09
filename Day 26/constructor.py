''''
pub -> inclass,child class,outside the class
pri -> inclass
pri -> inclass,child class,outside the class(not recommended)


'''


class Instagram:
    def __init__(self,username,password):#constructor is a special method that can be automatically called when creating an object(__init__)
        self.username = username
        self.password = password
        print(f"Welcome to instagram: {self.username}")
lohitha = Instagram("Lohitha","1234567")
mani = Instagram("Mani","mani")
chandu = Instagram("Chandu","882t782tghbedbjhd79")
