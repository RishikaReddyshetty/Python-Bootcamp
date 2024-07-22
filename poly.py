#POLYMORPHISM:More than one form

class Person:
    def _init_(self,name,age):
        self.name=name
        self.age=age

    def _str_(self):
        return f'(self.name),(self.age)'
class Student(Person):
    def _init_(self,name,age,roll,branch):
        super()._init_(name,age)
        self.roll=roll
        self.branch=branch
    def _str_(self):
        perdetails=super()._str_()
        return f'(perdetails),(self.roll),(self.branch)'

class AnnualDay(Student):
    def _init_(self,name,age,roll,branch,program):
        super()._init_(name,age,roll,branch)
        self.program=program
    def _str_(self):
        studetails=super().__str()
        return f'(studetails),(self.program)'
aobj=AnnualDay('john',20,'68','cse','solo')
print(aobj)















  #obj=person('name',444)
       # print(person)      
