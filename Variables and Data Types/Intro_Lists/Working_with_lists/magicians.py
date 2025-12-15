#Looping through the entire list 
magicians=['alice', 'david', 'carolina']
for magician in magicians:
      print(magician)
#a closer look at looping
""" The concept of looping is important because it is one of the most common ways a computer automates repetitive tasks """

""" Also keep in ming when writing your own for loops that you can choose any name you want for the temporary variable that will be associated with each valuse in the list.
Here is a good way to start a for loop for a list of cats, a list of dogs, a general list of items: 

for cat in cats:
for dog in dogs:
for items in list_of_items:
"""
#You can go just about anything with each item in a for loop 

friends= ['ram', 'shyam', 'gita', 'hari']
for friend  in friends:
      print(f"{friend.title()}, that was a great trick!")
      print(f"I can't wait to see your next trick, {friend.title()}.\n")

#python is super sensitive always check for indentation error, indentation means appropraite space in for loop where print cannot me paralled with for in next line it should be properly indented.
#Do not forget to indent additional lines as well 

#Indenting Unnecessarily should be avoided
#Indenting Unnecessarily after the loop is not necessary 
#forgeting a colon at the end of the for statement 


