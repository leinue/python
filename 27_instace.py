from classtools import AttrDisplay
class person(AttrDisplay):
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay=int(self.pay*(1+percent))
    '''def __str__(self):
        return '[Person:%s %s]' % (self.name,self.pay)'''

class Manager(person):
    def __init__(self,name,pay):
        person.__init__(self,name,'mgr',pay)
    def giveRaise(self,percent,bonus=.10):
        person.giveRaise(self,percent+bonus)

class Department:
    def __init__(self,*args):
        self.members=list(args)
    def addMember(self,person):
        self.members.append(person)
    def giveRaise(self,percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__=='__main__':
    bob=person("bob shit")
    fuck=person('fuck',job='enginner',pay=2000)
    print(bob.name.split()[-1],bob.pay)
    print(fuck.name,fuck.job,fuck.pay*10)
    print(bob)
    Tom=Manager('tom jones',50000)
    Tom.giveRaise(.10)
    print(Tom.lastName())
    print(Tom)
    print('----all three----')
    for obj in (bob,fuck,Tom):
        obj.giveRaise(.10)
        print(obj)
    print('----department----')
    development=Department(bob,fuck)
    development.addMember(Tom)
    development.giveRaise(.10)
    development.showAll()

    import shelve
    db=shelve.open('persondb')
    for obj in (bob,fuck,Tom):
        db[obj.name]=obj
    db.close()
