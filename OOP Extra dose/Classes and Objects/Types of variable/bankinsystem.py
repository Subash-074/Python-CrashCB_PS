#Bank System 
import sys
class Customer:
      """ This is Bank System """
      bankname="Sparkasse"
      def __init__(self, name, balance=0.0):
            self.name=name
            self.balance=balance
      def deposit(self, amt):
            self.balance=self.balance +amt
            print("New Balance After Deposit:", self.balance)
      def withdraw(self, amt):
            if amt>self.balance:
                  print("Insufficient Fund. Please deposit first. ")
                  sys.exit()
            else:
                  self.balance=self.balance=amt
                  print("Balance after withdraw:", self.balance)     


print("Welcome to Sparkasse Bank")

name=input("Enter your name: ")
c=Customer(name)

while True:
      print("D-Deposit\n W-Withdraw \n E-Exit")
      option=input("Enter your option: ")
      if option=='D' or option =="d":
            amt=float(input("Enter the amount you want to deposit. "))
            c.deposit(amt)
      elif option=='W' or option=='w':
            amt=float(input("Enter the abmount you want to withdraw "))
            c.withdraw(amt)
      elif option=='e' or option =="E":
            print("Thank you for using our service ")
            c.withdraw(amt)
            sys.exit()
      else:
            print("Ivalid option. Please choose valid option. ")





      

