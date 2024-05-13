import math
import pylint


class Line:

    def __init__(self, coor1 = (0,0), coor2 = (0,)):

        self.coor1 = coor1
        self.coor2 = coor2
        
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
        
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
    
# m_line = Line((3,2), (8,10))

# print(m_line.slope())
# print(m_line.distance())
##########################################################################################

##### Opens Cylinder class 
class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * self.radius**2 * self.height
    
    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius**2)
    
# m_cylinder = Cylinder(2,3)
# print(m_cylinder.volume())
# print(m_cylinder.surface_area())

##########################################################################################


class BankAccount:

    def __init__(self, owner='', balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance = self.balance + deposit
    
    def withdraw(self, withdraw):
        if(self.balance - withdraw) < 0:
            print("Cant withdraw - minus")
        else:
            self.balance = self.balance - withdraw
    
    def get_balance(self):
        return self.balance
    
    def get_owner(self):
        return self.owner
    

# my_bank = BankAccount(balance = 100, owner="oshkosh")
# print(my_bank.get_balance())
# (my_bank.deposit(100))
# print(my_bank.get_balance())
# (my_bank.withdraw(75))
# print(my_bank.get_balance())
# my_bank.withdraw(200)

##########################################################################################