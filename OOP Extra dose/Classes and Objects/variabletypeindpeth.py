class Student:
      college_name='srh'#static variable 
      def __init__(self,name,roll):
            self.name=name #instance variable 
            self.roll=roll #instance variable
      
      def getStudentInfo(self):
            print("Student Name: ",self.name)
            print("Student Roll: ", self.roll)
            
            
      @classmethod
      def getCollegeInfo(cls):
            print("College Name is ", cls.college_name)
      @staticmethod
      def m1(a,b):
            print("The Sum is ", a+b)


s=Student("Subash", 20)
s.getStudentInfo()
s.getCollegeInfo()
s1=Student("Pragyan", 22)
s1.getStudentInfo()
s1.getCollegeInfo()
s2=Student("Shiva",23)
s2.getStudentInfo()
s2.getCollegeInfo()
#value of variable changes in each object 



