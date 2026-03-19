#Operator overloading 
# print(20+30)
# print('Hello'+'world')
# print(10*10)
# print(3*'A')


# class Book:
#       def __init__(self, pages):
#             self.pages=pages
#       def __add__(self, other):
#             return self.pages +other.pages


# b1=Book(200)
# b2=Book(100)
# print(b1+b2) 
 
# class Student:
#       def __init__(self, name, marks):
#             self.name=name
#             self.marks=marks
#       def __gt__(self, other):
#             return self.marks>other.marks
      
# s=Student("Dipesh", 99)
# s1=Student("Vaskar", 97)
# print(s>s1)



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# class AttendanceSheet:
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days

#     def __mul__(self, other):              # properly indented inside class
#         return other.salary * self.days

# e = Employee("Subash", 5000)
# t = AttendanceSheet("Vaskar", 15)
# print("Total Salary : ", t * e)


# class Student:
#       def __init__(self, name, roll, marks):
#             self.name=name
#             self.marks=marks
#             self.roll=roll
#       def __str__(self):
#             return f"This is {self.name} object"
      
# s1=Student("Subash", 101, 90)
# s2=Student("Susmita", 202, 99)

# print(s1)
# print(s2)

class Book:
      def __init__(self,pages):
            self.pages= pages 
      def __add__(self, other):
            return Book(self.pages+other.pages)
      def __str__(self):
            return f"Total Number of pages is {self.pages}"
      def __mul__(self, other):
            print("This is multiplication ")
            return Book(self.pages*other.pages)
      
b1=Book(200)
b2=Book(100)
b3=Book(300)
b4=Book(900)
print(b1+b2*b3+b4)

