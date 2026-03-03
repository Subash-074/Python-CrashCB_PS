#Method 1 of using composition 
# Small small object combines to form a one big object  that concept is composition in python 




#  class Engine:
#       a=10
#       def __init__(self):
#             self.b=20
#       def m1(self):
#             print("This is engine ")
# class Car:
#       def __init__(self):
#             self.engine=Engine()
#       def m2(self):
#             print("Car object using engine object ")
#             print(self.engine.a)
#             print(self.engine.b)
#             self.engine.m1()

# c=Car()

# c.m2()


#MEthod 2 of using composition 
# class Car:
#       def __init__(self, name, model, color):
#             self.name=name
#             self.model=model
#             self.color=color
#       def getinfo(self):
#             print(f"Car Name: {self.name}\n Car Model :{self.model}\n Car Color: {self.color}")

# class Employee:
#       def __init__(self, ename, eno, car):
#             self.ename=ename
#             self.eno=eno
#             self.car=car
#       def empinfo(self):
#             print("Employee Name: ", self.ename)
#             print("Employee Numebr: ", self.eno)            
#             print("Employee car Information ")
#             self.car.getinfo()

# c=Car("Tesla", "V2", "Red")
# e=Employee("Ramesh", "e550", c)
# e.empinfo()




#Method 3 of using composition 

class X:
      a=10
      def __init__(self):
          self.b=20
      def m1(self):
          print("Class X method ")
class Y:
      c=30
      def __init__(self):
            self.d=40
      def m2(self):
            print("Class Y m2 method ")
      def m3(self):
            x1=X()
            print(x1.a)
            print(x1.b)
            x1.m1()
            print(Y.c)
            print(self.d)
            self.m2()
            print("class Y m3 method")

y=Y()
y.m3()


