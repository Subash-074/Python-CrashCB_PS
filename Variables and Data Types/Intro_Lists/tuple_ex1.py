""" Buffet: a buttet style restaurant offers only five basic foods. Think of five simple foods and store them in a  tuple """
 
foods=('burger', 'pizza', 'momo', 'pasta', 'sandwitch')

#use for loop to print each food the restraurants offers 

for food in foods:
      print(food)

#try to modify one of the items, and make sure that python rejects the change 

"""foods[0]='pasta'""" #error

""" The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrite the tuple and then use a for loop to print each of the items on the revised menu."""

foods=('burger', 'pizza', 'momo', 'dooner', 'samosa')
print('revised menu: ')
for food in foods:
      print(food)


