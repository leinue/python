import random

class island(object):

    def __init__(self,n,preyCnt=1,predatorCnt=1):
        self.gridSize=n
        self.grid=[]
        for i in range(n):
            row=[0]*n
            self.grid.append(row)
        self.initAnimals(preyCnt,predatorCnt)

    def size(self):
        return self.gridSize

    def register(self,animal):
        x=animal.x
        y=animal.y
        self.grid[x][y]=animal
    
    def __str__(self):
        s=''
        for j in range(self.gridSize-1,-1,-1):
            for i in range(self.gridSize):
                if not self.grid[i][j]:
                    s+="%-2s"%'x'+"    "
                else:
                    s+="%-2s"%str(self.grid[i][j])+"    "
            s+="\r\n"

        return s

    def initAnimals(self,preyCnt,predatorCnt):
        cnt=0

        while cnt<preyCnt:
            x=random.randint(0,self.gridSize-1)
            y=random.randint(0,self.gridSize-1)
            if not self.animal(x,y):
                newPrey=prey(island=self,x=y,y=y)
                cnt+=1
                self.register(newPrey)
        cnt=0
        while cnt<predatorCnt:
            x=random.randint(0,self.gridSize-1)
            y=random.randint(0,self.gridSize-1)
            if not self.animal(x,y):
                newPredator=predator(island=self,x=y,y=y)
                cnt+=1
                self.register(newPredator)        
        
    def animal(self,x,y):
        if 0<=x<self.gridSize and 0<=y<self.gridSize:
            return self.grid[x][y]
        else:return -1

    def remove(self,x,y):
        self.grid[x][y]=0
        
class animal(object):
    def __init__(self,island,x=0,y=0,s='a'):
        self.island=island
        self.name=s
        self.x=x
        self.y=y

    def __str__(self):
        return self.name

    def pos(self):
        return self.x,self.y

    def move(self):
        offset=[(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        for i in range(len(offset)):
            x=self.x+offset[i][0]
            y=self.y+offset[i][1]
            if self.island.animal(x,y)==0:
                self.island.remove(self.x,self.y)
                self.x=x
                self.y=y
                self.island.register(self)
                break

class prey(animal):
    def __init__(self,island,x=0,y=0,s='o'):
        animal.__init__(self,island,x,y,s)

class predator(animal):
    def __init__(self,island,x=0,y=0,s='p'):
        animal.__init__(self,island,x,y,s)


    #o=prey p=predator
    royale=island(15,1,1)
    timeSteps=20

    islandSize=royale.size()
    cnt=0
    while cnt<timeSteps:
        print (royale)
        for x in range(islandSize):
            animal=royale.animal(x,y)
            if animal:
                animal.move()

