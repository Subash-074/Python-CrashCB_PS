#Introducing while loops 
""" The for loop takes a collection of items and execute a block of code once for ecah item in the collection. In contrast while loop runs as long as, or while a certain condition is true. """

#The while loop in action 
""" You can use a while loop to count up through a series of numbers. For example, the following whild loop count from 1 to 5. """

"""current_number=1

while current_number<=5:
      print(current_number)
      current_number+=1
"""

#Letting the User Choose when to quit 
"""prompt= "\n Tell me something, and I will repeat it back to you: "
prompt+="\n Enter 'quit' to end the program. "

message=""

while message!="quit":
      message=input(prompt)
      print(message)"""


#Using a Flag 
""" 
For a program that should run only as long as many conditions are true,
you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We
can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False. As a result,
our overall while statement needs to check only one condition: whether or
not the flag is currently True

"""

"""prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active=True
while active:
      message=input(prompt)
      
      if message=='quit':
            active=False
      else:
            print(message)"""


#Using break to Exit a Loop
"""To exit a while loop immediately without running any remaining code in the
loop, regardless of the results of any conditional test, use the break statement"""
"""
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
   city = input(prompt)
   if city == 'quit':
          break
   else:
       print(f"I'd love to go to {city.title()}!")
"""

#Using continue in a loop 
current_number=0
while current_number<10:
      current_number+=1
      if current_number%2==0: #if current number is not divisible by 2 it is executed, if it is divisible it is not displayed as output 
            continue
      print(current_number)