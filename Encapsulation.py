#ENCAPSULATION:Binding(wrapping) data and methods into the single component is called Encapsulation
#Example:Class is the bestexample of Encapuslate
#ADVANTAGES:Code integration,security
#ACCESS MODIFIER: public anyone can access,private with in the class,protected



class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=85000 #private
    def get_salary(self): #public method private data 
        print(self.__salary)
    def Empdisplay(self):   #public method 
        print(self.name,self.role)
class Company(Employee):
    def __init__(self,cname,loc):
        self.cname=cname
        self.loc=loc
    def comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self): #protected method
        print('Hiring for the Manager Role')
cobj=Company('Wipro','Gachibowli')
eobj=Employee('Karthika','developer',85000)
eobj.Empdisplay()
print(cobj._hiring())

