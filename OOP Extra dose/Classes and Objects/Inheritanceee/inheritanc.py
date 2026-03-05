#Is-a relation (Inheritance)
#The process of creating new classes based on some existing classes is called inheritance. 

#Suppose you create one small class and then create another big class which will have all the features of small class  plus extra features or functionality this is in general terms inheritance. 

class P:
      def m(self):
            print("This is m method of class P")
class C(P):
      def m1(self):
            print("This is m1 method of class C")


c=C()
c.m()
c.m1()



