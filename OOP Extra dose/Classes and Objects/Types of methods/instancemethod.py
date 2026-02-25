#Instance Method 
#Instance method is a method which have at least one instance variable.
#instance method have first argument self 
#instance method is called inside the class by using self keyword 
#instance method is called outside  the class by refrence variable
#instance method can also have other variables as well but it must have at least one instance variabel and first argument must be self 
#instance method must be accessed through object. 
class Student:
      def __init__(self, name, marks):
            self.name=name
            self.marks=marks
      def display(self):
            print("Hi ", self.name)
            print("Your marks is ", self.marks)

      def grade(self):
            if self.marks >=60:
                  print("First Grade student. ")
            elif self.marks >=50:
                  print("Second Grade Student. ")
            else:
                  print("You are fail. ")

n=int(input("Please Enter How many students? "))
for i in range(n):
      name=input("Enter your name. ")
      marks=int(input("Enter your marks. "))
      s=Student(name, marks)
      s.display()
      s.grade()
      print()
