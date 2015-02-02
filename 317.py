class Customer:
    def __init__(self):pass
    def placeOrder(self,foodName,employee):
        self.name=foodName
        employee.takeOrder(foodName)
    def printFood(self):
        print(self.name)
class Employee:
    def takeOrder(self,foodName):
        food=Food(foodName)

class Food:
    def __init__(self,name):
        self.food=name

class Lunch:
    def __init__(self):
        self.customer=Customer()
        self.employee=Employee()
    def order(self,foodName):
        self.customer.placeOrder(foodName,self.employee)
    def result(self):
        self.customer.printFood()

lunch=Lunch()
lunch.order('bitch')
lunch.result()
