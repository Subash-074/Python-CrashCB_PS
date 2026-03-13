#collection of different type of inheritance is called hybrid inheritance. 

# class A:
#       def m1(self):
#             print("A class method ")
# class B(A): 
#       def m2(self):
#             print("B class method ")
# class C(A):
#       def m1(self):
#             print("C class method ")
# class D(B, C):
#       def m2(self):
#             print("C class method ")

# d=D()
# d.m1()


#Method Resolution Order concept is used here below

class A:
      def m1(self):
            print("A class method ")
class B:
      def m1(self):
            print("B class method ")

class C:
      def m1(self):
            print("C class method ")

class X(A,B):
      def m3(self):
            print("X Class method ")

class Y(B, C):
      def m1(self):
            print("Y class method ")
class P(X, Y, C):
      def m2(self):
            print("P class method ")


p=P()
print(P.mro())
p.m1()

#Here Method Resolution order of P is  PXAYBCO





#MRO Algorithm/C3 algorithm 
#How this algorithm works?
#MRO(X)=X + Merge(Mro(c1)-Mro(c2)....)
#you can just see the chain by simply usnig .mro() method 




