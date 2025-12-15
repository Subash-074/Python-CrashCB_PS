#Using a while Loop with Lists and Dictionaries
"""  
A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track of the
items in the list. To modify a list as you work through it, use a while loop.
Using while loops with lists and dictionaries allows you to collect, store, and
organize lots of input to examine and report on later. 


"""
#Moving items from one list to another 


#start with users that need to be verified, 
#and an empty list to hold confirmed users,
unconfirmed_users=['alice', 'brain', 'candace']
confirmed_users=[]

#verify each user untill there are no more unconfirmed users 
#move each verified user into the list of confirmed users.

while unconfirmed_users:
      current_users=unconfirmed_users.pop()

      print(f"Veryfying user: {current_users.title()}")

      confirmed_users.append(current_users)

#display all confirmed users.
print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
      print(confirmed_user.title())


#Removind all instances of specific valuse form a list 

"""  we used remove() to remove a specific value from a list. The
remove() function worked because the value we were interested in appeared
only once in the list. But what if you want to remove all instances of a value
from a list?"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
 pets.remove('cat')

print(pets)


#Filling a dictionary with a user input 
""" let's make a pooling program in which each pass through a loop prompts for a participant's name and response. We'll store the data we gather in a dictionary, because we want to connect each response with a particular user. """

responses= {}
#set a flag to indicate that pooling is active 
pooling_active=True 

while pooling_active:
    #prompt for the person's name and response 
    name=input("\nWhat is your name?")
    response=input("Which mountain would like to climb someday?")

    #store the response in the dictionary 
    responses[name]=response

    #find out if anyone else is going to take the pool 
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':
        pooling_active=False

     #Pooling is complete . show the results.
print("pool results")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")