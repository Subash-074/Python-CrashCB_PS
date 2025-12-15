#hello admin 

usernames=['admin', 'subash', 'sagar', 'bimala']

for username in usernames:
      if username == 'admin':
            print(f"Hello {username}")
      else:
            print(f"Hello {username}, thank you for logging in again. ")


#no user 

users=[ ]

if users:
      for user in users:
            print(f"hello{user}")
else:
            print('empty list ')


#checking usernames 

current_users=['sagar', 'bimala', 'brinda', 'rahul']

permanent_users=['lina', 'sam', 'sagar', 'rahul']

for permanent_user in permanent_users:
       if permanent_user in current_users:
              print(f"{permanent_user} must not be accepted it is already permanent")
       else:
              print(f"{permanent_user} must be accepted automatic in current list.")

       

# ordinal numbers 
"""Store the numbers 1 through 9 in a list.
•	 Loop through the list.
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.

"""

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
       if number==1:
              print(f"{number}st")
       elif number==2:
              print(f"{number}nd")
       elif number==3:
              print(f"{number}rd")
       else:
              print(f"{number}th")


