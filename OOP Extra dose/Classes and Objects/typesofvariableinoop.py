"""
In functional programming there There are only two types of variable:
local variable (variable inside function)
global variable (variable outside function)

In Object Oriented Programming:
There are three types of variable 
-Instance Variable(Object level Variable)
-Static Variable(Class Level Variable)
-Local Variable(Method Level Variable)



"""
#Instance Variable:
""" Instance variable is the variable whose value is  different from object to object 

for Example you called an object to keep record of student information now you call that object with refrence variable s1 with first student info, s2 with second student info, s3 with third student info and so on  Now  you can see value of name, class roll number in different object called is different .


first argument of instance variable is self 

class Student:
      def __init__(self, name, roll)
      self.name=name
      self.roll=roll
s1=Student("Subash", 10)  ==object 1 
s2=Student("Sagar", 11)==object 2 
"""

#static variable (whose value is same in all objects )
"""
Now college name of all the students is same if we use instance variable everytime we call an object there will be seperate copies of college name which is not necessary while we can store this in single id and call it back and forth for different students 


"""


#Local Variable(whose value is used inside methods(functions inside of class) of class)
"""
variables used inside methods. It's scope is limited within method only we cannot use it outside. 

"""


"""
Similarly There are three types of methods used in classes in python they are:
Instance Method(at least 1 instance variable: first argument: self)

Class Method (static variable or class level variable only used : first argument must be 
cls


@class method 
def getschoolInfo(cls):
       print('school Name; cls.collegename') )



Static Method 
Those methods which use make normal methods for temporary used 

@staticMethod
def getSum(a,b):






"""