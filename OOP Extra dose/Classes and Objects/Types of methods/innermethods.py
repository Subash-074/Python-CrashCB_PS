#methods inside methods are called inner methods

class Test:
      def m(self):
            def calc(a,b):
                  print("Sum :",a+b)
                  print("Difference :",a-b)
                  print("Product :",a*b)
            calc(10,20)
            calc(100,200)
            calc(1000,2000)
            calc(10000,20000)
t=Test()
t.m()

