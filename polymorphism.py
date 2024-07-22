#POLYMORPHISM:More than one form
# same funtion name different parameter overriding
#same parameter different function overloading

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'{self.name},{self.age}'
    
class Student(Person):
    def __init__(self,name,age,roll,branch):
        super().__init__(name,age)
        self.roll=roll
        self.branch=branch
        
    def __str__(self):
        perdetails=super().__str__()
        return f'{perdetails},{self.roll},{self.branch}'
#3
class AnnualDay(Student):
    def __init__(self,name,age,roll,branch,program):
        super().__init__(name,age,roll,branch)
        self.program=program
        
    def __str__(self):
        studetails=super().__str__()
        return f'{studetails},{self.program}'
aobj=AnnualDay('john',20,'68','cse','solo')
print(aobj) #3


#2
#obj=Person('rishika',111)
#print(obj)

#1
#obj=Student('john',26,111,'CSE')
#print(obj)
