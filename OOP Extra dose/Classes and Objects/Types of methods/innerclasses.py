#Inner Classes:
"""
Let's say you have a class called a car. you must have a class called engine, which is a part of the car. so you can create a class called engine inside the car class. this is called an inner class. the inner class can access the attributes and methods of the outer class. but the outer class cannot access the attributes and methods of the inner class.

similarly in university class there are different departments like computer science, mechanical, civil etc. so you can create a class called department inside the university class. this is called an inner class. the inner class can access the attributes and methods of the outer class. but the outer class cannot access the attributes and methods of the inner class. without university there is no chance of existence of department. so it is better to create a class called department inside the university class. this is called an inner class. 

in thiese cases inner class is very useful because it helps to organize the code and makes it more readable. it also helps to avoid name conflicts between the outer class and the inner class.


"""
"""
class Outer:
      def __init__(self):
            print("Outer classs. ")
      class Inner:
            def __init__(self):
                  print("Inner class. ")
            def m(self):
                  print("Inner class method. ")
o=Outer()
i=o.Inner() 
i.m() """

"""#i=Outer().Inner() this is also valid but it is not recommended because it creates an object of outer class every time you create an object of inner class. so it is better to create an object of outer class and then create an object of inner class through that object of outer class.

Outer().Inner().m()  #this is also valid but it is not recommended"""


"""class Outer:
      def __init__(self):
            print("Outer object is created. ")
      class Inner:
            def __init__(self):
                  print("Inner Object is created.")
            class InnerInner:
                  def __init__(self):
                        print("Inner Inner Object is created. ")
                  def m(self):
                        print("Inner Inner class. ")
ii=Outer().Inner().InnerInner()
ii.m()"""

"""
class Human:
      def __init__(self,name):
            self.name='Subash'
            self.head=self.Head()  
            self.brain=self.Brain()
      def display(self):
            print("Hello", self.name)
      class Head:
            def talk(self):
                  print("Print Brain can think")
      class Brain:
            def think(self):
                  print("Brain can think")
h=Human()
h.display()
h.head.talk()
h.brain.think()"""


class Human:
      def __init__(self,name):
            self.name=name
            self.head=self.Head()
      def info(self):
            print("Hello my name is ",self.name)
      class Head:
            def __init__(self):
                self.brain=self.Brain()
            def talk(self):
                  print("Talk")
            class Brain:
                  def think(self):
                        print("Think")   
h=Human("Subash")
h.head.talk()
h.head.brain.think()