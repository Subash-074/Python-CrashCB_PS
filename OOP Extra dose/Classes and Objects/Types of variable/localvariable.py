#local variable
#if we make variables inside methods to fulfill temporary requirements then those variable are called local variabe.
#The scope of local variable is within a function only. 
"""
class Test:
      @staticmethod
      def average(list):
            result=sum(list)/len(list)
            return result 

list=[10,20,30,40]
t=Test()
t.average(list)
"""

class Test:
      def m1(self):
            self.a=1000
            print(self.a)
      def m2(self):
            b=2000
            print(self.a)
            print(b)
t=Test()
t.m1()
t.m2()
