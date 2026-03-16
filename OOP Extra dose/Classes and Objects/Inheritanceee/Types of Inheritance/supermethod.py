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



# class A:
#       def m1(self):
#             print("A clas method ")
# class B(A):
#       def m1(self):
#             print("B clas method ")
# class C(B):
#       def m1(self):
#             print("C clas method ")
# class D(C):
#       def m1(self):
#             print("D clas method ")
# class E(D):
#       def m1(self):
#             # super().m1()# m1 method from inherited class D gets priority first 
#             # A.m1(self) #We directly called m1 method from class A 
#             super(B, self).m1() #we used super method and gave Class name and self parameter followed by m1 method. 

#             #these are the three different methods we can use to call desired methods from any class inside method of other class. 
#             print("E clas method ")

# e=E()
# e.m1()
      







#loopholes of super method 
#Case 1: From child class we are not allowed to access parent class instance variable by super(), compulsorarily we should use self only. use when there is class variable/static variable in parent class ===super() to access parent class form child class
# # In a child class, parent instance variables should be accessed using self, while super() is used to access parent methods and class/static variables..


# class P:
#       a=10
#       def __init__(self):
#             self.b=20

# class C(P):
#       def m1(self):
#             print(super().a)# this is valid 
#             # print(super().b) this is invalid instead we should use 
#             print(self.b)
# c=C()
# c.m1()








#case 2:From a child class (constructor or instance method), we can access the parent class’s instance, class, and static methods using super()

# class P:
#       def __init__(self):
#             print("Parent class constructor ")
#       def m1(self):
#             print("Parent class instance method")
#       @classmethod
#       def m2(cls):
#             print("Parent class class method ")
#       @staticmethod
#       def m3():
#             print("Parent class static method ")

# class C(P):
#       def __init__(self):#from the constructor of child class 
#             super().__init__()#we called constructor of parent class P 
#             super().m1()# we called m1 instance method of parent class P
#             super().m2()#we called class method 
#             super().m3()#we called static method 
#       def m1(self): #from instance method of child class also we can call and access parent class's constructor, instance, class, and static method 
#             super().__init__()
#             super().m1()
#             super().m2()
#             super().m3()


# c=C()
# c.m1()







#Case 3: From child class's class method, we cannot access parent class's- instance method and constructor by using super() directly(note indirectly it is possible), But,  we can access class/static method using super().

# class P:
#     def __init__(self):
#         print("Parent class constructor ")
#     def m1(self):
#         print("Parent class instance method")
#     @classmethod
#     def m2(cls):
#         print("Parent class class method ")
#     @staticmethod
#     def m3():
#         print("Parent class static method ")

# class C(P):
#     @classmethod 
#     def m1(cls): #inside class method of child class 
#       #   super().__init__() this is invalid
#       # super().m1() this is also invalid 
#       # super.m2() valid
#       # super.m3() valid
#       super(C, cls).__init__(cls)#indirect way to call parent class constructor 
#       super(C, cls).m1(cls)#indirect way to call parent class instance method 


# c = C()
# c.m1()


#case 4: In child class static methods we are not allowed to use super() generally but we can super method  in a special way


# class P:
#     def __init__(self):
#         print("Parent class constructor ")
#     def m1(self):
#         print("Parent class instance method")
#     @classmethod
#     def m2(cls):
#         print("Parent class class method ")
#     @staticmethod
#     def m3():
#         print("Parent class static method ")

# class C(P):
#     @staticmethod
#     def m1(self):
#       #   super().m1()#invalid 
#       #   super().m3()#invalid
#       super(C, C).m2()#indirect way 
#       super(C, C).m2()#indirect way
# c=C()
# c.m1()
