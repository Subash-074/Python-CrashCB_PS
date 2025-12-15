#slices
""" Using one of the programs you wrote in this chapter, add several lines ot the end of the program that do the following: """


#print the message The first three items in the list are: then use a slice to print the
 
# first three items form that program's list.
hehe=['sagar', 'brinda', 'bimala', 'bunu']
print('The first three items in the list are:\n')
print(hehe[0:3])

#middle three items in the list
haha=['cat', 'dog', 'elephant', 'tiger', 'leopard', 'snake']
print('Three items form the middle of the list are:\n')
print(haha[1:4])

#last three items in the list
huhu=['aaa', 'bbb', 'ccc', 'dddd', 'eee', 'fff', 'ggg', 'hhh']

print(huhu[5:])


# my fav foods , your fav foods  
""" start with your program from the exercise. make a copy of the list of pizzas, and call it friend_pizzas"""

my_fav=['momo', 'samosa', 'crossant']

your_fav=my_fav[:]

my_fav.append('dognut')

your_fav.append('tea')

print(my_fav)

for food in your_fav[:]:
      print(food)



