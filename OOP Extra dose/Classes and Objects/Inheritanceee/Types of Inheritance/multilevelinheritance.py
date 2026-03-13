class P:
      def m1(self):
            print("Parent Class ")
class C(P):
      def m2(self):
            print("Child method")
class CC(C):
      def m3(self):
            print("Child Child method ")

d=CC()
d.m3()
d.m1()
d.m2()