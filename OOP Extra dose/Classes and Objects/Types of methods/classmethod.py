#Class Method 
# Class Method is where all static(class level variable) are used then that method is class method 

#To make class method one decorator is cumpolsory and that is : @classmethod

#To access class method  we can access it through class name or cls variable since first argument of class method is cls 
#class_name/cls 

"""class Srh:
      department=4
      @classmethod
      def work(cls, name):
            print("Srh has {cls.department} department ")

#a=Srh()
#a.work('computer') this way of accessing class method is wrong 


Srh.work("computer")""" #if you are making classmethod inside the class  then directly access it through class name. 


class Test:
      count = 0
      def __init__(self):
            Test.count += 1
      @classmethod
      def no_of_objects(cls):
            print("Number of created objects are : ", cls.count)

t1 = Test()
Test.no_of_objects() #since no_of_objects is class method we can access it through class name
t2= Test()
Test.no_of_objects() 
t3.Test()
t3.no_of_objects






"""

Difference between instance method and class method 

Instance method: It must have at leasst one instance variable and it is used to access instance variable and instance method. It is accessed through object name.

It can have instance variable and static variable  and local variable  but it is used to access instance variable and instance method. It is accessed through object name.
first argument of instance method is self and it is used to access instance variable and instance method.
no decorator is required to make instance method.
called using object name.

class method: It must have at least onr static variable and it is used to access class variable and class method. It is accessed through class name or cls variable.
only static variable is used in class method. 
 
first argument of class method is cls and it is used to access class variable and class method.
decorator @classmethod is required to make class method.
call by using class name.




"""
