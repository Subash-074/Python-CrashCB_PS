#Method overriding 

# class P:
#       def property(self):
#             print("Gold +land +cash")
#       def wife(self):
#             print("Katrina")

# class C(P):
#       def wife(self):
#             super().wife()
#             # print("Kajol")
# c=C()
# c.property()
# c.wife()








#Constructor Overriding 
# class P:
#       def __init__(self):
#             print("Parent Constructor")
# class C(P):
#       def __init__(self):
#             print("child class constructor ")#this will override constructor of parent class and output child class consturctor 
#             #if we want to call parent class constructor we can always use super().__init__()
# c=C()           





#Duck Typing 
#If any animal swims like a duck(object), walk like a duck and quaks like a duck, then that animal is duck 

class Duck:
      def talk(self):
            print("Quack Quack ")

class Dog:
      def talk(self):
            print("Bhow, Bhow")

class Cat:
      def talk(self):
            print("Moew Moew")
class Goat:
      def talk(self):
            print("Maaa Maaa")


def f1(obj):
      obj.talk()

l=[Duck(), Dog(), Cat(), Goat()]

for obj in l:
      f1(obj)

