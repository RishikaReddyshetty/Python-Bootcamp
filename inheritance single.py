# Inheritance
#Types of Inheritance
#Single
#Multiple
#Multi level
#Hierarical
#Hybrid



#SINGLE INHERITANCE 
class JNTU:
     def schedule_academic(self):
         print("scheduling Academics")
     def declare_holidays(self):
         print("National and summer holidays")
     def results(self):
         print("go to www.jnturesults.com")
class Sridevi(JNTU):
    def fees(self):
        print('3rd year fee is 85k')

jobj=JNTU()
jobj.results()
#jobj.fees()
s1=Sridevi()
s1.schedule_academic()
s1.declare_holidays()
s1.fees()
