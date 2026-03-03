"""import time
class Test:
      def __init__(self):
            print("This is constructor")
      def __del__(self):
            print("This is destructor ")
t=Test()
print("End of application")
time.sleep(5)
t1=t
t2=t
print("Test object has 3 ref now")
del t
print("T object is deleted ")

time.sleep(5)
del t1
print("t1 refrence is deleted.")
del t2
print("t2 refrence is deleted. ")
time.sleep(5)
print("End of application")"""

import sys
class Test:
      def __init__(self):
            print("This is constructor")
      def __del__(self):
            print("This is destructor")
l=[Test(), Test(), Test()]
del l
print("End of application")


print(sys.getrefcount())



"""
Differences between Constructor and Distructor 

Constructor -  __init__(self)
instance variable initialiazation or default variable inside class 
it is called as soon as object is made 


Destruactor: __del__(self)
clean up activities/ resource deallocation from python virtual machine 
it is called just before Garbage collector destroys the object. 



"""
