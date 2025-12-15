#How the input() Function Works 
"""message= input('Tell me something, and i will repeat it back to you:')
#it displays message you kept inside input function , when you print message it displays your input

print(message)"""

#Writing clear prompts 

"""name=input('Please enter your name: ')
print(f"\n Hello, {name}!")"""

#sometimes you might want a longer prompt which is more than one line 

"""prompt=" IF you tell us who you are, we can personalize the message you see. "

prompt+="\nWhat is your first Name?"

name=input(prompt)
print(f"hello, {name}")"""

#Using int() to accept numerical input 


"""age=input("How old are you?")
age=int(age)

print(age>=18)

"""

#write a program to determine weather people are tall enough to ride a roller coaster:

"""height=input("How tall are you in inches? ")
height=int(height)

if height>=48:
      print("\nYou're tall enough to ride!")

else:
      print("\nYou'll be able to ride when you're a little older. ")"""

#The Modulo Operator 
print(4%3)#returns remainder

#write a program to identify weather a number is odd or even

"""number=input("Enter a number, and i will tell you if it is odd or even.")

number= int(number)

if number%2==0:
      print(f"\n The number {number} is even.")
else:
      print(f"\n The number {number} is odd. ")"""


#Write a program that ask user for a number, and then report weather a number is a multiple of 10 or not.

number=input("Give me a number and then I will tell you weather it is a multiple of 10 or not. ")

number=int(number)


if number%10==0:
      print(f"The given number {number} is a multiple of 10.")
else:
      print(f"The given number {number} is not multiple of 10")