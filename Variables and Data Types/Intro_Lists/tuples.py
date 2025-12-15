#Tuple
#Sometimes you might want to create a list of items that cannot change.An immutable or unchangable list is called a tuple 

#let's define a tuple with a dimensions of a rectangle with its length and breadth 

dimensions=(200, 50)
print(dimensions[0])
print(dimensions[1])

#let's see what happens when we try to change one of the items in the tuple 

"""dimensions[0]= 250""" # this will result in error in output 


#Loopint through all values in a tuple 
for dimension in dimensions:
      print(dimension)

#although you cannot modify tuple you can also redifeine same tuple with different dimension and print it again 

dimensions=(250, 44)
for dimension in dimensions:
      print(dimension)


