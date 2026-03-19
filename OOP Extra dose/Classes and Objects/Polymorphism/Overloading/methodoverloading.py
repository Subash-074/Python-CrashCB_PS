#Method overloading 
# if name of method is same but arguments are different this kind of situation is method overloading 
#usually method overloading do not exist in python but it may be done in below code type execution 
class Test:
      def sum(self, *a):
            total=0
            for x in a:
                  total=total+x
                  print("The sum is : ", total )
t=Test()
t.sum()
t.sum(10)
t.sum(10,20,30)
t.sum(10,20,30,40,50,60,70,80,90)
