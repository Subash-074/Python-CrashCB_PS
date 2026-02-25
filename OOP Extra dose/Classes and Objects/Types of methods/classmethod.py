#Class Method 
# Class Method is where all static(class level variable) are used then that method is class method 

#To make class method one decorator is cumpolsory and that is : @classmethod

#To access class method  we can access it through class name or cls variable since first argument of class method is cls 
#class_name/cls 

class Srh:
      department=4
      @classmethod
      def work(cls, name):
            print("Srh has {cls.department} department ")

#a=Srh()
#a.work('computer') this way of accessing class method is wrong 


Srh.work("computer") #if you are making classmethod inside the class  then directly access it through class name. 




