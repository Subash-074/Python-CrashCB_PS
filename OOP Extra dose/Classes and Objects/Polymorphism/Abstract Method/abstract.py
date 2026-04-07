from abc import abstractmethod , ABC


# class Test:
#       @abstractmethod
#       def m1():
#              pass
      
# class Vehicle(ABC):
#        @abstractmethod
#        def noofwheels(self):
#               pass
       
# class Bus(Vehicle):
#        pass

# b=Bus()

# Abstract class with abstract method instantiaon is not possible. 



# class Test:
#       @abstractmethod
#       def m1(self):
#             print("Hello")
# t=Test()

#INterface classes which have only abstract methods 

class A(ABC):
      @abstractmethod
      def m1(self):pass
      @abstractmethod
      def m2(self):pass
      @abstractmethod
      def m3(self):pass
      