class P1:
      def m1(self):
            print("Parent one method")
class P2:
      def m1(self):
            print("Parent two method ")
class C(P1, P2):
      def m3(self):
            print("This is child class method ")
c=C()
c.m1()
c.m3()
