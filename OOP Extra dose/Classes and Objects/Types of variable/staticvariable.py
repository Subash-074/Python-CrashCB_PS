#Static Variable 
""" Those variable whose value shared by all the objects and for all objects single variable with single id is present. Common variable vaule shared by all the objects"""

class Test:
      a=10  #inside the class but outside the methods 
      def __init__(self):
            print(Test.a)
            print(self.a)
        
      
      def m1(self):
            Test.a=30
            print(Test.a)
            print(self.a)
      
      @classmethod
      def m2(cls):
            Test.a=50
            cls.a=60
            print(Test.a)
            print(cls.a)
      @staticmethod
      def m3():
            Test.a=50
            print(Test.a)

t=Test()
t.m1()
t.m2()
t.m3()
print(Test.__dict__)




