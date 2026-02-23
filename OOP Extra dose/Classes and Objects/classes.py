#Classes and Object 
"""
Suppose we want to build a house 
we need a plan to build any house :this plan is class 
With that plan we can build different house in different places and that house we built is object. 
"""
#class is the blueprint of anything to be built 
#Class== blueprint/ template/ plan/ models /designs


#physical instance of a class is called an object


#Class/Object/Refrence Variable 


"""
Suppose a TV manufacturing company has a board meeting about the features which they want in their product 

Board meeting decided, TV will have 50 inch display, clor black, large screen, channel change features, ====This is called class 

Now the plan moves  to the manufacturing department  and all thousands of TV with all the features decided from board meeting will be built==== This is called Objects 



"""

"""
Now you take that TV manufactured which we called an Object in programming terms.

To operate that tv we need one remote to access it and use everything inside. In programming terms these reomte are known as refrence variable. Put simply, Refrence Variable operates objects. 

Now let's say that remote is lost. How will you operate that TV you will now go back to Manufacturer or find remote for same remote. 
Similarly in programming there can be multiple refrence variable(tv remotes) to access single object.

"""


#Now in layman's term the concept of class, object and refrence variable in programming is clear. 

#If your object do not have refrence variable it become eligible for garbage collection. 



#There are two things inside calsees 
#Attributes(properties)  variables 
#variables(actions) methods/  functions ===functions written inside class are called methods



#how to make clase 
#Syntax: 

"""
class className: 
'''docstring''' optional 
variables 
methods()


"""

class A:
      '''This class is demo class. This class does nothing.'''
      #attributes/variables==instance(object level) variable(more than 80%), (class level variable)static variable, (method level variable)local variable(15%)
      
      
      #behaviour/methods()=== Instance method(more than95% casee this is used), class method, static method

#To make empty class 
class B:
      pass 
#This pass statement states theres is nothing to do inside this class but in future you can add something  


#object syntax:
#refrence variable: ClassName()



class Student:
      '''This class is made for student. '''
      def __init__(self):
            self.name='Subash'
            self.age=21
            self.marks=99
      def talk(self):
            print("Hello my name is ", self.name)
            print("Hello my name is ", self.age)
            print("Hello my marks is ", self.marks)

s=Student()
print(s.name)
print(s.marks)
s.talk()


"""  
Now let's decode why is there

def __init__(self):
This is called constructor in python. 

When any object is made out of the class if we want something to be automatically there when object is made out of that class then we put those things in method init .
This is automatically called when object is made out of that class. 

Now why is there self in argument section 

It is because in any method inside class first argument must always be self. 

refrence variable can only be used outside the class but self can be called inside  class and values can be assigned. You can clearly see we have assigned name age and marks in above mentioned code example.

Self()
Defalut variable that points to current object 
By using self we can access:
instance variable
instance methods



"""


class B:
      def __init__(self):
            print(id(self))

s=B()
print(id(s)) #Here you can clearly observe Id of self argument inside init method and refrence variable s is same... Why is that???/


#Note that you cannot use self outside class. 


