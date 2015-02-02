class Animal:
    def reply(self,what):
        print(what)

class Mammal(Animal):pass

class Dog(Mammal):
    def reply(self):
        Animal.reply('self,bark')

class Cat(Mammal):
    def reply(self):
        Animal.reply(self,'mew')

class Primate(Mammal):pass

class Hacker(Primate):
    def reply(self):
        Animal.reply(self,'hello world!')

spot=Cat()
spot.reply()

data=Hacker()
data.reply()
