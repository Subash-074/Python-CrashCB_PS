"""class Test:
      a=10
      def m1(self):
            self.a=100
t1=Test()
t1.m1()
print(Test.a) #output is 10
print(t1.a)  #output is 100
"""
#example 2
"""class Test:
      x=10
      def __init__(self):
            self.y=20

t1=Test()
t2=Test()

print(t1.x, t1.y)#output is 10, 20
print(t2.x, t2.y)#output is 10,20

t1.x=111
t1.y=222

print(t1.x, t1.y)# output is 111, 222
print(t2.x, t2.y)#output is 10,20"""

#Example 3
"""class Test:
      a=10
      def __init__(self):
            self.b=20

t1=Test()
t2=Test()
Test.a=111
t1.b=222
print(t1.a, t1.b)#111,222
print(t2.a, t2.b)#111,20"""


#Example 4
"""class Test:
      a=10
      def __init__(self):
            self.b=20
      def m1(self):
            self.a=111
            self.b=222
t1=Test()
t2=Test()
t1.m1()
print(t1.a, t1.b)#111, 222
print(t2.a, t2.b)#10,20"""




#Example 5
"""class Test:
      a=10
      def __init__(self):
            self.b=20
t1=Test()
t2=Test()
Test.a=111
t1.b=222
print(t1.a, t1.b)#111,222
print(t2.a, t2.b)#111,20"""



#Example 6
"""class Test:
      a=10
      def __init__(self):
            self.b=20
      @classmethod
      def m1(cls):
            cls.a=111
            cls.b=222

t1=Test()
t2=Test()
t1.m1()
print(t1.a, t1.b)#111,20
print(t2.a, t2.b)#111, 20
print(Test.a, Test.b)#111,222"""



"""#deleting Static Variable
class Test:
      a=10
      @classmethod
      def m1(cls):
            del cls.a
            #del Test.a        both way is same 
t= Test()
t.m1()
#to delete outside the class : del Test.a
print(Test.__dict__)
"""


"""
#You Cannot delete in this case 
class Test:
      a=10

t1=Test()
del t1.a #this is invalid """




