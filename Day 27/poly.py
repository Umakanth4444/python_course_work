#method overloading
#Method overriding:below example
class Hotstar:
    def __init__(self,name):
        print("Welcome to hotstar, ",name)
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("You can see dash board")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("Pause play resume")
    def access(self):
        print("You can see limited movies")
    def quality(self):
        print("You can see lowquality")
    def download(self):
        print("You can't download")
    def ads(self):
        print("You can see ads")
    def devices(self):
        print("Single device login")


class PremiumHotstar(Hotstar):
    def __init__(self,name):
        print("Welcome to Premium hotstar, ",name)
    def access(self):
        print("You can see Unlimited movies")
    def quality(self):
        print("You can see in High quality")
    def download(self):
        print("You can download")
    def ads(self):
        print("You can't see ads")
    def devices(self):
        print("Multiple device login")

a = Hotstar("a")
a.auth()
a.dashboard()
a.search()
a.history()
a.playcontrollers()
a.access()
a.quality()
a.download()
a.ads()
a.devices()
print()
b = PremiumHotstar("B")
b.auth()
b.dashboard()
b.search()
b.history()
b.playcontrollers()
b.access()
b.quality()
b.download()
b.ads()
b.devices()
    
