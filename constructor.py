'''class Employe:
    def __init__(self,name,salary,address,phoneno):
       self.name=name
       self.salary=salary
       self.address=address
       self.phoneno=phoneno
    def display(self):
        print('name is:',self.name)
        print('salary is:',self.salary)
        print('address is:',self.address)
        print('phoneno is:',self.phoneno)
E1=Employe('Rishika',500000,'hyderabad',9989911215)
E1.display()'''
    

# static 
'''class Student:
    #static data
    branch='CSE'
    def __init__(self,name,roll,address,phoneno):
       self.name=name
       self.roll=roll
       self.address=address
       self.phoneno=phoneno
    def display(self):
        print('name is:',self.name)
        print('roll is:',self.roll)
        print('branch is:',self.branch)
        print('address is:',self.address)
        print('phoneno is:',self.phoneno)
S1=Student('Rishika',111,'hyderabad',9989911215)
S2=Student('komal',112,'hyderabad',9911225676)
S1.display()
S2.display()'''



# With out using display
class Student:
    #static data
    branch='CSE'
    def __init__(self,name,roll,address,phoneno):
       self.name=name
       self.roll=roll
       self.address=address
       self.phoneno=phoneno
    def __str__(self):
        return f'{self.name} {self.roll} {Student.branch} {self.address} {self.phoneno}'
s1=Student('Rishika',111,'hyderabad',9989911215)
s2=Student('komal',112,'hyderabad',9911225676)
print(s1)
print(s2)

    
