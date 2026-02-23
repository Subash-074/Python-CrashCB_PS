class Student:
      def __init__(self, name, age, marks):
            self.name=name
            self.age=age
            self.marks=marks

      def info(self):
            print('Hello my name is:', self.name)
            print('Hello my age is : ', self.age)
            print('Hello my marks is', self.marks)


s=Student("Vaskar", 20, 99)
s1=Student("Dipesh", 21, 95)
s.info()
s1.info()

#Here s and s1  will have different Id 
#



"""
What is constructor?
The special method(function inside class) which have __init__  as its name is known as constructor. The first argument of constructor is self. You can take other argument name as well but self name is standard practice.

What is it's work?
Variable initialization 
one object one constructor nonly 


"""

"""
Difference between constructor and methods ?

methods 
any name 
executed if and only if we call it explicitly
per object any number of methods  
method contains business logic 

constructor
must be __init__
called automatically once object is made 
per object only one constructor 
constructor contains variable declaration, variable initialization. 

"""


list_of_std =[]

while True: 
      name=input("Enter the name: ")
      age=int(input("Enter the age: "))
      marks= int(input("Enter the marks: "))
      s=Student(name, age, marks)
      list_of_std.append(s)
      print("Student Info is Added ")
      option= input("Do you want to continue adding students? [yes/no]")
      if option.lower()=='no':
            break

print("All students info are: ")
for s in list_of_std:
      s.info()
      print()
      print()

      



      