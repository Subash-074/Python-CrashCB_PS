#Static Method :
class Math:
      @staticmethod
      def add(x,y):
            print("The sum is : ",x+y)
      @staticmethod
      def mul(x,y):
            print("The product is : ",x*y)
      @staticmethod
      def sub(x,y):
            print("The difference is : ",x-y)

Math.add(10,20)
Math.mul(10,20)
Math.sub(10,20)


"""
class Test:
def m1(x):
    pass

t=Test()
t.m1()   #if you call through object then it is instance method 

class Test:
@staticmethod
def m1(x):
    pass
Test.m1(10)  #if you call through class then it is static method
you can also call static method through object but it is not recommended because it is not the way to call static method
t=Test()
t.m1(10)  #it is not recommended because it is not the way to call static method


"""