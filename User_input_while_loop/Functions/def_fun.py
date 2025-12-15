#Defining a function
""" IF you need to perform the same task multiple time again and again you just call the function dedicated to handeling that task, and the call tells python to run the code inside the function. """

#Here we will define a simple function that prints greeting:

def greet_user():
      print('Hello!')

""" A function call tells python to execute the code in the function, followed by any necessary information in parentheses"""
greet_user()

#passing information to a function 

def greet_userr(username):
      print(f"Hello, {username.title()}!")

greet_userr('jesse')

#parameter and argument 
""" 
Parameter is a piece of informationi the function needs to its job. 
Argument is a piece of information that is passed from a function call to a function.

"""
