#copying a list 
my_foods=['pizza', 'falafel', 'carrot cake']
friend_foods=my_foods[:]

print("my favouriate food are:")
print(my_foods)

print('\n my friends favouriate foods are:')
print(friend_foods)



# here my_foods and friends_foods are now two seperate lists we will add two different items in each of this lists 

my_foods.append('momos')
friend_foods.append('samosa')

print(my_foods)
print(friend_foods)

#if we had simply tried my_foods=friends_food we would not have been able to create two seperate list. 
