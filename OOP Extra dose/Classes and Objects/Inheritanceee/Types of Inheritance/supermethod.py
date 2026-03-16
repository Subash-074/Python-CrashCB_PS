#Super method 
# class P:
#       def m1(self):
#             print("This is parent method ")
# class C(P):
#       def m1(self):
#             super().m1() #if method name is different in parent class and child class then no need of super. 
      
#             print("This is child method ")
      
# c=C()
# c.m1()
 

# class P:
#       a=10
#       def __init__(self):
#             self.b=20
#             print("Patent constructor is called ") 
#       def m1(self):
#             print("Parent class instance method is called ")   
#       @classmethod
#       def m2(cls):
#             print("Parent class class method is called ")

#       @staticmethod
#       def m3():
#             print("Parent class static method ")


# class C(P):
#       a=555
#       def __init__(self):
#             self.b=666
#             print("Child constructor is called ")

#             #if child class also use the same method name and variable than to access parent class methods we can use super method to access parent class methods in child class. 
#             super().__init__()
#             super().m1()
#             super().m2()
#             super().m3()
# c=C()
# c.m1()
# print(c.b)

# class Person:
#       def __init__(self, name, age):
#             self.name=name
#             self.age=age
#       def display(self):
#             print("Name:", self.name)
#             print("Age: ", self.age)
# class Student(Person):
#       def __init__(self, name, age, roll, mark):
#             super().__init__(name, age)
#             self.roll=roll
#             self.mark=mark
#       def display(self):
#             super().display()
#             print("Roll Number : ", self.roll)
#             print("Marks :", self.mark)


# s=Student("Pragyan", 20, 101, 99)
# s.display()



class A:
      def m1(self):
            print("A clas method ")
class B(A):
      def m1(self):
            print("B clas method ")
class C(B):
      def m1(self):
            print("C clas method ")
class D(C):
      def m1(self):
            print("D clas method ")
class E(D):
      def m1(self):
            print("E clas method ")
      