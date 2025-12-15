#slicing a list 
""" to make a slice, you specify the inded of the first and last elements you want to work with. """

players=['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])

#you can omit first place and specify last item as well, in this case python start form first element of that list with index 0

print(players[:3])

#similarly, you can also omit the last index number 
print(players[1:])

#you can also use negative indexing 
print(players[-3:])

#here last three items of the list will be printed 


#This is all about slice, we explored different method to slice items form the list


#looping through a slice 
players1 = ['charles', 'martina', 'michael', 'florence', 'eli'] 

for player in players1[:3]:
      print(player.title())

#we can already observe instead of printing entire list python only print only first three items of list 


