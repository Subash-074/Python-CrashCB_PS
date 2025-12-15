#Organizing a list 
#sorting lists with sort method 
cars=['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#you can also sort it in reverse order
cars.sort(reverse=True)
print(cars)

#sorting temporarily with the sorted function 

names=['ram', 'shyam', 'hari', 'gita']
print(sorted(names))
print(names)

#printing the list in recerse order
names.reverse()
print(names)


#finding the length of lists
print(len(names))
print(len(cars))