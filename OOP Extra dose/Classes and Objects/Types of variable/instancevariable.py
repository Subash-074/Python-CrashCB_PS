#Instance Variable 
#Those variable whose value are different in object to object then that type of variable are called instance variable 

#For every object a seperate copy of instance variable is created 
#Instance variable are always declared by using refrence variable 


class Employee:
      def __init__(self):
            self.eno=100
            self.name='Ramesh'
            self.salary=30000

      def comp(self):
            self.comp=8848
e=Employee()
e.comp()
#outside the class 
e.month="jan"
print(e.__dict__)


#Accessing instance variable
class Test:
      def __init__(self):
            self.a=10
            self.b=20
      def display(self):
            print(self.a)
            print(self.b)

t=Test()
t.display()
print(t.a, t.b)


#deleting instanve variable

class Exam:
      def __init__(self):
            self.d=10
            self.e=20
            self.f=30
            self.g=40
            self.h=50
      def m2(self):
            del self.f     

t=Exam()
t1=Exam()
t.m2()
del t.h
print(t.__dict__)
print(t1.__dict__)

