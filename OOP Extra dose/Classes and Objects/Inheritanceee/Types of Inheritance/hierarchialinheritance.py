class P:
      def m1(self):
            print("Parent Class")
class C1(P):
      def m2(self):
            print("This is first child ")
class C2(P):
      def m3(self):
            print("This is second child ")

c=C1()

c.m1()
c.m2()

d=C2()
d.m1()
d.m3()

