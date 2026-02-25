#There are two special instance methods 
#1)setter/mutator 2)getter()/Accessor  methods 


class Student:
      def setName(self, name): #setter method
            self.name=name
      def getName(self):#getter method
            return self.name
      def setMarks(self, marks):#setter method 
            self.marks=marks
      def getMarks(self):#getter method 
            return self.marks

n=int(input("Enter number of student : "))
for i in range(n):
      s=Student()
      name=input("Enter your Name: ")
      s.setName(name)
      marks=int(input("Enter your Marks: "))
      s.setMarks(marks)
      print("Hi ", s.getName())
      print("Your marks is ", s.getMarks())
      print()